from sklearn.metrics import f1_score, precision_score, recall_score

def evaluate_model_performance(y_true, y_pred):
    """
    Evaluate the performance of the text-to-SQL model using precision, recall, and F1 Score.
    
    Args:
    - y_true: List/Array of true labels.
    - y_pred: List/Array of predicted labels.
    
    Returns:
    - precision: Precision score.
    - recall: Recall score.
    - f1: F1 Score.
    """
    precision = precision_score(y_true, y_pred, average='micro')
    recall = recall_score(y_true, y_pred, average='micro')
    f1 = f1_score(y_true, y_pred, average='micro')
    
    return precision, recall, f1

# Example usage:
if __name__ == "__main__":
    # Example ground truth and predicted labels
    y_true = [...]  # Ground truth labels
    y_pred = [...]  # Model predictions
    
    # Evaluate model performance
    precision, recall, f1 = evaluate_model_performance(y_true, y_pred)
    
    print("Precision:", precision)
    print("Recall:", recall)
    print("F1 Score:", f1)
