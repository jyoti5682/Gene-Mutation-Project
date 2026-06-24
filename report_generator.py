def generate_report(
    position,
    old_base,
    new_base,
    original_codon,
    mutated_codon,
    mutation_type,
    result
):

    # Detailed report
    with open("report.txt", "w") as file:

        file.write("HBB Mutation Analysis Report\n")
        file.write("=" * 40 + "\n\n")

        file.write(f"Nucleotide Position: {position}\n")
        file.write(f"Original Base: {old_base}\n")
        file.write(f"Mutated Base: {new_base}\n\n")

        file.write(f"Original Codon: {original_codon}\n")
        file.write(f"Mutated Codon: {mutated_codon}\n\n")

        file.write(f"Mutation Type: {mutation_type}\n\n")

        if result:
            file.write(
                f"Amino Acid Change: "
                f"{result['original']} -> {result['mutated']}\n"
            )
        else:
            file.write("No amino acid change\n")

    # Mutation history
    with open("mutation_history.txt", "a") as history:

        if result:
            aa_change = (
                f"{result['original']}->{result['mutated']}"
            )
        else:
            aa_change = "None"

        history.write(
            f"{position},"
            f"{old_base},"
            f"{new_base},"
            f"{original_codon},"
            f"{mutated_codon},"
            f"{mutation_type},"
            f"{aa_change}\n"
        )

    print("\nReport saved as report.txt")
    print("Mutation saved in mutation_history.txt")