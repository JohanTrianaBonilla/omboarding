TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "get_candidate_profile",
            "description": "Obtiene el perfil de un candidato por ID.",
            "parameters": {
                "type": "object",
                "properties": {
                    "candidate_id": {"type": "integer"},
                },
                "required": ["candidate_id"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "search_similar_profiles",
            "description": "Realiza búsqueda semántica usando Flask + Qdrant.",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {"type": "string"},
                },
                "required": ["query"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "calculate_score",
            "description": "Calcula compatibilidad entre habilidades del candidato y un cargo.",
            "parameters": {
                "type": "object",
                "properties": {
                    "candidate_text": {"type": "string"},
                    "job_description": {"type": "string"},
                },
                "required": ["candidate_text", "job_description"],
            },
        },
    }
]
