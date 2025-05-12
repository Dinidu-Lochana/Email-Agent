from crewai import Crew, Process
from agents import email_catcher, body_creator, subject_agent
from tasks import create_tasks

# User input text
speech_text = input("Enter the speech : ")

user_inputs = {
    'speech_text' : speech_text
}

tasks = create_tasks(user_inputs)

# Crew User inputs
crew = Crew(
    agents=[email_catcher, body_creator, subject_agent],
    tasks=tasks,
    process=Process.sequential,  
)

# Email planning process
result = crew.kickoff(inputs=user_inputs)

# Output
print("\n✨ Your Email ✨\n")
print(result)