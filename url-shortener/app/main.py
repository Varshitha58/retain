from flask import Flask
from app.routes import register_routes

def create_app():
    app = Flask(__name__)
    register_routes(app)

    @app.route('/')
    def health_check():
        return {"status": "healthy", "service": "URL Shortener API"}

    @app.route('/api/health')
    def api_health():
        return {"status": "ok", "message": "URL Shortener API is running"}

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
