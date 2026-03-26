from flask import request, jsonify
from services.text_pipeline_service import process_fake_news_pipeline

def detect_text_fake_news_controller(collection, transformer, nli):
    data = request.get_json()

    if not data or "query" not in data:
        return jsonify({"error": "Query tidak ditemukan"}), 400

    query = data["query"]

    result = process_fake_news_pipeline(
        query=query,
        collection=collection,
        transformer=transformer,
        nli=nli
    )
    print(result)
    return jsonify(result)