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

    print(query_duckdb("desc table movies;"))

