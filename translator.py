from Bio.Seq import Seq

def translate_sequence(sequence):

    seq = Seq(sequence)

    protein = seq.translate()

    return str(protein)