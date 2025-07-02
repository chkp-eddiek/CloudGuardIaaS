class RequestModel:
    def __init__(self, repo_path: str, project_name: str, user_name: str):
        self.repo_path = repo_path
        self.project_name = project_name
        self.user_name = user_name

    def validate(self):
        if not self.repo_path:
            raise ValueError("Repository path cannot be empty.")
        if not self.project_name:
            raise ValueError("Project name cannot be empty.")
        if not self.user_name:
            raise ValueError("User name cannot be empty.")