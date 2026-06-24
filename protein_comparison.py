def compare_proteins(p1, p2):

    for i in range(min(len(p1), len(p2))):

        if p1[i] != p2[i]:

            return {
                "position": i + 1,
                "original": p1[i],
                "mutated": p2[i]
            }

    return None