import os
import subprocess
from Bio import SeqIO

def run_mafft(input_file, output_file):
    cmd = f"mafft --auto {input_file} > {output_file}"
    subprocess.run(cmd, shell=True, check=True)

def run_hmmbuild(input_file, output_file):
    cmd = f"hmmbuild {output_file} {input_file}"
    subprocess.run(cmd, shell=True, check=True)

def run_hmmsearch(hmm_file, query_file, output_file):
    cmd = f"hmmsearch --tblout {output_file} {hmm_file} {query_file}"
    subprocess.run(cmd, shell=True, check=True)

def main():
    fasta_file = "StrR_all_together.fasta"
    sequences = list(SeqIO.parse(fasta_file, "fasta"))

    for i, seq in enumerate(sequences):
        # Create a temporary FASTA file excluding the current sequence
        temp_fasta = f"temp_{i}.fasta"
        with open(temp_fasta, "w") as out:
            for j, other_seq in enumerate(sequences):
                if i != j:
                    SeqIO.write(other_seq, out, "fasta")

        # Align sequences
        aligned_fasta = f"aligned_{i}.fasta"
        run_mafft(temp_fasta, aligned_fasta)

        # Build HMM model
        hmm_model = f"model_{i}.hmm"
        run_hmmbuild(aligned_fasta, hmm_model)

        # Search the left-out sequence against the HMM model
        search_output = f"hmmsearch_results_{i}.txt"
        with open(f"leftout_{i}.fasta", "w") as out:
            SeqIO.write(seq, out, "fasta")
        run_hmmsearch(hmm_model, f"leftout_{i}.fasta", search_output)

        # Clean up temporary files
        os.remove(temp_fasta)
        os.remove(aligned_fasta)

        print(f"Completed iteration {i+1}/{len(sequences)}")

    print("Leave-one-out analysis completed.")

if __name__ == "__main__":
    main()
