from database_helper import DatabaseHelper
from langchain_community.utilities import SQLDatabase
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
import os
import warnings
from sqlalchemy import exc
from generate_sql import generateSql
from dotenv import load_dotenv

# Suppress specific SQLAlchemy warnings
warnings.filterwarnings("ignore", category=exc.SAWarning)
load_dotenv()


class GenerateGraphLLM:

    def __init__(self, user_input):
        self.user_input = user_input
        self.llm = ChatOpenAI(model="gpt-4o", api_key=os.getenv("api_key", None))
        self.db_uri = "mysql+pymysql://riseup:riseup@127.0.0.1/riseup"
        self.db = SQLDatabase.from_uri(self.db_uri)
        self.database_helper = DatabaseHelper()

    def main(self, query=None):
        sql_generator = generateSql(self.llm, self.db)
        if not query:
            query = sql_generator.generate_sql_query(self.user_input)
        response = self.generate_graph(query)
        print("\n**************LLM GPT GRAPH ***************:\n")
        print(response)

    def generate_graph(self, query: str):
        prompt = self.generate_prompt()
        sql_chain = (
            RunnablePassthrough.assign(
                result=lambda _: self.database_helper.execute_query(query),
            )
            | prompt
            | self.llm
            | StrOutputParser()
        )
        response = sql_chain.invoke({"question": user_input, "query": query})
        return response

    def generate_prompt(self):

        template = """Title: "Graph Generator"
            The following are types of graphs:
            +(Bar Graph Syntax)=[The following represents a bar graph in javascript displayed in image markdown format:
            ![pollinations](https://www.quickchart.io/chart?bkg=white&c=%7B%0A%20%20type%3A%20%27bar%27%2C%0A%20%20data%3A%20%7B%0A%20%20%20%20labels%3A%20%5B%27Q1%27%2C%20%27Q2%27%2C%20%27Q3%27%2C%20%27Q4%27%5D%2C%0A%20%20%20%20datasets%3A%20%5B%7B%0A%20%20%20%20%20%20label%3A%20%27Users%27%2C%0A%20%20%20%20%20%20data%3A%20%5B50%2C%2060%2C%2070%2C%20180%5D%0A%20%20%20%20%7D%2C%20%7B%0A%20%20%20%20%20%20label%3A%20%27Revenue%27%2C%0A%20%20%20%20%20%20data%3A%20%5B100%2C%20200%2C%20300%2C%20400%5D%0A%20%20%20%20%7D%5D%0A%20%20%7D%0A%7D"
            +(Pie Graph Syntax)=[The following represents a pie graph in javascript displayed in image markdown format:
            ![pollinations](https://www.quickchart.io/chart?c=%7B%0A%20%20%22type%22%3A%20%22outlabeledPie%22%2C%0A%20%20%22data%22%3A%20%7B%0A%20%20%20%20%22labels%22%3A%20%5B%22ONE%22%2C%20%22TWO%22%2C%20%22THREE%22%2C%20%22FOUR%22%2C%20%22FIVE%22%5D%2C%0A%20%20%20%20%22datasets%22%3A%20%5B%7B%0A%20%20%20%20%20%20%20%20%22backgroundColor%22%3A%20%5B%22%23FF3784%22%2C%20%22%2336A2EB%22%2C%20%22%234BC0C0%22%2C%20%22%23F77825%22%2C%20%22%239966FF%22%5D%2C%0A%20%20%20%20%20%20%20%20%22data%22%3A%20%5B1%2C%202%2C%203%2C%204%2C%205%5D%0A%20%20%20%20%7D%5D%0A%20%20%7D%2C%0A%20%20%22options%22%3A%20%7B%0A%20%20%20%20%22plugins%22%3A%20%7B%0A%20%20%20%20%20%20%22legend%22%3A%20false%2C%0A%20%20%20%20%20%20%22outlabels%22%3A%20%7B%0A%20%20%20%20%20%20%20%20%22text%22%3A%20%22%25l%20%25p%22%2C%0A%20%20%20%20%20%20%20%20%22color%22%3A%20%22white%22%2C%0A%20%20%20%20%20%20%20%20%22stretch%22%3A%2035%2C%0A%20%20%20%20%20%20%20%20%22font%22%3A%20%7B%0A%20%20%20%20%20%20%20%20%20%20%22resizable%22%3A%20true%2C%0A%20%20%20%20%20%20%20%20%20%20%22minSize%22%3A%2012%2C%0A%20%20%20%20%20%20%20%20%20%20%22maxSize%22%3A%2018%0A%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20%7D%0A%20%20%20%20%7D%0A%20%20%7D%0A%7D)
            +(Line Graph Syntax)=[The following represents a line graph in javascript displayed in image markdown format:
            ![pollinations](https://www.quickchart.io/chart?c=%7B%0A%20%20type%3A%20%27line%27%2C%0A%20%20data%3A%20%7B%0A%20%20%20%20labels%3A%20%5B%27January%27%2C%20%27February%27%2C%20%27March%27%2C%20%27April%27%2C%20%27May%27%2C%20%27June%27%2C%20%27July%27%5D%2C%0A%20%20%20%20datasets%3A%20%5B%0A%20%20%20%20%20%20%7B%0A%20%20%20%20%20%20%20%20label%3A%20%27My%20First%20dataset%27%2C%0A%20%20%20%20%20%20%20%20backgroundColor%3A%20%27rgb(255%2C%2099%2C%20132)%27%2C%0A%20%20%20%20%20%20%20%20borderColor%3A%20%27rgb(255%2C%2099%2C%20132)%27%2C%0A%20%20%20%20%20%20%20%20data%3A%20%5B93%2C%20-29%2C%20-17%2C%20-8%2C%2073%2C%2098%2C%2040%5D%2C%0A%20%20%20%20%20%20%20%20fill%3A%20false%2C%0A%20%20%20%20%20%20%7D%2C%0A%20%20%20%20%20%20%7B%0A%20%20%20%20%20%20%20%20label%3A%20%27My%20Second%20dataset%27%2C%0A%20%20%20%20%20%20%20%20fill%3A%20false%2C%0A%20%20%20%20%20%20%20%20backgroundColor%3A%20%27rgb(54%2C%20162%2C%20235)%27%2C%0A%20%20%20%20%20%20%20%20borderColor%3A%20%27rgb(54%2C%20162%2C%20235)%27%2C%0A%20%20%20%20%20%20%20%20data%3A%20%5B20%2C%2085%2C%20-79%2C%2093%2C%2027%2C%20-81%2C%20-22%5D%2C%0A%20%20%20%20%20%20%7D%2C%0A%20%20%20%20%5D%2C%0A%20%20%7D%2C%0A%20%20options%3A%20%7B%0A%20%20%20%20title%3A%20%7B%0A%20%20%20%20%20%20display%3A%20true%2C%0A%20%20%20%20%20%20text%3A%20%27Chart.js%20Line%20Chart%27%2C%0A%20%20%20%20%7D%2C%0A%20%20%7D%2C%0A%7D%0A)


            +(Your Job)=[To display any question the user asks as a graph]
            +(Rules)=[ALWAYS pick with Bar graph, Pie graph, or Line graph and turn what the user asks into the image markdown for one of these]

            ALWAYS DISPLAY WHAT THE USER ASKS AS A GRAPH.

            
            Question: {question}
            SQL Query: {query}
            SQL Result: {result}
            """

        prompt = ChatPromptTemplate.from_template(template)
        return prompt


if __name__ == "__main__":
    user_input = "What percentage of registrations of each company?"
    print("*********************************************************")
    print("User Input:", user_input)
    print("*********************************************************")
    generate_graph_llm = GenerateGraphLLM(user_input)
    query = """SELECT
        training.id AS training_id,
        TrainingLanguage(training.id, 1, 'title') AS training_title,
        COUNT(trainingsubscription.id) AS number_of_registrations
    FROM
        training
            JOIN trainingsubscription ON training.id = trainingsubscription.idtraining
            JOIN user ON trainingsubscription.iduser = user.id
            JOIN userusergroup ON user.id = userusergroup.iduser
            JOIN usergroup ON userusergroup.idusergroup = usergroup.id
    WHERE
        usergroup.name = 'Group 1'
    AND usergroup.idcompany = 1
    AND usergroup.disabled = 0
    AND user.disabled = 0
    AND trainingsubscription.disabled = 0
    AND training.disabled = 0
    GROUP BY
        training.id
    ORDER BY
        number_of_registrations DESC
    LIMIT 10000;"""
    generate_graph_llm.main()
