def mutate_sequence(sequence, position, new_base):

    index = position - 1

    if index < 0 or index >= len(sequence):
        raise ValueError("Position out of range")

    sequence = list(sequence)

    old_base = sequence[index]

    sequence[index] = new_base

    mutated = "".join(sequence)

    return old_base, mutated