import csv

# Assuming the data is stored in a file called "spider_data.csv"
with open("spider_data.csv", "r") as f:
  reader = csv.DictReader(f)

  # Loop through each row in the CSV
  for row in reader:
    model_name = row["Model"]
    execution_accuracy = float(row["Execution Accuracy"])
    exact_matching_accuracy = float(row["Exact Matching Accuracy"])

    # Process the extracted data for each model
    print(f"{model_name} - Execution Accuracy: {execution_accuracy}, Exact Matching Accuracy: {exact_matching_accuracy}")

  # You can further process the data after iterating through all rows
