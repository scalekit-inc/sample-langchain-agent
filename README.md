# LangChain Tool Calling Agent

A conversational LangChain agent powered by GPT-4o with Scalekit integration that demonstrates tool calling capabilities.

## Features

- 🤖 **GPT-4o Agent**: Uses OpenAI's GPT-4o for intelligent conversations and tool selection
- � **Scalekit Tools**: Integrated tools for various services (Gmail, etc.)
- �💬 **Interactive Chat**: Command-line interface for natural conversations
- 🔗 **OAuth Authorization**: Secure authorization flow for connected services

## Prerequisites

⚠️ **Required**: You need both OpenAI and Scalekit credentials.

1. **OpenAI API Key**: Get from [OpenAI Platform](https://platform.openai.com/api-keys)
2. **Scalekit Credentials**: Get from your Scalekit dashboard
3. Ensure you have sufficient credits in your OpenAI account

## Installation

1. Clone or download this project
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   
   Or using pyproject.toml:
   ```bash
   pip install -e .
   ```
3. Set up your environment variables:
   ```bash
   cp .env.example .env
   # Edit .env and add your credentials
   ```

## Configuration

Create a `.env` file with the following variables:

```bash
# OpenAI Configuration
OPENAI_API_KEY=your_openai_api_key_here

# Scalekit Configuration  
SCALEKIT_CLIENT_ID=your_scalekit_client_id
SCALEKIT_CLIENT_SECRET=your_scalekit_client_secret
SCALEKIT_ENV_URL=your_scalekit_environment_url
```

## Usage

1. Run the agent:
   ```bash
   python main.py
   ```

2. Follow the authorization prompts for each service (e.g., Gmail)
3. Start chatting with the agent

### Example Usage

```
You: Hello!
Agent: Hi! I can help you with various tasks using connected services.

You: fetch my 1st unread email
```

## How It Works

### Authorization Flow
- The agent will prompt you to authorize each connected service
- Visit the provided links to complete OAuth authorization
- Press Enter after completing each authorization

### Agent Architecture
- **GPT-4o Model**: Uses OpenAI's latest model for intelligent responses
- **Scalekit Integration**: Provides secure access to various service APIs
- **Tool Calling**: Agent automatically decides when to use tools based on conversation context
- **Chat History**: Maintains conversation context across multiple exchanges

## Configuration Options

In `main.py`, you can customize:

```python
user_name = "user-1234"  # Change to your desired identifier
connection_names = ["gmail"]  # Add more services as needed
```


## Extending the Agent

To add more services:
1. Add the service name to `connection_names` array
2. Ensure the connection is configured in your Scalekit dashboard
3. The agent will automatically include tools for the new service

This project serves as a foundation for building LangChain agents with real API integrations.