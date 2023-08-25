class PostgresConfig:
    pg_db = "bunker_db"
    pg_user = "bunker"
    pg_password = "bunker"
    pg_host = "127.0.0.1"
    pg_port = "5433"
    db_url = f"postgresql+psycopg2://{pg_user}:{pg_password}@{pg_host}:{pg_port}/{pg_db}"
