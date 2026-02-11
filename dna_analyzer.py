def analyze_dna(sequence):
    sequence = sequence.upper()

    length = len(sequence)
    a_count = sequence.count('A')
    t_count = sequence.count('T')
    g_count = sequence.count('G')
    c_count = sequence.count('C')

    gc_content = ((g_count + c_count) / length) * 100

    print(f"Length: {length}")
    print(f"A: {a_count}")
    print(f"T: {t_count}")
    print(f"G: {g_count}")
    print(f"C: {c_count}")
    print(f"GC Content: {gc_content:.2f}%")

dna = input("Enter DNA sequence: ")
analyze_dna(dna)
