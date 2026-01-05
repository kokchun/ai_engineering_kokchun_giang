from utils import query_duckdb

if __name__ == "__main__":
    query_duckdb("""
        CREATE TABLE IF NOT EXISTS movies (
                title TEXT,
                year INTEGER,
                genre TEXT,
                rating TINYINT
        );
    """)

    # query_duckdb("INSERT INTO movies VALUES ('Titanic', 1997, 'romance', 5)")

    print(query_duckdb("desc table movies;"))

