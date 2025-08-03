from flask import request, jsonify, redirect
from app.service import shorten_url, get_original_url, get_url_stats

def register_routes(app):
    @app.route('/api/shorten', methods=['POST'])
    def shorten():
        data = request.get_json()
        url = data.get('url')
        result = shorten_url(url)
        if 'error' in result:
            return jsonify(result), 400
        return jsonify(result), 201

    @app.route('/<short_code>', methods=['GET'])
    def redirect_to_original(short_code):
        result = get_original_url(short_code)
        if 'error' in result:
            return jsonify(result), 404
        return redirect(result['url'])

    @app.route('/api/stats/<short_code>', methods=['GET'])
    def stats(short_code):
        result = get_url_stats(short_code)
        if 'error' in result:
            return jsonify(result), 404
        return jsonify(result)
