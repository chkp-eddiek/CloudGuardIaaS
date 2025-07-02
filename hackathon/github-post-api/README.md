# GitHub POST API

This project is a simple Flask-based API that integrates with GitHub to manage code repositories. It allows users to specify a path to a code repository, a project name, and a user name to perform operations on GitHub.

## Features

- POST API endpoint to interact with GitHub repositories.
- Basic logging functionality to track events and errors.
- Validation of incoming request parameters.

## Project Structure

```
github-post-api
├── src
│   ├── main.py               # Entry point of the application
│   ├── api
│   │   └── endpoints.py      # Defines the API endpoint
│   ├── services
│   │   └── github_service.py  # Logic for GitHub integration
│   ├── models
│   │   └── request_model.py   # Data model for incoming requests
│   └── utils
│       └── logger.py         # Logging functionality
├── requirements.txt          # Project dependencies
└── README.md                 # Project documentation
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd github-post-api
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the application:
   ```
   python src/main.py
   ```

## Usage

To use the API, send a POST request to the endpoint with the required parameters. Example:

```
POST /api/github
Content-Type: application/json

{
    "path": "/path/to/repo",
    "project_name": "my_project",
    "user_name": "my_username"
}
```

## Logging

The application includes basic logging to track events and errors. Logs will be output to the console.

## License

This project is licensed under the MIT License.