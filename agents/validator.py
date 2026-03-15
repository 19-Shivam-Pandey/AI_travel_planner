from langchain.agents import create_agent
from model import get_llm
from tools import get_weather, web_search

validator_agent = create_agent(
    model=get_llm(),
    tools=[get_weather, web_search],
    system_prompt="""
You are a travel plan validator.

Your job:
- verify realism
- check weather fit
- check if plan matches budget and constraints
- suggest corrections if something looks impractical
"""
)