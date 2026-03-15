from langchain.agents import create_agent
from model import get_llm
from tools import web_search, get_weather, geocode_city

planner_agent = create_agent(
    model=get_llm(),
    tools=[web_search, get_weather, geocode_city],
    system_prompt="""
You are a travel itinerary planner.

Your job:
- create a realistic day-by-day plan
- use live tools when needed
- consider weather, city context, and user constraints
- avoid overpacked schedules
- group activities logically

Always output a clean itinerary.
"""
)