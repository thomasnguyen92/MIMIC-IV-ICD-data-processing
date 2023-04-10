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
The MIMIC-IV files can be obtained from [this website](https://physionet.org/content/mimiciv/2.2/). You can download it to the physionet.org

Now, make sure your python path includes the base directory of this repository. Then, in Jupyter Notebook, run all cells (in the menu, click Cell -> Run All) in `notebooks/dataproc_mimic_IV_exploration_icd9.ipynb` and `notebooks/dataproc_mimic_IV_exploration_icd10.ipynb`. These will take some time.