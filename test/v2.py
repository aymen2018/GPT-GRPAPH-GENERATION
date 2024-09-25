from dotenv import load_dotenv
from langchain_community.utilities import SQLDatabase
from langchain_openai import ChatOpenAI
from langchain.chains import create_sql_query_chain
import os

load_dotenv()
# load api key
api_key = os.getenv("api_key", None)

# import db test
uri = "mysql+pymysql://riseup:riseup@127.0.0.1/riseup"
db = SQLDatabase.from_uri(uri)
# print(db.get_usable_table_names())
#db = SQLDatabase.from_uri("sqlite:///Chinook.db")
llm = ChatOpenAI(model="gpt-4o", api_key=api_key)
chain = create_sql_query_chain(llm, db)
chain.get_prompts()[0].pretty_print()
response = chain.invoke({"question": "How many users are there"})
cleaned_response = (
    response.strip()
    .replace("```sql", "")
    .replace("```", "")
    .replace("SQLQuery:", "")
    .strip()
)
print(cleaned_response)
# Run the cleaned SQL query on the database
result = db.run(cleaned_response)
# Print the result
print(result)
