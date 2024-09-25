import os
import openai, langchain
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema import SystemMessage, HumanMessage

load_dotenv()

api_key = os.getenv("api_key", None)


def get_sql_query_1(user_input):
    prompt = f"""
    You are a SQL expert. The following is the database schema and relationships:

    Tables:
    - registrations(id, registration_date, user_id)
    - users(id, name, client_id)
    - clients(id, name)
    
    Relationships:
    - registrations.user_id → users.id
    - users.client_id → clients.id

    Convert the following user request into a SQL query:
    "{user_input}"

    Example:
    "I want the number of registrations each day for this client over the past 2 years."

    SQL Query:
    """

    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a SQL expert."},
            {"role": "user", "content": prompt},
        ],
    )

    sql_query = response.choices[0].message["content"]
    return sql_query


# Define a function to get the SQL query
def get_sql_query(user_input):
    # Initialize the OpenAI chat model (gpt-4 or other model)
    chat = ChatOpenAI(model="gpt-4o", temperature=0, api_key=api_key)

    # Define the prompt template
    prompt_template = ChatPromptTemplate.from_messages(
        [
            SystemMessage(content="You are a SQL expert."),
            HumanMessage(
                content="""
        You are a SQL expert. The following is the database schema and relationships:

        Tables:
        - registrations(id, registration_date, user_id)
        - users(id, name, client_id)
        - clients(id, name)

        Relationships:
        - registrations.user_id → users.id
        - users.client_id → clients.id

        Convert the following user request into a SQL query:
        "{user_input}"

        Example:
        "I want the number of registrations each day for this client over the past 2 years."

        SQL Query:
        """
            ),
        ]
    )

    # Format the prompt with user input
    prompt = prompt_template.format_messages(user_input=user_input)

    # Get the SQL query response
    response = chat(prompt)

    # Extract and return the SQL query from the response
    sql_query = response.content
    return sql_query


user_input = (
    "I want the number of registrations each day for this client over the past year."
)
sql_query = get_sql_query(user_input)
print(sql_query)
