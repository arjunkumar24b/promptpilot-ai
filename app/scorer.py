def calculate_score(query: str):

    score = 0

    query = query.lower()

    # Length Score
    if len(query) > 20:
        score += 20

    if len(query) > 50:
        score += 20

    # Goal Clarity
    keywords = [
        "learn",
        "build",
        "create",
        "understand",
        "fix",
        "improve",
        "develop",
        "prepare"
    ]

    if any(word in query for word in keywords):
        score += 20

    # Context
    if "for" in query:
        score += 20

    # Specificity
    if len(query.split()) > 8:
        score += 20

    return min(score, 100)