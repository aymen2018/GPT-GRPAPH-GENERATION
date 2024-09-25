import re
import pandas as pd
import matplotlib.pyplot as plt
import os

# AI response text containing the data
ai_response = """
- **September 18, 2024:** 2 trainings
- **September 19, 2024:** 1 training
"""

# Function to parse the response and extract the data
def parse_ai_response(response):
    # Regular expression to match date and training count
    pattern = r"\*\*(.*?)\*\*: (\d+) trainings"
    
    # Find all matches of the pattern in the response text
    matches = re.findall(pattern, response)

    if not matches:
        print("No matches found. Check the response format.")
    
    # Convert matches into a list of dictionaries with 'date' and 'trainings' keys
    data = [{"date": match[0], "trainings": int(match[1])} for match in matches]
    
    return data


# Parse the AI response
data = parse_ai_response(ai_response)

# Convert the parsed data into a Pandas DataFrame
df = pd.DataFrame(data)

# Convert the 'date' column to datetime format for proper plotting
df['date'] = pd.to_datetime(df['date'])

# Function to generate and save the line plot
def generate_graph(df, title, x_label, y_label, file_name):
    # Create the plot
    plt.figure(figsize=(10, 6))
    plt.plot(df[x_label], df[y_label], marker='o', color='b')
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()

    # Save the plot to a file
    file_path = os.path.join("/mnt/data", file_name)
    plt.savefig(file_path)
    plt.show()

    print(f"Graph saved to {file_path}")

# Generate the graph
generate_graph(
    df,
    title="Trainings Over Time",
    x_label="date",
    y_label="trainings",
    file_name="trainings_over_time.png"
)
