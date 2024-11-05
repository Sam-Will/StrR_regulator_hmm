# StrR-like Regulator HMM Model  
**Author:** Sam Williams  
**Date:** 06/03/2024  

---

## Model Overview

This model is designed to identify **StrR-like pathway-specific regulators (PSR)**. StrR-like regulators are known to play a role in the regulation of several clinically important natural product classes.

### Natural Product Classes Regulated by StrR-like Regulators
- **Glycopeptides**: vancomycin, teicoplanin, balhimycin
- **Aminoglycosides**: streptomycin, kanamycin
- **Aminocyclitols**: spectinomycin
- **Chloramphenicol**

## Model Creation

This HMM model was created from a list of 83 validated sequences, identified in the paper:  
*The Impact of Heterologous Regulatory Genes from Lipodepsipeptide Biosynthetic Gene Clusters on the Production of Teicoplanin and A40926.*

- **File Used:** Multi-header file `StrR_all_together.fasta`

## Model Validation

To check the validity of the model, a "leave-one-out analysis" was performed using the `Leave_one_out_analysis.py` script.  
- **Results File:** `master_hmmsearch_results.csv`
- **Score Range:**  
  - Highest: 467.7 (decaplanin)
  - Lowest: 312.8 (pyrazofurin)

## Application to MiBIG 3.0 Database

The model was applied to the MiBIG 3.0 database using the following command:

```bash
hmmscan --tblout mibig_3.0_tbl_StrR_test.tbl --cpu 12 --noali --nobias StrR_model.hmm mibig_prot_seqs_3.1.fasta
```

- **Summary of Results:**  
  - **High-Scoring Hits**:  
    - Highest: 469.6 (vancomycin)
  - **Low-Scoring Hits Examples**:  
    - Lowest: -12.9 (xenovulene A)
    - Low cut off: 207.7 (streptonigrin) 

**Suggested Cut-off based on bimodal distribution is 195**

- **Results File:** `mibig_3.0_hmmsearch_results.csv`