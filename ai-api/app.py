# app.py
from flask import Flask
from routes.route import create_routes
from config.chroma_config import get_chroma_collection
from config.transformer_config import  get_transformer_model
from config.nli_config import  get_nli_model
from config.genai_client import get_client
from config.config import Config


# ==============================
# INIT FLASK APP
# ==============================
app = Flask(__name__)
app.config.from_object(Config)

print(f"Running in {Config.ENV} mode, DEBUG={Config.DEBUG}")

# ==============================
# INIT DEPENDENCIES
# ==============================
# ChromaDB collection & model
collection = get_chroma_collection()
transformer = get_transformer_model()
nli = get_nli_model()
client = get_client()

# ==============================
# REGISTER ROUTES
# ==============================
bp = create_routes(collection, transformer, nli, client)


app.register_blueprint(bp)

# ==============================
# RUN APP
# ==============================
if __name__ == "__main__":
    app.run(debug=Config.DEBUG)