# Integrated Flask Backend with React Frontend

from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
import os
import requests

# Initialize Flask app
app = Flask(__name__, static_folder="build", static_url_path="/")
CORS(app)  # Allow cross-origin requests for API calls

# Load environment variables
FINNHUB_API_KEY = os.getenv("FINNHUB_API_KEY")

# Endpoint for recommendations
@app.route('/recommendations', methods=['POST'])
def get_recommendations():
    data = request.json
    goal = data.get("goal")
    risk = data.get("risk")
    amount = data.get("amount")

    # Mock response for now
    response = {
        "stocks": [
            {"symbol": "AAPL", "price": 150, "change_percent": 1.5},
            {"symbol": "TSLA", "price": 900, "change_percent": 3.2}
        ],
        "bonds": [
            {"symbol": "BND", "price": 100, "change_percent": 0.5}
        ],
        "note": f"Goal: {goal}, Risk: {risk}, Amount: {amount}"
    }
    return jsonify(response)

# Endpoint for portfolio
@app.route('/portfolio', methods=['GET'])
def get_portfolio():
    # Mock portfolio data
    portfolio = {
        "portfolio": [
            {"symbol": "AAPL", "shares": 10, "price": 150},
            {"symbol": "TSLA", "shares": 5, "price": 900}
        ]
    }
    return jsonify(portfolio)

# Endpoint for LinkedIn links
@app.route('/linkedin', methods=['GET'])
def get_linkedin_links():
    links = [
        "https://www.linkedin.com/in/shaan-brahmbhatt-711369323/",
        "https://www.linkedin.com/in/victor-valadez-963512282/",
        "https://www.linkedin.com/in/aganze-hamuli-684b84279/"
    ]
    return jsonify({"links": links})

# Endpoint for Market News
@app.route('/market-news', methods=['GET'])
def market_news():
    return jsonify({"iframe_url": "https://www.cnbc.com/stocks/"})

# Update "Get Started" and "Analysis" buttons logic
@app.route('/get-started', methods=['GET'])
@app.route('/analysis', methods=['GET'])
def redirect_to_form():
    return send_from_directory(app.static_folder, 'index.html')

# Route to serve React frontend
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve_react(path):
    if path and os.path.exists(os.path.join(app.static_folder, path)):
        return send_from_directory(app.static_folder, path)
    return send_from_directory(app.static_folder, 'index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
