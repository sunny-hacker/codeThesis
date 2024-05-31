import json

# Assuming the data is stored in a file called "spider_data.json"
with open("spider_data.json", "r") as f:
  data = json.load(f)

# Access data for each model
sqlnet_accuracy = data["SQLNet"]["execution_accuracy"]
syntaxsql_accuracy = data["SyntaxSQL Net"]["execution_accuracy"]
your_model_accuracy = data["Our Model"]["execution_accuracy"]

# Access data for exact matching accuracy can be done similarly

# Print or process the extracted data
print(f"SQLNet Execution Accuracy: {sqlnet_accuracy}")
print(f"SyntaxSQL Net Execution Accuracy: {syntaxsql_accuracy}")
print(f"Your Model Execution Accuracy: {your_model_accuracy}")

# You can further iterate through the data structure to access other metrics
