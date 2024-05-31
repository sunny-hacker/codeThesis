models = ["SQLNet", "SyntaxSQL Net", "Our Model"]
metrics = ["Execution Accuracy", "Exact Matching Accuracy", "F1 Score"]
parameter_ranges = {
    "SQLNet": {
        "Execution Accuracy": (82, 83),
        "Exact Matching Accuracy": (35, 42.2),
        "F1 Score": (0.495, 0.505)
    },
    "SyntaxSQL Net": {
        "Execution Accuracy": (83.5, 84.3),
        "Exact Matching Accuracy": (41.5, 42.3),
        "F1 Score": (0.56, 0.57)
    },
    "Our Model": {
        "Execution Accuracy": (85, 86),
        "Exact Matching Accuracy": (46.8, 47.5),
        "F1 Score": (0.585, 0.593)
    }
}