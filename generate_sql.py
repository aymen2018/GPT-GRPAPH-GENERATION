from langchain_community.utilities import SQLDatabase
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
import re


class generateSql:
    """takes a user request and return a sql query
    in string format using GPT-4o LLM"""

    def __init__(self, llm, db):
        self.db = db
        self.llm = llm

    def get_schema(self, _):
        """extact the database structure and tables info from the
        correspond DB"""
        schema = self.db.get_table_info()
        cleaned_schema = re.sub(r"/\*.*?\*/", "", schema, flags=re.DOTALL)
        return cleaned_schema

    def generate_sql_query(self, user_question: str) -> str:
        """generate a sql query in str format. It takes the schema of our
        database (tables structures) and user input (question in the chatbot)"""

        template = """Based on the table schema below, write a SQL query that would answer the user's question:
        {schema}

        Question: {question}
        SQL Query:"""
        prompt = ChatPromptTemplate.from_template(template)

        sql_chain = (
            RunnablePassthrough.assign(schema=self.get_schema)
            | prompt
            | self.llm.bind(stop=["\nSQLResult:"])
            | StrOutputParser()
        )
        response = sql_chain.invoke({"question": user_question})
        # clean response
        sql_query = re.search(r"```sql\n(.*?)\n```", response, re.DOTALL)
        print("\n*******************Query**********************:\n")
        print(sql_query.group(1).strip())
        return sql_query.group(1).strip()
