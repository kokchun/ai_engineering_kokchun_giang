from constants import VECTOR_DB_PATH, DATA_PATH
import lancedb
from lancedb.pydantic import LanceModel, Vector
from pydantic import Field
from lancedb.embeddings import get_registry

embedding_model = get_registry().get("gemini-text").create(name="gemini-embedding-001")

# schema for a LanceTable
class Article(LanceModel):
    doc_id: str 
    filepath: str 
    content: str = embedding_model.SourceField()
    embedding: Vector(3072) = embedding_model.VectorField()