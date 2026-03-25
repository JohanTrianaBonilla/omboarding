import json

from openai import OpenAI

from .logic import calculate_score, get_candidate_profile, search_similar_profiles
from .tools import TOOLS

client = OpenAI()


def ask_llm(prompt: str):
    response = client.chat.completions.create(
        model="gpt-4.1",
        messages=[{"role": "user", "content": prompt}],
        tools=TOOLS,
        tool_choice="auto",
    )

    msg = response.choices[0].message

    if msg.tool_calls:
        tool_call = msg.tool_calls[0]
        name = tool_call.function.name
        args = json.loads(tool_call.function.arguments or "{}")

        if name == "get_candidate_profile":
            return get_candidate_profile(**args)
        if name == "search_similar_profiles":
            return search_similar_profiles(**args)
        if name == "calculate_score":
            return calculate_score(**args)

    return {"response": msg.content}
