import json
from model import get_llm
from state import TravelState

llm = get_llm()

SUPERVISOR_PROMPT = """
You are a supervisor for a dynamic travel-planning multi-agent system.

Your job is to decide what specialist should act next.

Available specialists:
- researcher
- planner
- budgeter
- validator
- finish

Decision rules:
- Choose researcher if destination info, local research, attractions, neighborhoods, food, or weather is still missing.
- Choose planner if enough research exists and itinerary is not yet prepared.
- Choose budgeter if itinerary exists but cost/budget fit is unclear.
- Choose validator if itinerary and budget both exist and need realism checking.
- Choose finish only if the final answer can already be given confidently.

Return ONLY valid JSON like:
{"next_agent": "researcher"}
"""

def supervisor_node(state: TravelState) -> TravelState:
    payload = {
        "user_query": state.get("user_query", ""),
        "destination": state.get("destination", ""),
        "days": state.get("days", 0),
        "budget": state.get("budget", 0),
        "interests": state.get("interests", []),
        "constraints": state.get("constraints", []),
        "research_notes": state.get("research_notes", ""),
        "itinerary": state.get("itinerary", ""),
        "budget_breakdown": state.get("budget_breakdown", ""),
        "validation_notes": state.get("validation_notes", ""),
    }

    msg = f"{SUPERVISOR_PROMPT}\n\nCurrent state:\n{json.dumps(payload, ensure_ascii=False, indent=2)}"
    response = llm.invoke(msg)
    text = response.content.strip() if isinstance(response.content, str) else str(response.content)

    try:
        data = json.loads(text)
        nxt = data.get("next_agent", "researcher")
    except Exception:
        nxt = "researcher"

    return {"next_agent": nxt}