from openai import OpenAI
from .tools import TOOLS
from .logic import (
    get_candidate_profile,
    search_similar_profiles,
    calculate_score
)

client = OpenAI()


def ask_llm(prompt: str):
    response = client.chat.completions.create(
        model="gpt-4.1",
        messages=[{"role": "user", "content": prompt}],
        tools=TOOLS,
        tool_choice="auto"
    )

    msg = response.choices[0].message

    # Si el modelo decide usar una tool
    if msg.tool_calls:
        tool_call = msg.tool_calls[0]
        name = tool_call["function"]["name"]
        args = tool_call["function"]["arguments"]

        if name == "get_candidate_profile":
            return get_candidate_profile(**args)
        elif name == "search_similar_profiles":
            return search_similar_profiles(**args)
        elif name == "calculate_score":
            return calculate_score(**args)

    # Si no usa tool
    return {"response": msg["content"]}
