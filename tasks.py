from crewai import Task
from agents import email_catcher, body_creator, subject_agent
from textwrap import dedent

def create_tasks(input_text):
    # Email Catcher Task
    email_catcher_task = Task(
        description=dedent(f"""
            Analyze the user's voice input and extract the recipient's email address.

            Your job is to identify a valid email address that the email should be sent to.
            Return only a single valid email address like: user@example.com.

            Input Text: "{input_text}"
        """),
        agent=email_catcher,
        expected_output="Only the extracted recipient's email address, e.g., john.doe@example.com"
    )

    # Email Body Creator Task
    body_task = Task(
        description=dedent(f"""
            Generate a professional and polite email body based on the provided user input.

            The email body should clearly communicate the main message, maintain proper formatting, 
            and use appropriate tone for a professional email.

            Input Text: "{input_text}"
        """),
        agent=body_creator,
        expected_output="A well-formatted email body with clear, concise language appropriate for professional communication."
    )

    # Subject Generator Task
    subject_task = Task(
        description=dedent(f"""
            From the given user input, identify or generate a suitable subject line for the email.

            If the subject is explicitly mentioned, return it. If not, create a short and meaningful subject line
            that reflects the content or purpose of the email.

            Input Text: "{input_text}"
        """),
        agent=subject_agent,
        expected_output="A concise subject line, e.g., 'Project Deadline Extension'"
    )

    return [email_catcher_task, subject_task, body_task]
