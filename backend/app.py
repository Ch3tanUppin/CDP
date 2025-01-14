from flask import Flask, request, jsonify
from flask_cors import CORS
from scraper import scrape_all_docs
from search_engine import index_docs, search

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Scrape and index documentation
try:
    docs = scrape_all_docs()
    indexed_data = {key: index_docs(value) for key, value in docs.items()}
except Exception as e:
    print(f"Error during scraping or indexing: {e}")
    indexed_data = {}

@app.route("/query", methods=["POST"])
def query():
    try:
        # Parse the request JSON
        data = request.json
        platform = data.get("platform")
        question = data.get("question")

        # Validate input
        if not platform or not question:
            return jsonify({"error": "Both 'platform' and 'question' are required"}), 400

        # Check if the platform is supported
        if platform not in indexed_data:
            return jsonify({"error": f"Platform '{platform}' not supported"}), 400

        # Perform the search
        docs, embeddings = indexed_data[platform]
        results = search(question, docs, embeddings)

        # Return results
        return jsonify({"answers": results})

    except Exception as e:
        # Catch unexpected errors
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True)
