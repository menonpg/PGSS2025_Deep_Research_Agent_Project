import os
import requests
from dotenv import load_dotenv
from langchain.agents import initialize_agent, Tool
from langchain.tools import tool
from langchain_community.utilities import SerpAPIWrapper
from langchain_openai import AzureChatOpenAI

# Load environment variables
load_dotenv()

# Azure OpenAI Configuration
AZURE_API_KEY = os.getenv("AZURE_API_KEY")
AZURE_API_BASE = os.getenv("AZURE_API_BASE")  # Example: https://<your-resource-name>.openai.azure.com/
AZURE_API_VERSION = os.getenv("AZURE_API_VERSION")
AZURE_DEPLOYMENT_NAME = os.getenv("AZURE_DEPLOYMENT_NAME")

# SerpAPI Configuration
SERPAPI_API_KEY = os.getenv("SERPAPI_API_KEY")

# Initialize SerpAPI Web Search Tool
search = SerpAPIWrapper(serpapi_api_key=SERPAPI_API_KEY)

@tool
def azure_openai_tool(query: str) -> str:
    """Send a query to Azure OpenAI and get a response with APA-style citations."""
    headers = {
        "Content-Type": "application/json",
        "api-key": AZURE_API_KEY
    }
    
    payload = {
        "messages": [
            {
                "role": "system",
                "content": (
                    "You are a helpful research assistant for Biomedical Researchers. "
                    "When providing information, always include APA-style citations with links to the sources. "
                    "Ensure that all outputs are validated and vetted with proper references. "
                    "Return your output in the following format:\n"
                    "Thought: <Your thought process>\n"
                    "Action: <Action to take>\n"
                    "Observation: <Observation from the action>\n"
                    "Final Answer: <Your final answer with citations in APA style>"
                )
            },
            {"role": "user", "content": query}
        ],
        "temperature": 0.7,
        "max_tokens": 1000
    }
    
    try:
        response = requests.post(
            f"{AZURE_API_BASE}/openai/deployments/{AZURE_DEPLOYMENT_NAME}/chat/completions?api-version={AZURE_API_VERSION}",
            headers=headers,
            json=payload,
            timeout=30
        )
        
        response.raise_for_status()
        response_data = response.json()
        
        if 'choices' in response_data and len(response_data['choices']) > 0:
            return response_data['choices'][0]['message']['content']
        else:
            return "No response received from the AI."
    except requests.exceptions.Timeout:
        return "Request timed out. Please try again."
    except requests.exceptions.RequestException as e:
        return f"Network error: {e}"
    except Exception as e:
        return f"Error contacting Azure OpenAI: {e}"

# Define tools for the agent
tools = [
    Tool(name="Web Search", func=search.run, description="Search the web for information."),
    Tool(name="Azure OpenAI", func=azure_openai_tool, description="Use Azure OpenAI for reasoning and answering questions with APA-style citations.")
]

# Initialize Azure OpenAI Chat Model (LLM)
llm = AzureChatOpenAI(
    azure_endpoint=AZURE_API_BASE,  # Azure OpenAI endpoint
    deployment_name=AZURE_DEPLOYMENT_NAME,  # Deployment name
    api_version=AZURE_API_VERSION,  # API version explicitly passed
    openai_api_key=AZURE_API_KEY,  # API key
    temperature=0.7,
    max_tokens=500
)

# Initialize the agent with error handling
agent = initialize_agent(
    tools,
    llm=llm,
    agent="zero-shot-react-description",
    verbose=True,
    handle_parsing_errors=True  # Handle output parsing errors gracefully
)

# Test the agent
if __name__ == "__main__":
    print("🤖 Welcome to your AI Research Assistant with Integrated Web Access!")
    print("Type 'quit' to exit\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            print("👋 Goodbye! Happy researching!")
            break

        # Use the agent to respond
        try:
            response = agent.invoke(user_input)  # Use invoke instead of run
            print(f"🤖 AI: {response}\n")
        except Exception as e:
            print(f"🤖 AI: An error occurred: {e}\n")