from crewai import Agent
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from tools import tools
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
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

def send_email_smtp(to_email, subject, body, sender_email, sender_password):
    try:
        # Setting up the MIME
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = to_email
        msg['Subject'] = subject
        
        # Attaching the body with the email
        msg.attach(MIMEText(body, 'plain'))

        # Setting up the SMTP server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()  # Secure the connection

        # Login to the SMTP server
        server.login(sender_email, sender_password)

        # Send the email
        text = msg.as_string()
        server.sendmail(sender_email, to_email, text)

        # Quit the server
        server.quit()
        print("✅ Email sent successfully!")
    except Exception as e:
        print(f"❌ Failed to send email: {e}")

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

# Email sending Agent
email_send_agent = Agent(
    role="Email Sending Agent",
    goal="Send structured emails to the recipient using SMTP protocol.",
    backstory="An expert in delivering emails securely and reliably.",
    llm=llm,
    verbose=True
)

