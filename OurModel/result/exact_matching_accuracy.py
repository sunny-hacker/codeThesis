import pandas as pd

def evaluate_exact_match(text_queries, predicted_queries):
  """
  This function evaluates the exact match accuracy between text queries 
  and predicted SQL queries, with basic pre-processing.

  Args:
      text_queries: List of text queries.
      predicted_queries: List of predicted SQL queries from your model.

  Returns:
      A dictionary with accuracy (percentage) and number of exact matches.
  """
  # Pre-process: remove whitespaces and convert to lowercase
  text_queries = [query.strip().lower() for query in text_queries]
  predicted_queries = [query.strip().lower() for query in predicted_queries]

  df = pd.DataFrame({'Text Query': text_queries, 'Predicted SQL': predicted_queries})
  df['Match'] = df['Text Query'] == df['Predicted SQL']
  accuracy = df['Match'].mean() * 100
  exact_matches = df[df['Match'] == True].shape[0]

  return {
      'accuracy': accuracy,
      'exact_matches': exact_matches
  }
