import glob
import re

def process_line(line):
    # Replace multiple spaces with a single comma
    return re.sub(' +', ',', line.strip()) + '\n'

def compile_hmmsearch_results_to_csv():
    result_files = sorted(glob.glob('hmmsearch_results_*.txt'))
    csv_file = 'master_hmmsearch_results.csv'

    with open(csv_file, 'w') as csv:
        for i, file in enumerate(result_files):
            with open(file, 'r') as f:
                lines = f.readlines()
                # For the first file, take the first four lines and process them
                if i == 0:
                    for line in lines[:4]:
                        csv.write(process_line(line))
                # For subsequent files, take the fourth line and process it
                if len(lines) >= 4:
                    csv.write(process_line(lines[3]))

    print(f"CSV file created: {csv_file}")

if __name__ == "__main__":
    compile_hmmsearch_results_to_csv()
