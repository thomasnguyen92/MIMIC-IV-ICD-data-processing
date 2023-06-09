# Mimic-IV-ICD: A new benchmark for eXtreme MultiLabel Classification

Official source code repository for [Mimic-IV-ICD: A new benchmark for eXtreme MultiLabel Classification](https://arxiv.org/abs/2304.13998)

```bibtex
@misc{nguyen2023mimicivicd,
      title={Mimic-IV-ICD: A new benchmark for eXtreme MultiLabel Classification}, 
      author={Thanh-Tung Nguyen and Viktor Schlegel and Abhinav Kashyap and Stefan Winkler and Shao-Syuan Huang and Jie-Jyun Liu and Chih-Jen Lin},
      year={2023},
      eprint={2304.13998},
      archivePrefix={arXiv},
      primaryClass={cs.AI}
}
```

## Introduction

Medical coding is an important operation within the healthcare industry’s revenue cycle management process, critical to the care of patients, efficiency of payments, and integrity of operations. 
This paper proposes a public benchmark suite for ICD-10 coding using a large EHR dataset derived from MIMIC-IV, the most recent public EHR dataset. Moreover, we also create a new ICD-9 benchmark using MIMIC-IV data, providing more data points and a higher number of ICD codes than MIMIC-III. Our open-source code offers easy access to data processing steps, benchmark creation, and experiment replication for those with MIMIC-IV access, providing insights, guidance, and protocols to efficiently develop ICD coding models.

The subsequent tables list the models currently included in our benchmark. As we continuously seek to enhance this benchmark, new models will be regularly integrated. 
We cordially invite individuals wishing to incorporate their model into our benchmark to get in touch with us.

| Model | Paper | Original Code | Our Adaptation|
| ----- | ----- | ------------- | --------------|
| CAML  |[Explainable Prediction of Medical Codes from Clinical Text](https://aclanthology.org/N18-1100/) | [link](https://github.com/jamesmullenbach/caml-mimic) |
| LAAT  | [A Label Attention Model for ICD Coding from Clinical Text](https://www.ijcai.org/proceedings/2020/461) | [link](https://github.com/aehrc/LAAT) |
| MSMN  | [Code Synonyms Do Matter: Multiple Synonyms Matching Network for Automatic ICD Coding](https://aclanthology.org/2022.acl-short.91) | [link](https://github.com/GanjinZero/ICD-MSMN)
| PLM-ICD | [PLM-ICD: Automatic ICD Coding with Pretrained Language Models](https://aclanthology.org/2022.clinicalnlp-1.2/) | [link](https://github.com/MiuLab/PLM-ICD) |


## Data processing

Our directory has the following structure:
```
mimicdata
└───physionet.org/
|   |files/
└───mimic4_icd9/
|   |   ALL_CODES.csv
|   |   ALL_CODES_filtered.csv
|   |   disch_9_full.csv
|   |   disch_9_filtered.csv
|   |   notes_labeled.csv
|   |   *_hadm_ids.csv (already in repo)
└───mimic4_icd10/
|   |   ALL_CODES.csv
|   |   ALL_CODES_filtered.csv
|   |   disch_10_full.csv
|   |   disch_10_filtered.csv
|   |   notes_labeled.csv
|   |   *_hadm_ids.csv (already in repo)
```
The MIMIC-IV files can be obtained from [this website](https://physionet.org/content/mimiciv/2.2/). You can download it to the directory `mimicdata/physionet.org`

Now, make sure your python path includes the base directory of this repository. Then, in Jupyter Notebook, run all cells (in the menu, click Cell -> Run All) in `notebooks/dataproc_mimic_IV_exploration_icd9.ipynb` and `notebooks/dataproc_mimic_IV_exploration_icd10.ipynb`. These will take some time.
