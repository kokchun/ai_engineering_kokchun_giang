from constants import VECTOR_DB_PATH, DATA_PATH
import lancedb
from lancedb.pydantic import LanceModel, Vector
from lancedb.embeddings import get_registry
from lancedb.table import LanceTable
import time
from dotenv import load_dotenv 

load_dotenv()

embedding_model = get_registry().get("gemini-text").create(name="gemini-embedding-001")

# schema for a LanceTable
class Article(LanceModel):
    doc_id: str 
    filepath: str 
    content: str = embedding_model.SourceField()
    embedding: Vector(3072) = embedding_model.VectorField()

def setup_vector_db(path):
    # Path(path).mkdir(exist_ok=True)
    vector_db = lancedb.connect(path)
    vector_db.create_table("articles", schema=Article, exist_ok=True)

    return vector_db

def ingest_docs_to_vector_db(table: LanceTable):
    for filepath in DATA_PATH.glob("*.txt"):
        with open(filepath, "r") as file:
            content = file.read()

        doc_id = filepath.stem # or some hash/number
        table.delete(f"doc_id = '{doc_id}") # make idempotent

        table.add([{
            "doc_id": doc_id,
            "filepath": filepath,
            "content": content
        }])

        print(table.to_pandas()["filename"])

        time.sleep(30)

if __name__ == "__main__":
    vector_db = setup_vector_db(VECTOR_DB_PATH)
    ingest_docs_to_vector_db(vector_db["articles"])