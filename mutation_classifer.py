def classify_mutation(comparison):

    if comparison is None:
        return "Silent"

    if comparison["mutated"] == "*":
        return "Nonsense"

    return "Missense"