from Bio import SeqIO

def load_sequence(filepath):
    record = SeqIO.read(filepath, "fasta")

    return {
        "id": record.id,
        "description": record.description,
        "sequence": str(record.seq)
    }