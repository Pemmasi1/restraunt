from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
import os

# Load API key from .env
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY is not set in .env file.")

# Set environment variable
os.environ["OPENAI_API_KEY"] = api_key

# Initialize LLM
llm = OpenAI(temperature=0.7)

# Prompt template
restaurant_prompt = PromptTemplate(
    input_variables=["cuisine"],
    template="""
I want to open a new restaurant that serves {cuisine} food.
- Suggest a fancy, catchy name for the restaurant.
- Suggest a list of 5 creative menu items with names, give a header "Menu" before the menu items.
"""
)

def generate_restaurant_idea(cuisine: str) -> str:
    prompt = restaurant_prompt.format(cuisine=cuisine)
    response = llm.invoke(prompt)
    return response
