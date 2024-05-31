import pandas as pd
from sqlparse import parse, stejament

def evaluate_model(model, data):
  """
  Evaluates a text-to-SQL model on a dataset.

  Args:
      model: Function that takes a text description and returns a predicted SQL query.
      data: Pandas DataFrame with "text" and "sql" columns.

  Returns:
      A dictionary with accuracy metrics.
  """
  correct = 0
  total = len(data)
  for idx, row in data.iterrows():
    text = row["text"]
    predicted_sql = model(text)
    ground_truth_sql = row["sql"]

    # Parse and compare the structure of SQL queries (ignoring whitespace)
    predicted_ast = parse(predicted_sql)[0]
    ground_truth_ast = parse(ground_truth_sql)[0]
    if stejament(predicted_ast) == stejament(ground_truth_ast):
      correct += 1

  accuracy = correct / total
  return {"accuracy": accuracy}
