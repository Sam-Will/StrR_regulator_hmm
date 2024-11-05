import re

def process_line(line):
    # Split the line by multiple spaces and return a comma-separated string
    return re.sub(' +', ',', line.strip()) + '\n'

def compile_hmmsearch_results_to_csv():
    result_file = 'mibig/mibig_3.0_tbl_StrR_test.tbl'  # Specify the single file name
    csv_file = 'mibig_3.0_hmmsearch_results.csv'

    with open(csv_file, 'w') as csv:
        with open(result_file, 'r') as f:
            for line in f:
                if line.startswith('#'):
                    continue  # Skip comment lines
                processed_line = process_line(line)
                csv.write(processed_line)

# Call the function to execute
compile_hmmsearch_results_to_csv()