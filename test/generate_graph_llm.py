from langchain_community.utilities import SQLDatabase
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
import os
import warnings
from sqlalchemy import exc
from display_result import display_result
from generate_sql import generateSql
from dotenv import load_dotenv

# Suppress specific SQLAlchemy warnings
warnings.filterwarnings("ignore", category=exc.SAWarning)
load_dotenv()
api_key = os.getenv("api_key", None)
llm = ChatOpenAI(model="gpt-4o", api_key=api_key)
db = SQLDatabase.from_uri("mysql+pymysql://riseup:riseup@127.0.0.1/riseup")
user_input = "I want the number of trainings each day for all users over the past year indexed by email."
sql_generator = generateSql(llm, db)
sql_query = sql_generator.generate_sql_query(user_input)
print(sql_query)
exit()


def get_data(_):
    data = """email,subscription_date,trainings_count
            AdeleV@0g7ls.onmicrosoft.com,2024-09-16,1
            admin_internal_1_c_1@gmail.com,2024-09-17,4
            admin_internal_1_c_2@gmail.com,2024-09-17,1
            AlexW@0g7ls.onmicrosoft.com,2024-09-16,2
            community_manager_1_c_2@gmail.com,2024-09-17,1
            designer_1_c_2@gmail.com,2024-09-17,1
            DiegoS@0g7ls.onmicrosoft.com,2024-09-16,1
            facilitator_1_c_2@gmail.com,2024-09-17,1
            GradyA@0g7ls.onmicrosoft.com,2024-09-16,1
            HenriettaM@0g7ls.onmicrosoft.com,2024-09-16,1
            learner_1@training-waiting-list.com,2024-09-17,4
            learner_2@training-waiting-list.com,2024-09-17,4
            learner_3@training-waiting-list.com,2024-09-17,4
            learner_internal_1_c_1@gmail.com,2024-09-17,5
            learner_internal_1_c_11@gmail.com,2024-09-17,7
            learner_internal_1_c_2@gmail.com,2024-09-15,1
            learner_internal_1_c_9@gmail.com,2024-07-24,3
            learner_internal_1_c_9@gmail.com,2024-07-25,3
            learner_internal_1_c_9@gmail.com,2024-07-26,3
            learner_internal_1_c_9@gmail.com,2024-07-27,3
            learner_internal_1_c_9@gmail.com,2024-07-28,3
            learner_internal_1_c_9@gmail.com,2024-07-29,3
            learner_internal_1_c_9@gmail.com,2024-07-30,3
            learner_internal_1_c_9@gmail.com,2024-07-31,3
            learner_internal_1_c_9@gmail.com,2024-08-01,3
            learner_internal_1_c_9@gmail.com,2024-08-02,3
            learner_internal_1_c_9@gmail.com,2024-08-03,3
            learner_internal_1_c_9@gmail.com,2024-08-04,3
            learner_internal_1_c_9@gmail.com,2024-08-05,3
            learner_internal_1_c_9@gmail.com,2024-08-06,3
            learner_internal_1_c_9@gmail.com,2024-08-07,3
            learner_internal_1_c_9@gmail.com,2024-08-08,3
            learner_internal_1_c_9@gmail.com,2024-08-09,3
            learner_internal_1_c_9@gmail.com,2024-08-10,3
            learner_internal_1_c_9@gmail.com,2024-08-11,3
            learner_internal_1_c_9@gmail.com,2024-08-12,3
            learner_internal_1_c_9@gmail.com,2024-08-13,3
            learner_internal_1_c_9@gmail.com,2024-08-14,3
            learner_internal_1_c_9@gmail.com,2024-08-15,3
            learner_internal_1_c_9@gmail.com,2024-08-16,3
            learner_internal_1_c_9@gmail.com,2024-08-17,3
            learner_internal_1_c_9@gmail.com,2024-08-18,3
            learner_internal_1_c_9@gmail.com,2024-08-19,3
            learner_internal_1_c_9@gmail.com,2024-08-20,3
            learner_internal_1_c_9@gmail.com,2024-08-21,3
            learner_internal_1_c_9@gmail.com,2024-08-22,3
            learner_internal_1_c_9@gmail.com,2024-08-23,3
            learner_internal_1_c_9@gmail.com,2024-08-24,3
            learner_internal_1_c_9@gmail.com,2024-08-25,3
            learner_internal_1_c_9@gmail.com,2024-08-26,3
            learner_internal_1_c_9@gmail.com,2024-08-27,3
            learner_internal_1_c_9@gmail.com,2024-08-28,3
            learner_internal_1_c_9@gmail.com,2024-08-29,3
            learner_internal_1_c_9@gmail.com,2024-08-30,3
            learner_internal_1_c_9@gmail.com,2024-08-31,3
            learner_internal_1_c_9@gmail.com,2024-09-01,3
            learner_internal_1_c_9@gmail.com,2024-09-02,3
            learner_internal_1_c_9@gmail.com,2024-09-03,3
            learner_internal_1_c_9@gmail.com,2024-09-04,3
            learner_internal_1_c_9@gmail.com,2024-09-05,3
            learner_internal_1_c_9@gmail.com,2024-09-06,3
            learner_internal_1_c_9@gmail.com,2024-09-07,3
            learner_internal_1_c_9@gmail.com,2024-09-08,3
            learner_internal_1_c_9@gmail.com,2024-09-09,3
            learner_internal_1_c_9@gmail.com,2024-09-10,3
            learner_internal_1_c_9@gmail.com,2024-09-11,3
            learner_internal_1_c_9@gmail.com,2024-09-12,3
            learner_internal_1_c_9@gmail.com,2024-09-13,3
            learner_internal_1_c_9@gmail.com,2024-09-14,3
            learner_internal_1_c_9@gmail.com,2024-09-15,4
            learner_internal_1_c_9@gmail.com,2024-09-16,6
            learner_internal_1_c_9@gmail.com,2024-09-17,99
            learner_internal_2_c_10@gmail.com,2024-09-17,1
            learner_internal_2_c_2@gmail.com,2024-09-17,1
            learner_internal_2_c_9@gmail.com,2024-09-17,10
            learner_internal_3_mobile_2@gmail.com,2024-09-17,1
            learner_internal_3_mobile@gmail.com,2024-09-17,5
            learner_internal_4_mobile@gmail.com,2024-09-17,3
            learner_internal_5_mobile@gmail.com,2024-09-16,2
            learner_internal_6_mobile@gmail.com,2024-09-16,1
            learner_internal_6_mobile@gmail.com,2024-09-17,3
            learner_internal_7_mobile@gmail.com,2024-09-17,10
            learner_internal_8_mobile@gmail.com,2024-09-17,1
            """
    return data


template = """Title: "Graph Generator"
The following are types of graphs:
+(Bar Graph Syntax)=[The following represents a bar graph in javascript displayed in image markdown format:
![pollinations](https://www.quickchart.io/chart?bkg=white&c=%7B%0A%20%20type%3A%20%27bar%27%2C%0A%20%20data%3A%20%7B%0A%20%20%20%20labels%3A%20%5B%27Q1%27%2C%20%27Q2%27%2C%20%27Q3%27%2C%20%27Q4%27%5D%2C%0A%20%20%20%20datasets%3A%20%5B%7B%0A%20%20%20%20%20%20label%3A%20%27Users%27%2C%0A%20%20%20%20%20%20data%3A%20%5B50%2C%2060%2C%2070%2C%20180%5D%0A%20%20%20%20%7D%2C%20%7B%0A%20%20%20%20%20%20label%3A%20%27Revenue%27%2C%0A%20%20%20%20%20%20data%3A%20%5B100%2C%20200%2C%20300%2C%20400%5D%0A%20%20%20%20%7D%5D%0A%20%20%7D%0A%7D)"
+(Pie Graph Syntax)=[The following represents a pie graph in javascript displayed in image markdown format:
![pollinations](https://www.quickchart.io/chart?c=%7B%0A%20%20%22type%22%3A%20%22outlabeledPie%22%2C%0A%20%20%22data%22%3A%20%7B%0A%20%20%20%20%22labels%22%3A%20%5B%22ONE%22%2C%20%22TWO%22%2C%20%22THREE%22%2C%20%22FOUR%22%2C%20%22FIVE%22%5D%2C%0A%20%20%20%20%22datasets%22%3A%20%5B%7B%0A%20%20%20%20%20%20%20%20%22backgroundColor%22%3A%20%5B%22%23FF3784%22%2C%20%22%2336A2EB%22%2C%20%22%234BC0C0%22%2C%20%22%23F77825%22%2C%20%22%239966FF%22%5D%2C%0A%20%20%20%20%20%20%20%20%22data%22%3A%20%5B1%2C%202%2C%203%2C%204%2C%205%5D%0A%20%20%20%20%7D%5D%0A%20%20%7D%2C%0A%20%20%22options%22%3A%20%7B%0A%20%20%20%20%22plugins%22%3A%20%7B%0A%20%20%20%20%20%20%22legend%22%3A%20false%2C%0A%20%20%20%20%20%20%22outlabels%22%3A%20%7B%0A%20%20%20%20%20%20%20%20%22text%22%3A%20%22%25l%20%25p%22%2C%0A%20%20%20%20%20%20%20%20%22color%22%3A%20%22white%22%2C%0A%20%20%20%20%20%20%20%20%22stretch%22%3A%2035%2C%0A%20%20%20%20%20%20%20%20%22font%22%3A%20%7B%0A%20%20%20%20%20%20%20%20%20%20%22resizable%22%3A%20true%2C%0A%20%20%20%20%20%20%20%20%20%20%22minSize%22%3A%2012%2C%0A%20%20%20%20%20%20%20%20%20%20%22maxSize%22%3A%2018%0A%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20%7D%0A%20%20%20%20%7D%0A%20%20%7D%0A%7D)
+(Line Graph Syntax)=[The following represents a line graph in javascript displayed in image markdown format:
![pollinations](https://www.quickchart.io/chart?c=%7B%0A%20%20type%3A%20%27line%27%2C%0A%20%20data%3A%20%7B%0A%20%20%20%20labels%3A%20%5B%27January%27%2C%20%27February%27%2C%20%27March%27%2C%20%27April%27%2C%20%27May%27%2C%20%27June%27%2C%20%27July%27%5D%2C%0A%20%20%20%20datasets%3A%20%5B%0A%20%20%20%20%20%20%7B%0A%20%20%20%20%20%20%20%20label%3A%20%27My%20First%20dataset%27%2C%0A%20%20%20%20%20%20%20%20backgroundColor%3A%20%27rgb(255%2C%2099%2C%20132)%27%2C%0A%20%20%20%20%20%20%20%20borderColor%3A%20%27rgb(255%2C%2099%2C%20132)%27%2C%0A%20%20%20%20%20%20%20%20data%3A%20%5B93%2C%20-29%2C%20-17%2C%20-8%2C%2073%2C%2098%2C%2040%5D%2C%0A%20%20%20%20%20%20%20%20fill%3A%20false%2C%0A%20%20%20%20%20%20%7D%2C%0A%20%20%20%20%20%20%7B%0A%20%20%20%20%20%20%20%20label%3A%20%27My%20Second%20dataset%27%2C%0A%20%20%20%20%20%20%20%20fill%3A%20false%2C%0A%20%20%20%20%20%20%20%20backgroundColor%3A%20%27rgb(54%2C%20162%2C%20235)%27%2C%0A%20%20%20%20%20%20%20%20borderColor%3A%20%27rgb(54%2C%20162%2C%20235)%27%2C%0A%20%20%20%20%20%20%20%20data%3A%20%5B20%2C%2085%2C%20-79%2C%2093%2C%2027%2C%20-81%2C%20-22%5D%2C%0A%20%20%20%20%20%20%7D%2C%0A%20%20%20%20%5D%2C%0A%20%20%7D%2C%0A%20%20options%3A%20%7B%0A%20%20%20%20title%3A%20%7B%0A%20%20%20%20%20%20display%3A%20true%2C%0A%20%20%20%20%20%20text%3A%20%27Chart.js%20Line%20Chart%27%2C%0A%20%20%20%20%7D%2C%0A%20%20%7D%2C%0A%7D%0A)


+(Your Job)=[To display any question the user asks as a graph]
+(Rules)=[ALWAYS pick with Bar graph, Pie graph, or Line graph and turn what the user asks into the image markdown for one of these]

ALWAYS DISPLAY WHAT THE USER ASKS AS A GRAPH.

Question : {question}
data : {data}

"""
prompt = ChatPromptTemplate.from_template(template)

sql_chain = (
    RunnablePassthrough.assign(data=get_data)
    | prompt
    | llm.bind(stop=["\nSQLResult:"])
    | StrOutputParser()
)

users_questions = [
    "I want the number of trainings each day for all users over the past year indexed by email."
]

display_result(users_questions, sql_chain)
