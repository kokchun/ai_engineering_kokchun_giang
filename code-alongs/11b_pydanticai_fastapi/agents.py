from pydantic_ai import Agent
from dotenv import load_dotenv
from data_models import Movie

load_dotenv()

agent = Agent(
    model="google-gla:gemini-2.5-flash",
    system_prompt="""You are a movie expert, based
              on a prompt, you should find the closest 
              matching movie
            """,
    output_type=Movie,
)
