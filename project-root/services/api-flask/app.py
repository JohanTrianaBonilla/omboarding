from flask import Flask, request, jsonify
from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance, PointStruct
from sentence_transformers import SentenceTransformer
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

# -----------------------------
# Inicializar Qdrant
# -----------------------------
#client = QdrantClient(host="localhost", port=6333)
QDRANT_HOST = os.getenv("QDRANT_HOST", "localhost")
QDRANT_PORT = int(os.getenv("QDRANT_PORT", 6333))

client = QdrantClient(host=QDRANT_HOST, port=QDRANT_PORT)


COLLECTION_NAME = "candidates"

# Crear colección si no existe
client.recreate_collection(
    collection_name=COLLECTION_NAME,
    vectors_config=VectorParams(size=384, distance=Distance.COSINE)
)

# -----------------------------
# Modelo de embeddings
# -----------------------------
#model = SentenceTransformer("all-MiniLM-L6-v2")
model_name = os.getenv("EMBED_MODEL", "all-MiniLM-L6-v2")
model = SentenceTransformer(model_name)

# -----------------------------
# Endpoint: generar embeddings
# -----------------------------
@app.post("/embed")
def embed():
    data = request.json

    candidate_id = data.get("candidate_id")
    text = data.get("text")

    if not candidate_id or not text:
        return jsonify({"error": "candidate_id y text son requeridos"}), 400

    embedding = model.encode(text).tolist()

    client.upsert(
        collection_name=COLLECTION_NAME,
        points=[
            PointStruct(
                id=str(candidate_id),
                vector=embedding,
                payload={"candidate_id": candidate_id}
            )
        ]
    )

    return jsonify({"status": "ok", "candidate_id": candidate_id})

# -----------------------------
# Endpoint: búsqueda semántica
# -----------------------------
@app.post("/search")
def search():
    data = request.json
    query = data.get("query")

    if not query:
        return jsonify({"error": "query es requerido"}), 400

    query_vector = model.encode(query).tolist()

    results = client.search(
        collection_name=COLLECTION_NAME,
        query_vector=query_vector,
        limit=5
    )

    formatted = [
        {
            "candidate_id": r.payload["candidate_id"],
            "score": r.score
        }
        for r in results
    ]

    return jsonify(formatted)

# -----------------------------
# Run
# -----------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
