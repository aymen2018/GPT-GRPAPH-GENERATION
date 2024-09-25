import matplotlib.pyplot as plt
import pandas as pd
from langchain_core.messages import HumanMessage
from langchain_core.messages import SystemMessage
from langgraph.prebuilt import create_react_agent
from langchain_community.agent_toolkits import SQLDatabaseToolkit
from dotenv import load_dotenv
from langchain_community.utilities import SQLDatabase
from langchain_openai import ChatOpenAI
import os


# Modified SQL_PREFIX to include graph instructions
SQL_PREFIX = """
You are an agent designed to interact with a SQL database and visualize the results.
Given an input question, create a syntactically correct SQL query to run, execute it, then return the answer.
If the question involves time series or other visualizable data (e.g., daily registrations over the past year), generate a graph.

Always look at the tables in the database first to understand the schema before querying. 

Important Rules:
1. Only retrieve the necessary data.
2. For time series data, generate a line plot where the X-axis is the time (e.g., date) and the Y-axis is the value (e.g., count of registrations).
3. Always ensure the query results are limited to a manageable size (e.g., last 365 days for yearly data).
4. DO NOT make any changes to the database (like INSERT, UPDATE, DELETE).

You will use Python tools to generate graphs if needed.
"""

system_message = SystemMessage(content=SQL_PREFIX)


# Function to generate time series graph
def generate_graph(df, title, x_label, y_label):
    plt.figure(figsize=(10, 6))
    plt.plot(df[x_label], df[y_label], marker="o")
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    # Save the plot to a file
    file_path = os.path.join("app", "graph.png")
    plt.savefig(file_path)
    print("file path :", file_path)
    # plt.show()


# Function to run the SQL query and visualize results
def query_and_visualize(agent_executor, question):
    # Execute the query with the agent
    for s in agent_executor.stream({"messages": [HumanMessage(content=question)]}):
        print(s)
        if (
            isinstance(s, dict) and "data" in s
        ):  # Expecting the result from the SQL query
            # Convert the data into a Pandas DataFrame
            df = pd.DataFrame(
                s["data"], columns=s["columns"]
            )  # assuming data is structured as rows and columns
            print("kkkkkk")
            # Visualize the data for time-based queries
            if "date" in df.columns:
                print("gnerate graph...")
                generate_graph(
                    df,
                    title=f"Results for '{question}'",
                    x_label="date",  # assuming 'date' is the time field
                    y_label=df.columns[
                        1
                    ],  # second column is usually the value (e.g., 'registrations')
                )
        else:
            print(s)


load_dotenv()
# load api key
api_key = os.getenv("api_key", None)
uri = "mysql+pymysql://riseup:riseup@127.0.0.1/riseup"
db = SQLDatabase.from_uri(uri)
llm = ChatOpenAI(model="gpt-4o", api_key=api_key)
toolkit = SQLDatabaseToolkit(db=db, llm=llm)
tools = toolkit.get_tools()
agent_executor = create_react_agent(llm, tools, messages_modifier=system_message)
# Example user input for graph generation
query_and_visualize(
    agent_executor,
    "I want the number of trainings each day for the client 'learner_internal_1_c_1@gmail.com' over the past year.",
)
