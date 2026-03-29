from flask import request, jsonify
from services.text_pipeline_service import process_fake_news_pipeline

def detect_text_fake_news_controller(collection, transformer, nli,client):
    data = request.get_json()

    if not data or "query" not in data:
        return jsonify({"error": "Query tidak ditemukan"}), 400

    query = data["query"]

    result = process_fake_news_pipeline(
        raw_text=query,
        collection=collection,
        transformer=transformer,
        nli=nli,
        client=client
    )
    return jsonify(result)