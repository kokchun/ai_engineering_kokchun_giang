# RAG

## Steps

1. Read in pdf data and export as txt 
2. Ingest the data into LanceDB (custom, but could be e.g. dlt-lance) -> knowledge base with embeddings
3. Create data models (pydantic models) for agent to get structured output
4. RAG agent with some prompt engineering and a tool to retrieve documents
5. Create a FastAPI API to serve the RAG model
6. Consume API with Streamlit frontend