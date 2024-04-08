#Matthew Stephenson
#Program 4
#04/08/2024
###################################################################
# Prog to calc GC ratio of DNA fragments and check if they fall within 35%-65% range
 
def calculate_gc_ratio(dna_fragment):
    """
    Calculate the GC ratio of a DNA fragment.
    
    :param dna_fragment: The DNA fragment to calculate the GC ratio for.
    :return: GC ratio of the DNA fragment.
    """
    dna_fragment = dna_fragment.upper()  # Convert to upper case once for efficiency
    gc_count = dna_fragment.count('G') + dna_fragment.count('C')
    return gc_count / len(dna_fragment) if dna_fragment else 0
 
def process_dna_fragments(file_name):
    """
    Process DNA fragments from file, calculating GC ratio,checking if it falls within 35%-65% range.
    
    :param file_name: The name of the file containing the DNA fragments.
    """
    with open(file_name, 'r') as file:
        for line_number, line in enumerate(file, start=1):
            dna_fragment = line.strip()
            if len(dna_fragment) < 30:
                print(f"Fragment {line_number} is too short to process.")
                continue
            gc_ratio = calculate_gc_ratio(dna_fragment)
            if 0.35 <= gc_ratio <= 0.65:
                status = "falls within 35%-65% range"
            else:
                status = "does not fall within 35%-65% range"
            print(f"Fragment {line_number} has a GC ratio of {gc_ratio:.2%} and {status}.")
 
if __name__ == "__main__":
    file_name = input("Enter name of input data file: ")
    process_dna_fragments(file_name)
 