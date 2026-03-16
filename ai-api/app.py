from flask import Flask
from config.config import Config
from routes.route import welcome_bp

app = Flask(__name__)
app.config.from_object(Config)

# register blueprint
app.register_blueprint(welcome_bp)

if __name__ == "__main__":
    app.run(debug=True)