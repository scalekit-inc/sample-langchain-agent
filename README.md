# LangChain Tool Calling Agent

A conversational LangChain agent powered by GPT-4o with Scalekit integration that demonstrates tool calling capabilities.
This project serves as a foundation for building LangChain agents with real API integrations.

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

# Scalekit Configuration From dashboard
SCALEKIT_CLIENT_ID=your_scalekit_client_id
SCALEKIT_CLIENT_SECRET=your_scalekit_client_secret
SCALEKIT_ENV_URL=your_scalekit_environment_url
```
get these from your Scalekit dashboard at [app.scalekit.com](https://app.scalekit.com) 
Developers-> Settings -> API Credentials

## Usage

1. Run the agent:
   ```bash
   python main.py
   ```

2. Follow the authorization prompts for each service (e.g., Gmail)
![Agent screenshot](https://testmagiclink-dev.scalekit.cloud/magicLink/f368ec29-d2fc-493a-aba6-befadfa08fa0_o)
3. Start chatting with the agent

### Example Usage

```
You: Hello!
Agent: Hi! I can help you with various tasks using connected services.

You: fetch my first unread email
```



## Configuration Options

In `main.py`, you can customize:

```python
user_name = "user-1234"  # Change to your desired identifier
connection_names = ["gmail"]  # Add more connection names as needed
```
## Extending the Agent

To add more services:
1. Add your connection name to `connection_names` array
2. Ensure the connection is configured in your Scalekit dashboard [app.scalekit.com](https://app.scalekit.com)
 Agent Actions -> Connections -> Create Connection
3. The agent will automatically include tools for the new service

![Create A conenction](https://github.com/user-attachments/assets/98f7bbad-08a2-4a42-a9f8-c6301cfb72a1)
