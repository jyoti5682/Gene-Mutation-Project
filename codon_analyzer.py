def get_codon(sequence, nucleotide_position):

    pos = nucleotide_position - 1

    codon_start = (pos // 3) * 3

    codon = sequence[codon_start:codon_start + 3]

    return codon, codon_start + 1
    
    
    