from crewai import Agent
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from tools import serper_tool
import os
import nest_asyncio

# Fix asyncio event loop issues for Streamlit
nest_asyncio.apply()

load_dotenv()

# Gemini model
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash",
                             verbose=True, # Getting all details
                             termperature=0.5, # Randomness
                             google_api_key = os.getenv("GOOGLE_API_KEY"))

# Emails catcher Agent
email_catcher = Agent(
    role="Email Catcher",
    goal="Find the recipient's email address from a sentence",
    backstory="You specialize in finding the target email addresses in natural language",
    llm=llm,
    verbose=True
)

# Body create Agent
body_creator = Agent(
    role="Body Creator",
    goal="Generate a concise and clear body of the email",
    backstory="You're great at converting natural speech into professional email body content",
    llm=llm,
    verbose=True
)

# Subject catching or creating Agent
subject_agent = Agent(
    role="Subject Generator",
    goal="Find or generate the email subject based on input",
    backstory="You find or generate a suitable subject line for the email from the voice message",
    llm=llm,
    verbose=True,
    allow_delegation=True,
)

