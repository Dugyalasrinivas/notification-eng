def get_priority_score(priority):
    """
    Simulated AI model scoring
    """

    if priority == "HIGH":
        return 0.9

    elif priority == "MEDIUM":
        return 0.6

    elif priority == "LOW":
        return 0.3

    else:
        return 0.5