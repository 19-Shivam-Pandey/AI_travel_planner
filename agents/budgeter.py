from langchain.agents import create_agent
from model import get_llm
from tools import web_search, estimate_budget

budget_agent = create_agent(
    model=get_llm(),
    tools=[web_search, estimate_budget],
    system_prompt="""
You are a travel budget specialist.

Your job:
- estimate trip cost realistically
- use tools for calculations
- infer rough hotel/food/transport assumptions from context when needed
- say clearly if the plan exceeds budget
"""
)