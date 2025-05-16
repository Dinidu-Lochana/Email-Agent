from composio_crewai import ComposioToolSet, Action, App

import os
from dotenv import load_dotenv

api_key=os.getenv("COMPOSIO_API")

composio_toolset = ComposioToolSet(api_key)
tools = composio_toolset.get_tools(actions=['GMAIL_SEND_EMAIL'])