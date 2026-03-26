from flask import Blueprint
from controllers.text_detection_controller import detect_text_fake_news_controller
from controllers.kb_controller import update_knowledge_base_controller

def create_routes(collection, transformer, nli):
    bp = Blueprint("main", __name__)

    # ======================
    # SEARCH
    # ======================
    @bp.route("/search", methods=["POST"])
    def search():
        return detect_text_fake_news_controller(collection, transformer, nli)

    # ======================
    # SCRAPER
    # ======================
    @bp.route("/scrape", methods=["POST"])
    def scrape():
        return update_knowledge_base_controller(transformer, collection)

    return bp