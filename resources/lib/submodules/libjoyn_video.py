# -*- coding: utf-8 -*-

from hashlib import sha1
from ..xbmc_helper import xbmc_helper
from .. import compat
from ..const import CONST
from ..lib_joyn import lib_joyn
from base64 import b64decode

if compat.PY2:
	from urllib import urlencode
	from urlparse import urlparse, urlunparse, parse_qs
	try:
		from simplejson import dumps
	except ImportError:
		from json import dumps
elif compat.PY3:
	from urllib.parse import urlencode, urlparse, urlunparse, parse_qs
	from json import dumps


def build_signature(encoded_client_data, entitlement_token):

	sha_input = compat._format('{},{}{}', encoded_client_data, entitlement_token,
	                           compat._decode(b64decode(CONST.get('SIGNATURE_KEY'))))

	xbmc_helper().log_debug('Build signature: {}', sha_input)
	return sha1(sha_input.encode('utf-8')).hexdigest()


def get_mpd_parser(url, stream_type='VOD', video_id=None):

	from ..mpd_parser import mpd_parser

	xbmc_helper().log_debug('set_mpd_props {} stream_type {}', url, stream_type)
	mpdparser = None

	# strip out the filter parameter
	parts = urlparse(url)
	query_dict = parse_qs(parts.query)

	if 'filter' in query_dict.keys():
		query_dict.update({'filter': ''})
		new_parts = list(parts)
		new_parts[4] = urlencode(query_dict)
		new_mpd_url = urlunparse(new_parts)
		xbmc_helper().log_debug('Stripped out filter from mpd url is {}', new_mpd_url)
		try:
			mpdparser = mpd_parser(new_mpd_url, lib_joyn().config)
		except Exception as e:
			xbmc_helper().log_debug('Invalid MPD - Exception: {}', e)
			pass

	if mpdparser is None or mpdparser.mpd_tree is None:
		try:
			mpdparser = mpd_parser(url, lib_joyn().config)
		except Exception as e:
			xbmc_helper().log_error('Invalid Orginal MPD - Exception: {}', e)

	if mpdparser is not None:

		toplevel_base_url = mpdparser.get_toplevel_base_url()
		if xbmc_helper().get_bool_setting('fixup_vod') is True and stream_type == 'VOD' and toplevel_base_url is not None:
			if toplevel_base_url.startswith('http'):
				new_mpd_url = compat._format('{}.mpd?filter={}', toplevel_base_url, CONST.get('MPD_FILTER'))
				xbmc_helper().log_debug('Try to force new MPD with URL: {}', new_mpd_url)
				try:
					_mpdparser = mpd_parser(new_mpd_url, lib_joyn().config)
					if _mpdparser is not None and _mpdparser.mpd_tree is not None:
						mpdparser = _mpdparser
						url = new_mpd_url
					else:
						raise Exception('Could not be parsed as valid MPD')
				except Exception as e:
					xbmc_helper().log_notice('Trying to force new MPD for VOD failed with URL: {} - Exception: {}', new_mpd_url, e)

		elif xbmc_helper().get_bool_setting('fixup_live') is True and stream_type == 'LIVE' and toplevel_base_url is not None:
			period_base_url = mpdparser.query_node_value(['Period', 'BaseURL'])
			if period_base_url is not None:
				new_mpd_url = compat._format('{}{}cenc-default.mpd', toplevel_base_url, period_base_url)
				xbmc_helper().log_debug('Trying to fixup Livestream with new URL: {}', new_mpd_url)
				try:
					_mpdparser = mpd_parser(new_mpd_url, lib_joyn().config)
					if _mpdparser is not None and _mpdparser.mpd_tree is not None:
						mpdparser = _mpdparser
						url = new_mpd_url
					else:
						raise Exception('Could not be parsed as valid MPD')
				except Exception as e:
					xbmc_helper().log_notice('Trying to fixup Livestream failed with new URL: {} - Exception: {}', new_mpd_url, e)

	if xbmc_helper().get_bool_setting('force_local_manifest') is True:
		mpdparser.set_local_path(video_id)

	return mpdparser


def get_entitlement_data(video_id, stream_type, pin_required=False, invalid_pin=False, force_refresh_token=False):

	from ..request_helper import post_json

	entitlement_request_data = {
	        'content_id': video_id,
	        'content_type': stream_type,
	}

	if pin_required is True:
		if invalid_pin is True:
			xbmc_helper().notification(xbmc_helper().translation('MPAA_PIN'), xbmc_helper().translation('MSG_INVALID_MPAA_PIN'))
		mpaa_pin_settings = xbmc_helper().get_text_setting('mpaa_pin')
		if len(mpaa_pin_settings) == 4 and invalid_pin is False:
			entitlement_request_data.update({'pin': mpaa_pin_settings})
		else:
			from xbmcgui import Dialog, INPUT_NUMERIC
			_fsk_pin = Dialog().input(xbmc_helper().translation('MPAA_PIN'), type=INPUT_NUMERIC)
			if len(_fsk_pin) == 4:
				entitlement_request_data.update({'pin': _fsk_pin})
			elif len(_fsk_pin) == 0:
				return {}
			else:
				return get_entitlement_data(video_id=video_id, stream_type=stream_type, pin_required=pin_required, invalid_pin=True)

	entitlement_request_headers = [('Authorization', lib_joyn().get_access_token(force_refresh=force_refresh_token))]
	entitlement_response = post_json(url=compat._format(
	        '{}/{}',
	        lib_joyn().config['entitlementBaseUrl'], CONST['ENTITLEMENT_URL']),
	                                 config=lib_joyn().config,
	                                 data=entitlement_request_data,
	                                 additional_headers=entitlement_request_headers,
	                                 no_cache=True,
	                                 return_json_errors=['ENT_PINRequired', 'ENT_PINInvalid', 'INVALID_JWT'])

	if isinstance(entitlement_response, dict) and 'json_errors' in entitlement_response:
		if 'ENT_PINInvalid' in entitlement_response['json_errors']:
			return get_entitlement_data(video_id=video_id,
			                            stream_type=stream_type,
			                            pin_required=True,
			                            invalid_pin=True,
			                            force_refresh_token=('INVALID_JWT' in entitlement_response['json_errors']))
		elif 'ENT_PINRequired' in entitlement_response['json_errors']:
			return get_entitlement_data(video_id=video_id,
			                            stream_type=stream_type,
			                            pin_required=True,
			                            force_refresh_token=('INVALID_JWT' in entitlement_response['json_errors']))
		elif 'INVALID_JWT' in entitlement_response['json_errors']:
			return get_entitlement_data(video_id=video_id,
			                            stream_type=stream_type,
			                            pin_required=pin_required,
			                            invalid_pin=invalid_pin,
			                            force_refresh_token=True)

	return entitlement_response


def get_video_data(video_id, stream_type, season_id=None, movie_id=None, compilation_id=None, path=None):

	video_data = dict()
	entitlement_data = get_entitlement_data(video_id, stream_type)

	if entitlement_data.get('entitlement_token', None) is not None:
		from ..request_helper import base64_encode_urlsafe, get_json_response

		video_url = compat._format('{}/{}/{}/playlist',
								   lib_joyn().config['playbackApiBaseUrl'],
								   'channel' if stream_type == 'LIVE' else 'asset', video_id)

		video_data_payload = dumps(dict(
				manufacturer='unknown',
				platform='browser',
				maxSecurityLevel=1,
				model='unknown',
				protectionSystem='widevine',
				streamingFormat='dash',
		        enableSubtitles=True,
				maxResolution=1080,
				version='v1',
		)).replace(' ', '')

		xbmc_helper().log_debug('get_video_data: video url: {} - video payload {}', video_url, video_data_payload)

		video_data_headers = [('Authorization', compat._format('Bearer {}', entitlement_data['entitlement_token'])),
								('Content-Type', 'application/json')]

		xbmc_helper().log_debug('force_playready: {}, is_android: {}',
		                        xbmc_helper().get_bool_setting('force_playready'),
		                        lib_joyn().config.get('IS_ANDROID', False))

		if xbmc_helper().get_bool_setting('force_playready') is True and lib_joyn().config.get('IS_ANDROID', False) is True:
			video_data_headers.append(('User-Agent', CONST['EDGE_UA']))

		video_data_params = dict(signature=build_signature(video_data_payload, entitlement_data['entitlement_token']))

		video_data = get_json_response(url=video_url,
		                               config=lib_joyn().config,
		                               params=video_data_params,
		                               headers=video_data_headers,
		                               post_data=video_data_payload,
		                               no_cache=True,
		                               silent=True)

		video_data.update(dict(drm='widevine', streamingFormat='dash'))

		if isinstance(video_data, dict) and video_data.get('streamingFormat', '') == 'dash' and video_data.get('manifestUrl', None) is not None:
			mpdparser = get_mpd_parser(url=video_data.get('manifestUrl'), stream_type=stream_type, video_id=video_id)
			if mpdparser is not None:
				video_data.update({'parser': mpdparser})

			if season_id is not None:
				video_data.update({'season_id': season_id})
			if movie_id is not None:
				video_data.update({'movie_id': movie_id})
			if compilation_id is not None:
				video_data.update({'compilation_id': compilation_id})
			if path is not None:
				video_data.update({'path': path})

	return video_data


def get_video_client_data(asset_id, stream_type, asset_data={}):

	client_data = {
	        'genre': [],
	        'startTime': 0,
	        'videoId': None,
	        'npa': False
	}

	if stream_type == 'VOD':
		client_data.update({'videoId': asset_id})
	elif stream_type == 'LIVE':
		client_data.update({'channelId': asset_id})

	if 'video' in asset_data.keys() and 'duration' in asset_data['video'].keys():
		client_data.update({'duration': (asset_data['video']['duration'] * 1000)})

	if 'genres' in asset_data.keys():
		for genre in asset_data['genres']:
			if 'name' in genre.keys():
				client_data['genre'].append(genre['name'])

	if 'series' in asset_data.keys() and 'id' in asset_data['series'].keys():
		client_data.update({'tvShowId': asset_data['series']['id']})

	if 'tracking' in asset_data.keys():
		if 'agofCode' in asset_data['tracking'].keys():
			client_data.update({'agofCode': asset_data['tracking']['agofCode']})
		if 'brand' in asset_data['tracking'].keys():
			client_data.update({'brand': asset_data['tracking']['brand']})

	if client_data.get('brand', None) is None:
		client_data.update({'brand': ''})

	return client_data
