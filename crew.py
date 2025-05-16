from crewai import Crew, Process
from agents import email_catcher, body_creator, subject_agent, email_send_agent
from tasks import create_tasks
from dotenv import load_dotenv
import os

load_dotenv()

user_token_id = os.getenv("COMPOSIO_API")

# User input text
speech_text = input("Enter the speech : ")

user_inputs = {
    'speech_text': speech_text,
    'user_token_id': user_token_id  
}

tasks = create_tasks(user_inputs)

# Crew User inputs
crew = Crew(
    agents=[email_catcher, body_creator, subject_agent, email_send_agent],
    tasks=tasks,
    process=Process.sequential,  
)

# Email planning process
result = crew.kickoff(user_inputs)

# Output
print("\n✨ Your Email ✨\n")
print(result)