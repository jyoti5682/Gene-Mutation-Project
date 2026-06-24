known_mutations = {

    ("E", "V"): {
        "disease": "Sickle Cell Disease",
        "severity": "High",
        "description": "Abnormal hemoglobin causes red blood cells to become sickle-shaped."
    },

    ("E", "K"): {
        "disease": "Hemoglobin C Disease",
        "severity": "Moderate",
        "description": "Hemoglobin variant causing mild to moderate hemolytic anemia."
    },

    ("Q", "H"): {
        "disease": "Hemoglobin D Variant",
        "severity": "Moderate",
        "description": "A hemoglobin beta-chain variant that may affect oxygen transport."
    },

    ("E", "*"): {
        "disease": "Beta Thalassemia",
        "severity": "High",
        "description": "Premature stop codon prevents normal beta-globin production."
    },

    ("K", "*"): {
        "disease": "Beta Thalassemia",
        "severity": "High",
        "description": "Early protein termination can reduce hemoglobin production."
    },

    ("W", "*"): {
        "disease": "Severe Beta Thalassemia",
        "severity": "High",
        "description": "Loss of functional beta-globin protein."
    },

    ("G", "D"): {
        "disease": "Hemoglobin G Variant",
        "severity": "Low",
        "description": "Rare hemoglobin variant."
    },

    ("A", "T"): {
        "disease": "Possible Hemoglobin Variant",
        "severity": "Low",
        "description": "Amino acid substitution observed in some hemoglobin variants."
    },

    ("V", "G"): {
        "disease": "Experimental Variant",
        "severity": "Unknown",
        "description": "Mutation detected but clinical significance is uncertain."
    },

    ("K", "M"): {
        "disease": "Experimental Variant",
        "severity": "Unknown",
        "description": "Mutation recorded for research demonstration."
    }
}

def check_disease(result):

    if result is None:
        return None

    key = (
        result["original"],
        result["mutated"]
    )

    return known_mutations.get(key)