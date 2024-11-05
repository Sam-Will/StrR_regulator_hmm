StrR-like regulator HMM model
Sam Williams
06/03/2024

This model is deisgned to identify StrR-like pathway specfic regulators (PSR)
StrR-like are known to regulate several important natural product classes that are used clinically

Including:
GLycopeptides (vancomycin, teicoplanin, balhimycin)
Aminoglycosides (streptomycin, kanamycin)
Aminocyclitols (spectinomycin)
Chloramphenicol

This hmmmodel was created from a list of 83 validated sequences identified in this paper:
The Impact of Heterologous Regulatory Genes from Lipodepsipeptide Biosynthetic Gene Clusters on the Production of Teicoplanin and A40926

Muti header StrR_all_together.fasta

To check the validlity of the model I ran 'leave on out analysis' with the Leave_one_out_analysis.py scipt and results are here master_hmmsearch_results.csv
Scores vary from 467.7 (decaplanin) to 312.8 (pyrazofurin)

Ran model again MiBIG 3.0 database
hmmscan --tblout mibig_3.0_tbl_StrR_test.tbl --cpu 12 --noali --nobias StrR_model.hmm mibig_prot_seqs_3.1.fasta

Results summarised here: mibig_3.0_hmmsearch_results.csv
469.6 (vancomycin) to 318.9	(keratinimicin A) [59 hits]
208.5 (streptonigrin) and 198.1 (cremeomycin) 
16.6 (aldgamycin) to -12.9 (xenovulene A) [29 hits]

