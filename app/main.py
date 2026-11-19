import os
from flask import Flask, jsonify

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")

    @app.after_request
    def security_headers(response):
        response.headers["X-Content-Type-Options"] = "nosniff"
        response.headers["X-Frame-Options"] = "DENY"
        response.headers["Cache-Control"] = "no-store"
        return response

    @app.route("/")
    def home():
        return jsonify({
            "application": "Enterprise DevOps Deployment Toolkit",
            "version": os.environ.get("APP_VERSION", "1.0.0"),
            "environment": os.environ.get("APP_ENV", "development"),
            "status": "running"
        })

    @app.route("/health")
    def health():
        return jsonify({"status": "healthy"})

    @app.route("/ready")
    def ready():
        return jsonify({"status": "ready"})

    return app

app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
