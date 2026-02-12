def reverse_complement(sequence):
    sequence = sequence.upper()

    complement = {
        "A": "T",
        "G": "C",
        "T": "A",
        "C": "G"
    }

    rev_seq = sequence[::-1]
    reverse_complement_seq = ""

    for base in rev_seq:
        if base in complement:
            reverse_complement_seq += complement[base]
        else:
            return "Invalid DNA sequence"

    return reverse_complement_seq


dna = input("Enter the DNA sequence: ")
result = reverse_complement(dna)

print(f"Original: {dna.upper()}")
print(f"Reversed DNA: {result}")