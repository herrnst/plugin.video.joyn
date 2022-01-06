# -*- coding: utf-8 -*-

CONST = {
        'BASE_URL': 'https://www.joyn.de',
        'ENTITLEMENT_URL': 'entitlement-token',
        'IP_API_URL': 'http://ip-api.com/json?lang={:s}&fields=status,country,countryCode',
        'AUTH_URL': 'https://auth.joyn.de/auth',
        'AUTH_ANON': '/anonymous',
        'AUTH_REFRESH': '/refresh',
        'AUTH_LOGIN': '/login',
        'AUTH_LOGOUT': '/logout',
        'SSO_AUTH_URL': 'https://auth.joyn.de/sso/endpoints',
        'OAUTH_URL': 'https://www.joyn.de/oauth',
        'CLIENT_NAMES': ['web', 'ios', 'android'],
        'EDGE_UA': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36',
        'JOYN_CLIENT_VERSION': '2.3.5',
        'MAX_VIDEO_TRIES': 5,
        'MPD_FILTER': '%28type%3D%3D%22video%22%29%7C%7C%28true%29',
        'SIGNATURE_KEY': 'MzU0MzM3MzgzMzM4MzMzNjM1NDMzNzM4MzYzNDM2MzYzNTQzMz'\
                         'czODM2MzYzMzM4MzIzNjM1NDMzNzM4MzMzMDM2MzQzNTM5MzU0'\
                         'MzM3MzgzMzM5MzMzNTMyMzQzNTQzMzczODM2MzUzMzM5MzU0Mz'\
                         'M3MzgzMzM4MzMzMjMzNDYzNTQzMzczODM2MzYzMzMzMzM0NDMz'\
                         'NDIzNTQzMzczODMzMzgzNjM2MzMzNQ==',

        'PRELOAD_JS_CONFIGS': {
            'API_GW_API_KEY': '"x-api-key":"(.*?)"}',
        },
        'CHUNKS_JS_CONFIGS': {
            'PLAYERCONFIG_URL': 'https://playerconfig.*?.json',
        },
        'COUNTRIES': {
            'DE': {
                'language': 'de',
                'setting_id': '1',
            },
        },

        'CACHE_DIR': 'cache',
        'TEMP_DIR': 'tmp',
        'DATA_DIR': 'data',
        'CACHE': {
            'CONFIG': { 'key': 'config', 'expires': 432000 },
            'EPG': { 'key': 'epg', 'expires': 36000 },
            'ETAGS': { 'key': 'etags', 'expires': None},
            'ACCOUNT_INFO': { 'key': 'account_info', 'expires': 36000}
        },

        'CACHE_FILES_KEEP': ['config.json'],

        'ETAGS_TTL': 1209600,  # 14 days

        'LASTSEEN_ITEM_COUNT': 20,
        'UEPG_REFRESH_INTERVAL': 7200,
        'UEPG_ROWCOUNT': 5,
        'INPUTSTREAM_ADDON': 'inputstream.adaptive',

        'MSG_IDS': {
            'ADD_TO_WATCHLIST': 30651,
            'ADD_TO_WATCHLIST_PRX': 30653,
            'REMOVE_FROM_WATCHLIST': 30652,
            'REMOVE_FROM_WATCHLIST_PRFX': 30654,
            'MEDIA_LIBRARY': 30622,
            'CATEGORY': 30623,
            'TV_SHOW': 30624,
            'SEASON': 30625,
            'EPISODE': 30625,
            'WATCHLIST': 30601,
            'MEDIA_LIBRARIES': 30602,
            'CATEGORIES': 30603,
            'SEARCH': 30604,
            'LIVE_TV': 30605,
            'TV_GUIDE': 30606,
            'MEDIA_LIBRARIES_PLOT': 30608,
            'CATEGORIES_PLOT': 30609,
            'WATCHLIST_PLOT': 30607,
            'SEARCH_PLOT': 30610,
            'LIVE_TV_PLOT': 30611,
            'TV_GUIDE_PLOT': 30612,
            'WL_TYPE_ADDED': 30526,
            'WL_TYPE_REMOVED': 30527,
            'MSG_INPUSTREAM_NOT_ENABLED': 30501,
            'MSG_WIDEVINE_NOT_FOUND': 30502,
            'MSG_NO_SEARCH_RESULTS': 30525,
            'MSG_NO_FAVS_YET': 30528,
            'MSG_FAVS_UNAVAILABLE': 30529,
            'ERROR': 30521,
            'MSG_ERR_TRY_AGAIN': 30522,
            'MSG_ERROR_CONFIG_DECRYPTION': 30523,
            'MSG_ERROR_NO_VIDEOSTEAM': 30524,
            'LIVETV_TITLE': 30655,
            'LIVETV_UNTIL': 30656,
            'LIVETV_UNTIL_AND_NEXT': 30657,
            'MIN_AGE': 30658,
            'VIDEO_AVAILABLE': 30650,
            'SEASON_NO': 30621,
            'MSG_CONFIG_VALUES_INCOMPLETE': 30530,
            'MSG_NO_ACCESS_TO_URL': 30531,
            'MSG_COUNTRY_NOT_DETECTED': 30532,
            'MSG_COUNTRY_INVALID': 30533,
            'CANCEL': 30503,
            'OPEN_ADDON_SETTINGS': 30504,
            'CACHE_WAS_CLEARED': 30659,
            'CACHE_COULD_NOT_BE_CLEARED': 30660,
            'LANG_CODE': 30661,
            'MSG_VIDEO_UNAVAILABLE': 30662,
            'MSG_GAPHQL_ERROR': 30663,
            'MSG_NO_CONTENT': 30664,
            'CONTINUE_WATCHING': 30665,
            'RECOMMENDATION': 30666,
            'MOVIE': 30667,
            'SERIES': 30668,
            'TITLE_LABEL': 30669,
            'LOGGED_IN_LABEL': 30670,
            'LOGIN_FAILED_LABEL': 30671,
            'ACCOUNT_INFO_LABEL': 30672,
            'YES_LABEL': 30673,
            'NO_LABEL': 30674,
            'USERNAME_LABEL': 30675,
            'PASSWORD_LABEL': 30676,
            'MSG_INVALID_EMAIL': 30677,
            'LOGOUT_OK_LABEL': 30678,
            'NOT_LOGGED_IN_LABEL': 30679,
            'LOGOUT_NOK_LABEL': 30680,
            'RETRY': 30505,
            'ACCOUNT': 30352,
            'MSG_RERESH_AUTH_FAILED_RELOG': 30534,
            'MSG_RERESH_AUTH_FAILED': 30535,
            'CONTINUE_ANONYMOUS': 30506,
            'JOYN_BOOKMARKS': 30681,
            'JOYN_BOOKMARK_LABEL': 30682,
            'MSG_JOYN_BOOKMARK_ADD_SUCC': 30683,
            'MSG_JOYN_BOOKMARK_ADD_FAIL': 30684,
            'MSG_JOYN_BOOKMARK_DEL_SUCC': 30685,
            'MSG_JOYN_BOOKMARK_DEL_FAIL': 30686,
            'ADD_TO_JOYN_BOOKMARKS_LABEL': 30687,
            'DEL_FROM_JOYN_BOOKMARKS_LABEL': 30688,
            'MPAA_PIN': 30689,
            'MSG_INVALID_MPAA_PIN': 30690,
            'PLUS_HIGHLIGHT_LABEL': 30691,
            'MSG_INVALID_PASSWORD': 30692,
            'NO_INFORMATION_AVAILABLE': 30693,
            'LOGIN_NOW_LABEL': 30694,
            'LOGIN_LABEL': 30136,
            'ASCENDING_LABEL': 30695,
            'DESCENDING_LABEL': 30696,
        },

        'VIEW_MODES': {
            'Standard': {
                'skin.estuary': '0',
            },
            'List': {
                'skin.estuary': '50',
            },
            'Poster': {
                'skin.estuary': '51',
            },
            'IconWall': {
                'skin.estuary': '52',
            },
            'Shift': {
                'skin.estuary': '53',
             },
            'InfoWall': {
                'skin.estuary': '54',
            },
            'WideList': {
                'skin.estuary': '55',
            },
            'Wall': {
                'skin.estuary': '500',
            },
            'Banner': {
                'skin.estuary': '501',
            },
            'Fanart': {
                'skin.estuary': '502',
            },
        },
        'LICENSE_FILTER': {
            'hasActivePlus': 'FREE',
        },
        'LICENSE_TYPES': {
            'FREE': {
                'AVOD': {
                    'MARKING_TYPES': ['JOYN_ORIGINAL', 'HD']
                }
            },
            'PAID': {
                'SVOD': {
                    'SUBSCRIPTION_TYPE': 'hasActivePlus',
                    'MARKING_TYPES': ['PREMIUM', 'HD', 'JOYN_ORIGINAL', 'PLUS'],
                },
            },
        },
        'FOLDERS': {
            'INDEX': {
                'content_type': 'tags',
                'view_mode': 'categories_view',
            },
             'CATEORIES': {
                'content_type': 'tags',
                'view_mode': 'categories_view',
                'cacheable': True,
            },
            'MEDIA_LIBS': {
                'content_type': 'tags',
                'view_mode': 'categories_view',
                'cacheable': True,
            },
            'WATCHLIST': {
                'content_type': 'videos',
                'view_mode': 'watchlist_view',
            },
            'CATEGORY': {
                'content_type': 'tvshows',
                'view_mode': 'category_view',
                'cacheable': True,
            },
            'LIVE_TV': {
                'content_type': 'videos',
                'view_mode': 'livetv_view',
            },
            'TV_SHOWS': {
                'content_type': 'tvshows',
                'view_mode': 'tvshow_view',
                'cacheable': True,
            },
            'SEASONS': {
                'content_type': 'seasons',
                'view_mode': 'season_view',
                'sort': {
                   'order_type': '7',  # SortByTitle
                   'setting_id': 'season_order',
                },
                'cacheable': True,
            },
            'EPISODES': {
                'content_type': 'episodes',
                'view_mode': 'episode_view',
                'sort': {
                   'order_type': '23',  # SortByEpisodeNumber
                   'setting_id': 'episode_order',
                },
                'cacheable': True,
            },
        },

        'SETTING_VALS': {
            'SORT_ORDER_DEFAULT': '0',
            'SORT_ORDER_ASC': '1',
            'SORT_ORDER_DESC': '2',
        },

        'GRAPHQL': {
            'API_URL': 'https://api.joyn.de/graphql',

            'REQUIRED_HEADERS': ['x-api-key', 'joyn-platform'],

            'STATIC_VARIABLES': {
                'first': 1000,
                'offset': 0,
            },

        'METADATA': {
            'TVCHANNEL': {
                'TEXTS': {'title': 'title'},
                'ART': {
                    'logo': {
                        'BRAND_LOGO': {
                            'icon': 'profile:nextgen-web-artlogo-183x75',
                            'thumb': 'profile:original',
                            'clearlogo': 'profile:nextgen-web-artlogo-183x75',
                        },
                    },
                },
            },

            'TVSHOW': {
                'TEXTS': {'title': 'title', 'description': 'plot'},
                'ART': {
                    'images': {
                        'PRIMARY': {
                            'thumb': 'profile:original'
                        },
                        'ART_LOGO': {
                            'icon': 'profile:nextgen-web-artlogo-183x75',
                            'clearlogo': 'profile:nextgen-web-artlogo-183x75',
                            'clearart': 'profile:nextgen-web-artlogo-183x75',
                        },
                        'HERO_LANDSCAPE': {
                            'fanart': 'profile:nextgen-web-herolandscape-1920x',
                            'landscape': 'profile:nextgen-web-herolandscape-1920x',
                        },
                        'HERO_PORTRAIT': {
                            'poster': 'profile:nextgen-webphone-heroportrait-563x',
                        },
                    },

                },
            },

           'EPISODE': {
               'TEXTS': {'title': 'title', 'description': 'plot'},
               'ART': {
                    'images': {
                        'PRIMARY': {
                            'thumb': 'profile:original'
                        },
                        'ART_LOGO': {
                            'icon': 'profile:nextgen-web-artlogo-183x75',
                            'clearlogo': 'profile:nextgen-web-artlogo-183x75',
                        },
                        'HERO_LANDSCAPE': {
                            'fanart': 'profile:nextgen-web-herolandscape-1920x',
                        },
                        'HERO_PORTRAIT': {
                            'poster': 'profile:nextgen-webphone-heroportrait-563x',
                        },
                    },
                },
            },

            'EPG': {
                'TEXTS': {'title': 'title', 'secondaryTitle': 'plot'},
                'ART': {
                    'images': {
                        'LIVE_STILL': {
                            'poster': 'profile:original',
                            'thumb': 'profile:original',
                        },
                    },
                },
            },
        },

        'GET_BONUS': {
            'QUERY': '($seriesId: ID!, $first: Int!, $offset: Int!) { series(id: $seriesId) { __typename id ageRating { __typename description minAge '\
                'ratingSystem } extras(first: $first, offset: $offset) { __typename id title video { __typename duration id } images { __typename id '\
                'copyright type url accentColor } tracking { __typename agofCode externalAssetId brand url } } } }',
            'OPERATION': 'getBonus',
            'REQUIRED_VARIABLES': ['seriesId', 'first', 'offset']
        },

        'GET_BRANDS': {
            'QUERY': '{ brands { __typename id livestream { __typename id agofCode title quality } logo { __typename accentColor url } hasVodContent title } }',
            'OPERATION': 'getBrands',
        },

        'LANDINGPAGE': {
            'QUERY': '($path: String!) { page(path: $path) { __typename ... on LandingPage { blocks { __typename id isPersonalized ... on StandardLane { '\
                'headline } ... on FeaturedLane { headline } ... on LiveLane { headline } ... on ResumeLane { headline } ... on ChannelLane { headline '\
                '} ... on BookmarkLane { headline } ... on RecoForYouLane { headline } } } } }',
            'OPERATION': 'LandingPage',
            'REQUIRED_VARIABLES': ['path'],
            'AUTH': True,
        },

       'SINGLEBLOCK': {
            'QUERY': '($blockId: String!, $offset: Int!, $first: Int!) { block(id: $blockId) { __typename id assets(offset: $offset, first: $first) { '\
                '__typename ...MovieCoverFragment ...SeriesCoverFragment ...BrandCoverFragment ...EpisodeCoverFragment ...EpgFragment '\
                '...CompilationCoverFragment } } } fragment MovieCoverFragment on Movie { __typename id title description ageRating { description label '\
                'minAge ratingSystem } copyright copyrights endsAt genres { id name title type } images { __typename type url } isBookmarked languages '\
                '{ code title } licenseTypes markings productionCompanies productionCountries productionYear resumePosition { position } tagline '\
                'tracking { adfree agofCode brand duration externalAssetId genres parentAssetId primaryAirdateBrand promamsId trackingId url '\
                'visibilityStart webExclusive } video { __typename id licenses { deviceRestrictions { deviceClasses maximumResolution } endDate '\
                'geoRestrictions protectionLevel publishingChannels source startDate type } duration markers { end source start type } } } fragment '\
                'SeriesCoverFragment on Series { __typename id title isBookmarked description ageRating { description label minAge ratingSystem } '\
                'copyright copyrights markings images { url type __typename } licenseTypes genres { id name title type } isBingeable numberOfSeasons '\
                'productionCompanies productionCountries productionYear subtype tagline languages { code title } } fragment BrandCoverFragment on Brand '\
                '{ __typename id title path logo { __typename type accentColor url } livestream { __typename id quality } } fragment '\
                'EpisodeCoverFragment on Episode { __typename id airdate ageRating { description label minAge ratingSystem } description endsAt genres '\
                '{ id name title type } images { __typename type url } licenseTypes markings number resumePosition { position } title tracking { adfree '\
                'agofCode brand duration externalAssetId genres parentAssetId primaryAirdateBrand promamsId trackingId url visibilityStart webExclusive '\
                '} video { __typename id licenses { deviceRestrictions { deviceClasses maximumResolution } endDate geoRestrictions protectionLevel '\
                'publishingChannels source startDate type } duration markers { end source start type } } season { __typename id number numberOfEpisodes '\
                'title } series { __typename id title isBookmarked description ageRating { description label minAge ratingSystem } copyright copyrights '\
                'markings images { url type __typename } licenseTypes genres { id name title type } isBingeable numberOfSeasons productionCompanies '\
                'productionCountries productionYear subtype tagline languages { code title } } } fragment EpgFragment on EpgEntry { __typename id '\
                'startDate endDate images { __typename type url accentColor } title secondaryTitle livestream { __typename id brand { __typename id '\
                'logo { __typename url accentColor } title } } } fragment CompilationCoverFragment on Compilation { __typename id title isBookmarked '\
                'description ageRating { description label minAge ratingSystem } copyright copyrights licenseTypes markings images { url type '\
                '__typename } genres { id name title type } numberOfItems languages { code title } }',
            'OPERATION': 'SingleBlockQuery',
            'REQUIRED_VARIABLES': ['blockId', 'offset', 'first'],
            'AUTH': True,
            'BOOKMARKS': True,
        },

        'CHANNEL': {
            'QUERY': '($path: String!, $offset: Int!, $first: Int!) { page(path: $path) { __typename ... on ChannelPage { assets(offset: $offset, first: '\
                '$first) { __typename ...MovieCoverFragment ...SeriesCoverFragment ...EpisodeCoverFragment ...CompilationCoverFragment } } } } fragment '\
                'MovieCoverFragment on Movie { __typename id title description ageRating { description label minAge ratingSystem } copyright copyrights '\
                'endsAt genres { id name title type } images { __typename type url } isBookmarked languages { code title } licenseTypes markings '\
                'productionCompanies productionCountries productionYear resumePosition { position } tagline tracking { adfree agofCode brand duration '\
                'externalAssetId genres parentAssetId primaryAirdateBrand promamsId trackingId url visibilityStart webExclusive } video { __typename id '\
                'licenses { deviceRestrictions { deviceClasses maximumResolution } endDate geoRestrictions protectionLevel publishingChannels source '\
                'startDate type } duration markers { end source start type } } } fragment SeriesCoverFragment on Series { __typename id title '\
                'isBookmarked description ageRating { description label minAge ratingSystem } copyright copyrights markings images { url type '\
                '__typename } licenseTypes genres { id name title type } isBingeable numberOfSeasons productionCompanies productionCountries '\
                'productionYear subtype tagline languages { code title } } fragment EpisodeCoverFragment on Episode { __typename id airdate ageRating { '\
                'description label minAge ratingSystem } description endsAt genres { id name title type } images { __typename type url } licenseTypes '\
                'markings number resumePosition { position } title tracking { adfree agofCode brand duration externalAssetId genres parentAssetId '\
                'primaryAirdateBrand promamsId trackingId url visibilityStart webExclusive } video { __typename id licenses { deviceRestrictions { '\
                'deviceClasses maximumResolution } endDate geoRestrictions protectionLevel publishingChannels source startDate type } duration markers '\
                '{ end source start type } } season { __typename id number numberOfEpisodes title } series { __typename id title isBookmarked '\
                'description ageRating { description label minAge ratingSystem } copyright copyrights markings images { url type __typename } '\
                'licenseTypes genres { id name title type } isBingeable numberOfSeasons productionCompanies productionCountries productionYear subtype '\
                'tagline languages { code title } } } fragment CompilationCoverFragment on Compilation { __typename id title isBookmarked description '\
                'ageRating { description label minAge ratingSystem } copyright copyrights licenseTypes markings images { url type __typename } genres { '\
                'id name title type } numberOfItems languages { code title } }',
            'OPERATTON': 'ChannelPageQuery',
            'REQUIRED_VARIABLES': ['path', 'offset', 'first'],
            'AUTH': True,
            'BOOKMARKS': True,
        },

        'SEASONS': {
            'QUERY': '($seriesId: ID!, $seasonLicenseFilter: LicenseFilter!) { series(id: $seriesId) { __typename id title isBookmarked description '\
                'ageRating { description label minAge ratingSystem } copyright copyrights markings images { url type __typename } licenseTypes genres { '\
                'id name title type } isBingeable numberOfSeasons productionCompanies productionCountries productionYear subtype tagline languages { '\
                'code title } seasons (licenseFilter: $seasonLicenseFilter) { __typename id number numberOfEpisodes title  licenseTypes} } }',
            'OPERATION': 'getSeries',
            'REQUIRED_VARIABLES': ['seriesId', 'seasonLicenseFilter'],
            'BOOKMARKS': True,
            'AUTH': True,
            'FILTER_LICENSE_TYPES': False,
        },

        'SEASONS_NOLICENSEFILTER': {
            'QUERY': '($seriesId: ID!) { series(id: $seriesId) { __typename id title isBookmarked description '\
                'ageRating { description label minAge ratingSystem } copyright copyrights markings images { url type __typename } licenseTypes genres { '\
                'id name title type } isBingeable numberOfSeasons productionCompanies productionCountries productionYear subtype tagline languages { '\
                'code title } seasons { __typename id number numberOfEpisodes title licenseTypes } } }',
           'OPERATION': 'getSeries',
           'REQUIRED_VARIABLES': ['seriesId'],
           'BOOKMARKS': True,
           'AUTH': True,
           'FILTER_LICENSE_TYPES': False,
        },

        'EPISODES': {
            'QUERY': '($seasonId: ID!, $first: Int!, $offset: Int!, $episodeLicenseFilter: LicenseFilter!) { season(id: $seasonId) { __typename id number '\
                'title episodes(first: $first, offset: $offset, licenseFilter: $episodeLicenseFilter) { __typename id airdate ageRating { description '\
                'label minAge ratingSystem } description endsAt genres { id name title type } images { __typename type url } licenseTypes markings '\
                'number resumePosition { position } title tracking { adfree agofCode brand duration externalAssetId genres parentAssetId '\
                'primaryAirdateBrand promamsId trackingId url visibilityStart webExclusive } video { __typename id licenses { deviceRestrictions { '\
                'deviceClasses maximumResolution } endDate geoRestrictions protectionLevel publishingChannels source startDate type } duration markers '\
                '{ end source start type } } season { __typename id number numberOfEpisodes title } series { __typename id title isBookmarked '\
                'description ageRating { description label minAge ratingSystem } copyright copyrights markings images { url type __typename } '\
                'licenseTypes genres { id name title type } isBingeable numberOfSeasons productionCompanies productionCountries productionYear subtype '\
                'tagline languages { code title } } } } }',
            'OPERATION': 'getSeason',
            'REQUIRED_VARIABLES': ['seasonId', 'first', 'offset', 'episodeLicenseFilter'],
            'AUTH': True,
            'BOOKMARKS': True,
            'FILTER_LICENSE_TYPES': False,
        },

        'EPISODES_NOLICENSEFILTER': {
            'QUERY': '($seasonId: ID!, $first: Int!, $offset: Int!) { season(id: $seasonId) { __typename id number '\
                'title episodes(first: $first, offset: $offset) { __typename id airdate ageRating { description '\
                'label minAge ratingSystem } description endsAt genres { id name title type } images { __typename type url } licenseTypes markings '\
                'number resumePosition { position } title tracking { adfree agofCode brand duration externalAssetId genres parentAssetId '\
                'primaryAirdateBrand promamsId trackingId url visibilityStart webExclusive } video { __typename id licenses { deviceRestrictions { '\
                'deviceClasses maximumResolution } endDate geoRestrictions protectionLevel publishingChannels source startDate type } duration markers '\
                '{ end source start type } } season { __typename id number numberOfEpisodes title } series { __typename id title isBookmarked '\
                'description ageRating { description label minAge ratingSystem } copyright copyrights markings images { url type __typename } '\
                'licenseTypes genres { id name title type } isBingeable numberOfSeasons productionCompanies productionCountries productionYear subtype '\
                'tagline languages { code title } } } } }',
            'OPERATION': 'getSeason',
            'REQUIRED_VARIABLES': ['seasonId', 'first', 'offset'],
            'AUTH': True,
            'BOOKMARKS': True,
            'FILTER_LICENSE_TYPES': False,
        },

        'COMPILATION_ITEMS': {
            'QUERY': '($id: ID!, $offset: Int!, $first: Int!) { compilation(id: $id) { __typename compilationItems(first: $first, offset: $offset) { '\
                '__typename ... on CompilationItem { ...CompilationItemCoverFragment } } } } fragment CompilationItemCoverFragment on CompilationItem { '\
                '__typename id ageRating { description label minAge ratingSystem } description endsAt genres { id name title type } images { __typename '\
                'type url } markings licenseTypes resumePosition { position } title tracking { adfree agofCode brand duration externalAssetId genres '\
                'parentAssetId primaryAirdateBrand promamsId trackingId url visibilityStart webExclusive } video { __typename id licenses { '\
                'deviceRestrictions { deviceClasses maximumResolution } endDate geoRestrictions protectionLevel publishingChannels source startDate '\
                'type } duration markers { end source start type } } compilation { id images { __typename type url } ageRating { description label '\
                'minAge ratingSystem } copyright } }',
            'OPERATION': 'GetCompilationItemsQuery',
            'REQUIRED_VARIABLES': ['id', 'first', 'offset'],
            'BOOKMARKS': True,
            'AUTH': True,
        },

        'COMPILATION': {
            'QUERY': '($id: ID!) { compilation(id: $id) { __typename id description images { __typename id type url } genres { __typename name type } title '\
                'ageRating { __typename description minAge ratingSystem } copyrights numberOfItems licenseTypes markings isBookmarked } }',
            'OPERATION': 'GetCompilationDetailsQuery',
            'REQUIRED_VARIABLES': ['id'],
            'BOOKMARKS': True,
            'AUTH': True,
        },

        'SERIES': {
            'QUERY': '($id: ID!) { series(id: $id) { __typename id title isBookmarked description ageRating { description label minAge ratingSystem } '\
                'copyright copyrights markings images { url type __typename } licenseTypes genres { id name title type } isBingeable numberOfSeasons '\
                'productionCompanies productionCountries productionYear subtype tagline languages { code title } }}',
            'REQUIRED_VARIABLES': ['id'],
            'BOOKMARKS': True,
            'AUTH': True,
        },

        'BRAND': {
            'QUERY': '($id: Int!) { brand(brandId: $id) { __typename id title hasVodContent livestream { __typename id agofCode title quality } markings logo '\
                '{ url type __typename } path } }',
            'REQUIRED_VARIABLES': ['id'],
        },

        'EPG': {
            'QUERY': '($first: Int!) { brands { __typename id livestream { __typename id title quality epg(first: $first) { __typename id startDate endDate '\
                'title secondaryTitle images { __typename id  type url } } } logo { __typename  url } hasVodContent title } }',
            'OPERATION': 'getEpg',
            'REQUIRED_VARIABLES': ['first'],
            'NO_CACHE': True,
        },

        'SEARCH': {
            'QUERY': '($text: String!) { search(term: $text, first: 50) { __typename results { __typename ...BrandCoverFragment ...SeriesCoverFragment '\
                '...MovieCoverFragment ...CompilationCoverFragment } } } fragment BrandCoverFragment on Brand { __typename id title path logo { '\
                '__typename type accentColor url } livestream { __typename id quality } } fragment SeriesCoverFragment on Series { __typename id title '\
                'isBookmarked description ageRating { description label minAge ratingSystem } copyright copyrights markings images { url type '\
                '__typename } licenseTypes genres { id name title type } isBingeable numberOfSeasons productionCompanies productionCountries '\
                'productionYear subtype tagline languages { code title } } fragment MovieCoverFragment on Movie { __typename id title description '\
                'ageRating { description label minAge ratingSystem } copyright copyrights endsAt genres { id name title type } images { __typename type '\
                'url } isBookmarked languages { code title } licenseTypes markings productionCompanies productionCountries productionYear '\
                'resumePosition { position } tagline tracking { adfree agofCode brand duration externalAssetId genres parentAssetId primaryAirdateBrand '\
                'promamsId trackingId url visibilityStart webExclusive } video { __typename id licenses { deviceRestrictions { deviceClasses '\
                'maximumResolution } endDate geoRestrictions protectionLevel publishingChannels source startDate type } duration markers { end source '\
                'start type } } } fragment CompilationCoverFragment on Compilation { __typename id title isBookmarked description ageRating { '\
                'description label minAge ratingSystem } copyright copyrights markings images { url type __typename } genres { id name title type } '\
                'numberOfItems languages { code title } }',
            'OPERATION': 'searchQuery',
            'REQUIRED_VARIABLES': ['text'],
            'AUTH': True,
            'NO_CACHE': True,
            'BOOKMARKS': True,
        },

        'ACCOUNT': {
            'QUERY': '{ me { account { id } profile { id email gender birthday avatar { color icon iconURL } } state subscriptions { productId type '\
                'provider { name } state { freeTrialUntil isActive } } subscriptionConfig { hasActivePlus hasActiveHD } } }',
            'OPERATION': 'GetAccountInfoQuery',
            'REQUIRED_VARIABLES': [],
            'AUTH': True,
            'NO_CACHE': True,
        },

        'USER_PROFILE': {
            'QUERY': '{ me { account { id email } profile { id email name gender birthday } state bookmarkedAssetIds subscriptions { id productId type '\
                '} subscriptionType subscriptionConfig { stripePublicAPIKey canUseDirectDebit freeTrialUntil hasActivePremium hasActivePlus hasActiveHD '\
                'renewsOn } } }',
            'AUTH': True,
            'NO_CACHE': True,
        },

        'ADD_BOOKMARK': {
            'QUERY': '($assetId: ID!) {setBookmark(assetId:$assetId) { __typename}}',
            'OPERATION': 'setBookmarkMutation',
            'REQUIRED_VARIABLES': ['assetId'],
            'AUTH': True,
            'IS_MUTATION': True,
            'NO_CACHE': True,
        },

        'DEL_BOOKMARK': {
            'QUERY': '($assetId: ID!) { removeBookmark(assetId:$assetId) }',
            'OPERATION': 'removeBookmarkMutation',
            'REQUIRED_VARIABLES': ['assetId'],
            'AUTH': True,
            'IS_MUTATION': True,
            'NO_CACHE': True,
        },

        'SET_RESUME_POSITION': {
            'QUERY': '($assetId: ID!, $position: Int!) { setResumePosition(assetId:$assetId, position:$position) { __typename '\
                'assetId position } }',
            'OPERATION': 'setResumeMutation',
            'AUTH': True,
            'IS_MUTATION': True,
            'NO_CACHE': True,
        },
    },

    'CATEGORY_LANES': ['RecoForYouLane', 'ResumeLane', 'FeaturedLane', 'StandardLane'],
}
