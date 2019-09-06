
main_table_schema = [
    {
        "name": "clientId",
        "type": "STRING"
    },
    {
        "name": "type",
        "type": "STRING"
    },
    {
        "name": "version",
        "type": "STRING"
    },
    {
        "name": "tid",
        "type": "STRING"
    },
    {
        "name": "userId",
        "type": "STRING"
    },
    {
        "name": "referer",
        "type": "STRING"
    },
    {
        "name": "ip",
        "type": "STRING"
    },
    {
        "name": "timestamp",
        "type": "INTEGER"
    },
    {
        "name": "device",
        "type": "RECORD",
        "fields": [
            {
                "name": "screenResolution",
                "type": "STRING"
            },
            {
                "name": "viewPort",
                "type": "STRING"
            },
            {
                "name": "encoding",
                "type": "STRING"
            },
            {
                "name": "screenColors",
                "type": "STRING"
            },
            {
                "name": "language",
                "type": "STRING"
            },
            {
                "name": "javaEnabled",
                "type": "BOOLEAN"
            },
            {
                "name": "flashVersion",
                "type": "STRING"
            },
            {
                "name": "userAgent",
                "type": "STRING"
            }
        ]
    },
    {
        "name": "page",
        "type": "RECORD",
        "fields": [
            {
                "name": "location",
                "type": "STRING"
            },
            {
                "name": "title",
                "type": "STRING"
            },
            {
                "name": "pagePath",
                "type": "STRING"
            },
            {
                "name": "hostname",
                "type": "STRING"
            }
        ]
    },
    {
        "name": "trafficSource",
        "type": "RECORD",
        "fields": [
            {
                "name": "referralPath",
                "type": "STRING"
            },
            {
                "name": "campaign",
                "type": "STRING"
            },
            {
                "name": "source",
                "type": "STRING"
            },
            {
                "name": "medium",
                "type": "STRING"
            },
            {
                "name": "term",
                "type": "STRING"
            },
            {
                "name": "content",
                "type": "STRING"
            }
        ]
    },
    {
        "name": "eventInfo",
        "type": "RECORD",
        "fields": [
            {
                "name": "eventCategory",
                "type": "STRING"
            },
            {
                "name": "eventAction",
                "type": "STRING"
            },
            {
                "name": "eventLabel",
                "type": "STRING"
            },
            {
                "name": "eventValue",
                "type": "INTEGER"
            }
        ]
    },
    {
        "name": "customDimensions",
        "type": "RECORD",
        "mode": "REPEATED",
        "fields": [
            {
                "name": "index",
                "type": "INTEGER"
            },
            {
                "name": "value",
                "type": "STRING"
            }
        ]
    },
    {
        "name": "customMetrics",
        "type": "RECORD",
        "mode": "REPEATED",
        "fields": [
            {
                "name": "index",
                "type": "INTEGER"
            },
            {
                "name": "value",
                "type": "STRING"
            }
        ]
    }
]

#network,geoname_id,registered_country_geoname_id,represented_country_geoname_id,is_anonymous_proxy,is_satellite_provider
ip_table_schema = [
    {
        "name": "network",
        "type": "STRING"
    },
    {
        "name": "geoname_id",
        "type": "INTEGER"
    },
    {
        "name": "registered_country_geoname_id",
        "type": "INTEGER"
    },
    {
        "name": "represented_country_geoname_id",
        "type": "INTEGER"
    },
    {
        "name": "represented_country_geoname_id",
        "type": "INTEGER"
    },
    {
        "name": "is_anonymous_proxy",
        "type": "INTEGER"
    },
    {
        "name": "is_satellite_provider",
        "type": "INTEGER"
    }
]

#geoname_id,locale_code,continent_code,continent_name,country_iso_code,country_name,is_in_european_union
country_table_schema = [
    {
        "name": "geoname_id",
        "type": "INTEGER"
    },
    {
        "name": "locale_code",
        "type": "STRING"
    },
    {
        "name": "continent_code",
        "type": "STRING"
    },
    {
        "name": "continent_name",
        "type": "STRING"
    },
    {
        "name": "country_iso_code",
        "type": "STRING"
    },
    {
        "name": "country_name",
        "type": "STRING"
    },
    {
        "name": "is_in_european_union",
        "type": "INTEGER"
    }
]