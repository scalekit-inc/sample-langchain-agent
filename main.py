import os
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain.tools import tool
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage, AIMessage
from langchain_openai import ChatOpenAI
import scalekit.client
from dotenv import load_dotenv
# Load environment variables from .env file
load_dotenv()
scalekit = scalekit.client.ScalekitClient(
    client_id=os.getenv("SCALEKIT_CLIENT_ID"),
    client_secret=os.getenv("SCALEKIT_CLIENT_SECRET"),
    env_url=os.getenv("SCALEKIT_ENV_URL"),
)
actions = scalekit.actions

user_name = "user-1234"  # Change this to your desired identifier
connection_names = ["gmail"] # Add more connection names as needed. Remember to create connections in Scalekit dashboard



def create_tool_agent():
    """Create a LangChain agent with weather tools."""
    # Use GPT-4o model
    llm = ChatOpenAI(
        model="gpt-4o",
        temperature=0.1,
        api_key=os.getenv("OPENAI_API_KEY")
    )
    
    for conn_name in connection_names:  
            link = actions.get_authorization_link(
                identifier=user_name,
                connection_name=conn_name
            )
            print(f"🔗 Authorize {conn_name}: {link.link}")
            input("✅ Press Enter after authorization...")

    # Define the tools
    scalekit_tools = actions.langchain.get_tools(
        identifier= user_name,
        connection_names= connection_names,
        page_size=100
    ) 
    print (f"Using tools: {[tool.name for tool in scalekit_tools]}")
    
    
    # Create the prompt template
    prompt = ChatPromptTemplate.from_messages([
        ("system", 
         """
         You are a helpful conversational assistant with access to  tools. 
         You can have normal conversations with users AND help them with queries that need tool access.
        """),
        ("placeholder", "{chat_history}"),
        ("human", "{input}"),
        ("placeholder", "{agent_scratchpad}"),
    ])
    
    # Create the agent
    agent = create_tool_calling_agent(llm, scalekit_tools, prompt)
    
    # Create the agent executor
    agent_executor = AgentExecutor(
        agent=agent, 
        tools=scalekit_tools, 
        verbose=False,  # Set to True for debugging
        handle_parsing_errors=True
    )
    
    return agent_executor


def main():
    """Main chat loop for the weather agent."""
    print(f"Hi {user_name} Welcome to the Conversational Tool Calling Agent!")    
    
    agent = create_tool_agent()
    chat_history = []
    
    while True:
        try:
            user_input = input("You: ").strip()
            if not user_input:
                continue
            
            # Use the real LangChain agent with GPT-4o
            response = agent.invoke({
                "input": user_input,
                "chat_history": chat_history
            })
            agent_response = response["output"]
            
            # Only print "Agent: " if no tools were used (regular conversation)
            if "intermediate_steps" in response and len(response["intermediate_steps"]) > 0:
                # Tools were used, show processing message and then the response
                print("🔧 Agent is processing tool call...")
                print(agent_response)
            else:
                # No tools used, print with "Agent: " prefix
                print(f"Agent: {agent_response}")
            
            # Update chat history
            chat_history.extend([
                HumanMessage(content=user_input),
                AIMessage(content=agent_response)
            ])
            
            
            if len(chat_history) > 20:
                chat_history = chat_history[-20:]
            
            print() 
            
        except KeyboardInterrupt:
            print("\n\nGoodbye! 👋 Thanks for chatting!")
            break

if __name__ == "__main__":
    main()
