DATABASE_TYPE_CLASS_MAPPING = {
    "file": "Csv",
    "sqlite": "Sqlite",
    "postgres": "Postgres",
    "api_eneco": "Api",
    "azure_eneco": "Azure",
}

CONFIG = {
    "local": {
        "file": {"file_path": "data"},
        "sqlite": {"data_path": "data/data.db"},
        "api_eneco": {"host": "http://code001.ecsbdp.com"},
        "azure_eneco": {
            "account": "sacodeassessment",
            "signature": "sv=2022-11-02&ss=b&srt=o&sp=wc&se=2034-11-11T11:00:00Z&st=2024-11-10T23:00:00Z&spr=https&sig=D%2BgRbWPJDTmsbPtyfTEiTnb7gg594uNsvm62oQK49Yg%3D",
            "container": "results",
            "path": "ingest-assessment-2026-03-17-MV",
        },
        "postgres": {
            "host": "code001.ecsbdp.com",
            "port": "5432",
            "dbname": "chinook",
            "user": "larry",
            "password": "iddqd",
        },
    }
}
