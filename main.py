from sequence_loader import load_sequence
from translator import translate_sequence
from mutation_engine import mutate_sequence
from protein_comparison import compare_proteins
from mutation_classifer import classify_mutation
from codon_analyzer import get_codon
from report_generator import generate_report
from disease_database import check_disease

# Load gene sequence
gene = load_sequence("../Data/NM_000518.5.fna")

print("\n===== HBB Mutation Analyzer =====")
print("Gene ID:", gene["id"])
print("Sequence Length:", len(gene["sequence"]))

# Find start codon
start = gene["sequence"].find("ATG")

print("\nStart Codon Position:", start)

coding_seq = gene["sequence"][start:]

# Translate protein
protein = translate_sequence(coding_seq)

print("Protein Length:", len(protein))
print("\nFirst 50 Amino Acids:")
print(protein[:50])

# Amino acid dictionary
amino_acids = {
    "A": "Alanine",
    "R": "Arginine",
    "N": "Asparagine",
    "D": "Aspartate",
    "C": "Cysteine",
    "Q": "Glutamine",
    "E": "Glutamate",
    "G": "Glycine",
    "H": "Histidine",
    "I": "Isoleucine",
    "L": "Leucine",
    "K": "Lysine",
    "M": "Methionine",
    "F": "Phenylalanine",
    "P": "Proline",
    "S": "Serine",
    "T": "Threonine",
    "W": "Tryptophan",
    "Y": "Tyrosine",
    "V": "Valine",
    "*": "STOP"
}

while True:

    try:

        position = int(
            input("\nEnter nucleotide position: ")
        )

        new_base = input(
            "Enter new base (A/T/G/C): "
        ).upper()

        if new_base not in ["A", "T", "G", "C"]:
            print("Invalid base entered.")
            continue

        old_base, mutated_seq = mutate_sequence(
            coding_seq,
            position,
            new_base
        )

        # Same base check
        if old_base == new_base:

            print("\nNo mutation created.")
            print(
                f"Position {position} already contains {old_base}"
            )

            again = input(
                "\nTry another mutation? (y/n): "
            )

            if again.lower() != "y":
                break

            continue

        # Codon analysis
        original_codon, _ = get_codon(
            coding_seq,
            position
        )

        mutated_codon, _ = get_codon(
            mutated_seq,
            position
        )

        # Translate proteins
        original_protein = translate_sequence(
            coding_seq
        )

        mutated_protein = translate_sequence(
            mutated_seq
        )

        # Compare proteins
        result = compare_proteins(
            original_protein,
            mutated_protein
        )

        mutation_type = classify_mutation(
            result
        )

        disease = check_disease(
            result
        )

        print("\n========== Mutation Report ==========")

        print("Original Base :", old_base)
        print("New Base      :", new_base)

        print("\nCodon Analysis")
        print("Original Codon :", original_codon)
        print("Mutated Codon  :", mutated_codon)

        print("\nMutation Type :", mutation_type)

        if result:

            original_name = amino_acids.get(
                result["original"],
                result["original"]
            )

            mutated_name = amino_acids.get(
                result["mutated"],
                result["mutated"]
            )

            print(
                f"\nAmino Acid Position : {result['position']}"
            )

            print(
                f"Protein Change : "
                f"{original_name} ({result['original']})"
                f" -> "
                f"{mutated_name} ({result['mutated']})"
            )

        else:

            print("\nProtein Change : None")
            print("This is a Silent Mutation")

        print("\n=== Disease Information ===")

        if disease:

            print(f"Disease : {disease['disease']}")
            print(f"Severity: {disease['severity']}")
            print(f"Details : {disease['description']}")

        else:

            print("Disease : None Detected")
            print("Severity: N/A")
            print("Details : No matching disease record found.")

        # Save report
        generate_report(
            position,
            old_base,
            new_base,
            original_codon,
            mutated_codon,
            mutation_type,
            result
        )

        again = input(
            "\nTry another mutation? (y/n): "
        )

        if again.lower() != "y":
            break

    except Exception as e:

        print("\nError:", e)

print("\nProgram Ended.")