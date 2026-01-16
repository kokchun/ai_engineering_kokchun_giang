from pydantic_ai import Agent
from data_models import RagResponse

rag_agent = Agent(
    model="google-gla:gemini-2.5-flash",
    retries=2,
    system_prompt=(
        "You are an expert in rabbit races and knows how to distinguish between the rabbits",
        "Always answer based on the retrieved knowledge, but you can mix in your expertise to make the answer more coherent",
        "Don't hallucinate, rather say you can't answer it if the user prompts outside of the retrieved knowledge",
        "Make sure to keep the answer clear and concise, getting to the point directly, max 4 sentences",
        "Also describe which file you have used as source",
    ),
    output_type=RagResponse,
)

# create tool for rag_agent to use
@rag_agent.tool_plain
def retrieve_top_document(query: str, k=3) -> str:
    """
    uses vector search to find the closest k matching documents to query
    """

    # logic to connect to knowledge base
    # retrieve most relevant document
    # pick out relevant info and construct a context for LLM to use