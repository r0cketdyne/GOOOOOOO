#Matthew Stephenson
#Program 4
#04/08/2024
# Prog to calc GC ratio of DNA fragments and check if they fall within 35%-65% range
###################################################################

 
import os #import standard lib to interact with operating system

def calculate_gc_ratio(dna_fragment):
    """
    Calculate the GC ratio of a DNA frag.
    
    :param dna_fragment: The DNA frag to calculate the GC ratio for.
    :return: GC ratio of the DNA frag.
    """
    dna_fragment = dna_fragment.upper()  # Convert to upper case once for efficiency
    gc_count = dna_fragment.count('G') + dna_fragment.count('C')  # Count occurrences of G and C
    return gc_count / len(dna_fragment) if dna_fragment else 0  # Calculate GC ratio

def process_dna_fragments(file_name):
    """
    Process DNA frag's from file, calculating GC ratio, checking if it falls within 35%-65% range.
    
    :param file_name: The name of the file containing the DNA frags.
    """
    if not os.path.exists(file_name):  # Check if the file actually existsat pwd
        print(f"Error: File '{file_name}' does not exist.")
        return
    
    print(f"Processing file: {file_name}")
    
    output_file = "REPORT ON INPUT FILE: " + file_name + ".txt"  # Create output file name
    with open(output_file, 'w') as report_file:  # Open output file for writing
        report_file.write("FRAGMENT GCRatio Other messages\n")  # Write header
        report_file.write("----------------------------------------------------------------------------------------------\n")
        
        total_fragments = 0  # Counter for total fragments
        not_long_enough = 0  # Counter for fragments not long enough
        longest_fragment_length = 0  # Variable to store length of longest fragment
        
        with open(file_name, 'r') as file:  # Open input file for reading at pwd. one of three flags
            for line_number, line in enumerate(file, start=1):  # Read lines from file
                dna_fragment = line.strip()  # Remove leading/trailing whitespace
                if len(dna_fragment) < 30:  # Check if fragment is too short
                    report_file.write(f"{dna_fragment} : Fragment is too short to process.\n")  # Write message
                    not_long_enough += 1  # Increment counter
                else:
                    gc_ratio = calculate_gc_ratio(dna_fragment)  # Calculate GC ratio
                    status = "Fragment within the range 35% - 65%" if 0.35 <= gc_ratio <= 0.65 else ""  # Determine status
                    report_file.write(f"{dna_fragment} : {gc_ratio:.2%} {status}\n")  # Write fragment info
                    total_fragments += 1  # Increment counter
                    longest_fragment_length = max(longest_fragment_length, len(dna_fragment))  # Update longest fragment length
        
        # Write summary
        report_file.write("---------------------------------------- SUMMARY -----------------------------------------------\n")
        report_file.write(f"There were {total_fragments} fragments found.\n")
        report_file.write(f"{not_long_enough} fragment was/were not long enough to process.\n")
        report_file.write(f"The longest fragment found had {longest_fragment_length} values\n")

if __name__ == "__main__":
    file_name = input("Welcome to the DNA profiler. This program will analyze a collection of DNA fragments from a specified input file, generating a report detailing the GC-ratios identified within the file. Enter name of input data file at pwd: ")  # Get input file name from usr
    process_dna_fragments(file_name)  # Process DNA frag
    print("Processing complete.")  # Print completion message



#input file was unable to be uploaded as .txt as canvas takes only .py files. I may upload it as a comment .py or wmail