from langchain_community.utilities import SQLDatabase
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
import re
import os
import warnings
from sqlalchemy import exc


# Suppress specific SQLAlchemy warnings
warnings.filterwarnings("ignore", category=exc.SAWarning)





db_uri = "mysql+pymysql://riseup:riseup@127.0.0.1/riseup"
db = SQLDatabase.from_uri(db_uri)

template = """Based on the table schema below, write a SQL query that would answer the user's question:
{schema}

Question: {question}
SQL Query:"""
prompt = ChatPromptTemplate.from_template(template)

llm = ChatOpenAI(model="gpt-4o", api_key=os.environ.get("OPENAI_API_KEY"))
sql_chain = (
    RunnablePassthrough.assign(schema=get_schema)
    | prompt
    | llm.bind(stop=["\nSQLResult:"])
    | StrOutputParser()
)

users_questions = [
    "I want the number of trainings each day for the client 'learner_internal_1_c_1@gmail.com' over the past year.",
    "I want the number of trainings each day for all users over the past year indexed by user email.",
]

for user_question in users_questions:
    print("********************************************************************")
    print("User question:", user_question)
    print("********************************************************************")

    response = sql_chain.invoke({"question": user_question})
    print("********************************************************************")
    # Clean the response to extract only the SQL query part
    sql_query = re.search(r"```sql\n(.*?)\n```", response, re.DOTALL)
    if sql_query:
        print("SQL Query:", sql_query.group(1).strip())
    else:
        print("response:", response)
    print("********************************************************************")
