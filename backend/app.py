from flask import Flask
from flask_cors import CORS
from pathlib import Path
from .api.routes import bp

def create_app():
    app = Flask(__name__, static_folder=None, static_url_path=None)
    CORS(app)
    app.register_blueprint(bp, url_prefix="/api")
    
    # Serve frontend static files if they exist
    frontend_dist = Path(__file__).parent.parent / "frontend" / "dist"
    if frontend_dist.exists():
        from flask import send_from_directory
        
        @app.route("/")
        def serve_root():
            return send_from_directory(frontend_dist, "index.html")
        
        @app.route("/<path:path>")
        def serve_static(path):
            if Path(frontend_dist / path).exists():
                return send_from_directory(frontend_dist, path)
            return send_from_directory(frontend_dist, "index.html")
    
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(port=8000, debug=True)