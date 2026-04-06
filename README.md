
# JIRA Activity Tracker

A simple AI-powered chatbot that integrates with JIRA and GitHub to answer questions like:

> “What is John working on these days?”


## Features

- API-based authentication (JIRA + GitHub)
- LLM-powered natural language query parsing
- Fetches:
  - JIRA issues (active / in-progress)
  - GitHub commits
  - GitHub pull requests


## Setup Instructions

### 1. Clone the repository

```

git clone <repo-url>
cd jira_activity_tracker

```

### 2. Create and activate virtual environment

```

virtualenv venv
source venv/bin/activate

```

### 3. Install dependencies

```

pip install -r requirements.txt

```

### 4. Configure environment variables

Fill in the values in the .env file:

```

# JIRA CONFIG

JIRA_BASE_URL=[https://your-domain.atlassian.net]
JIRA_EMAIL=[your-email@example.com]
JIRA_API_TOKEN=your_jira_api_token

# GITHUB CONFIG

GITHUB_TOKEN=your_github_token

# OPENAI CONFIG

OPENAI_API_KEY=your_openai_api_key

```


## Running the Application

Start the backend server:

```

python run.py

```

Server will run at:

```

[http://localhost:5000](http://localhost:5000)

```

Then ask questions like:

- “What is John working on?”
- “What has Mike committed this week?”
- “Show me Lisa’s pull requests”


## Running Tests

Run tests using:

```

PYTHONPATH=. python -m pytest -v

```


## Work Flow

1. User submits a natural language query
2. LLM parses:
   - User name
   - Intent (COMMITS, PRS, JIRA, ALL)
3. Backend fetches data from:
   - JIRA API
   - GitHub API
4. Results are combined into a structured response
5. Response is returned to UI

