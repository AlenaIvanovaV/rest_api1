from voluptuous import PREVENT_EXTRA, Schema

user = Schema(
    {
        "page": int,
        "per_page": int,
        "total": int,
        "total_pages": int,
        "data": [
            {
                "id": int,
                "name": str,
                "year": int,
                "color": str,
                "pantone_value": str
            }

        ],
        "support": {
            "url": str,
            "text": str
        }
    },
    extra=PREVENT_EXTRA,
    required=True
)

user_unsuccessful = Schema({
    "error": "Missing password"
},
    extra=PREVENT_EXTRA,
    required=True
)
