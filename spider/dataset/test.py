import json

# Open the test data JSON file
with open("spider_test.json", "r") as f:
  test_data = json.load(f)

# Access data for each question in the test set
for question in test_data:
  question_text = question["question"]
  # Access other relevant data points as needed (e.g., database schema information)
  print(f"Question: {question_text}")

# You can further process the extracted data for analysis or evaluation
