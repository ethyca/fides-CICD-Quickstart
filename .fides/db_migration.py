import psycopg2

DB_HOST = "localhost"
DB_PORT = 5432
DB_USER = "postgres"
DB_PASSWORD = "postgres"
DB_NAME = "sample_db"


def execute_migration() -> None:
    with psycopg2.connect(
        dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT
    ) as connection:
        with open("database/migrations/postgres_sample.sql", "r") as f:
            sql_script = f.read()

        with connection.cursor() as cursor:
            cursor.execute(sql_script)
            connection.commit()


if __name__ == "__main__":
    execute_migration()
