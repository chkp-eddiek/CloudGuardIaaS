from flask import Blueprint, request, jsonify
from src.services.github_service import GitHubService
from src.models.request_model import RequestModel
import logging

# Create a blueprint for the API
api_blueprint = Blueprint('api', __name__)

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@api_blueprint.route('/api/repo', methods=['POST'])
def create_repo():
    try:
        # Get JSON data from the request
        data = request.get_json()

        # Validate incoming request data
        request_model = RequestModel(data)
        if not request_model.is_valid():
            return jsonify({"error": "Invalid input"}), 400

        # Extract parameters
        repo_path = request_model.path
        project_name = request_model.project_name
        user_name = request_model.user_name

        # Integrate with GitHub
        github_service = GitHubService()
        result = github_service.push_changes(repo_path, project_name, user_name)

        if result:
            return jsonify({"message": "Changes pushed successfully"}), 200
        else:
            return jsonify({"error": "Failed to push changes"}), 500

    except Exception as e:
        logger.error(f"Error occurred: {str(e)}")
        return jsonify({"error": "An error occurred while processing the request"}), 500