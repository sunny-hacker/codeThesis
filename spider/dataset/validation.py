import json

# Assuming the validation data is stored in a separate JSON file named "spider_validation.json"
with open("spider_validation.json", "r") as f:
  validation_data = json.load(f)

# Access data for each question in the validation set
for question in validation_data:
  question_text = question["question"]
  # Access other relevant data points as needed (e.g., database schema information)
  print(f"Question: {question_text}")

# You can further process the extracted data for analysis or model evaluation
