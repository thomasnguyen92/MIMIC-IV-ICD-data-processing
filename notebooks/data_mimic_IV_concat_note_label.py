MIMIC_4_DIR='./mimicdata/physionet.org/files/mimiciv/2.2'
MIMIC_4_SAVE_DIR='./mimicdata/mimic4_icd10'
"""
    Concatenate the labels with the notes data and split using the saved splits
"""
import csv
from datetime import datetime
import random


import pandas as pd

DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"

def concat_data(labelsfile, notes_file, output_note_labeled_file):
    """
        INPUTS:
            labelsfile: sorted by hadm id, contains one label per line
            notes_file: sorted by hadm id, contains one note per line
    """
    with open(labelsfile, 'r', encoding='utf-8') as lf:
        print("CONCATENATING")
        with open(notes_file, 'r', encoding='utf-8') as notesfile:
            outfilename = output_note_labeled_file
            with open(outfilename, 'w', encoding='utf-8') as outfile:
                w = csv.writer(outfile)
                w.writerow(['subject_id', 'hadm_id', 'text', 'labels'])

                labels_gen = next_labels(lf)
                notes_gen = next_notes(notesfile)

                for i, (subj_id, text, hadm_id) in enumerate(notes_gen):
                    if i % 10000 == 0:
                        print(str(i) + " done")
                    cur_subj, cur_labels, cur_hadm = next(labels_gen)

                    if cur_hadm == hadm_id:
                        w.writerow([subj_id, str(hadm_id), text, ';'.join(cur_labels)])
                    else:
                        print("couldn't find matching hadm_id. data is probably not sorted correctly")
                        break
                    
    return outfilename

def next_labels(labelsfile):
    """
        Generator for label sets from the label file
    """
    labels_reader = csv.reader(labelsfile)
    #header
    next(labels_reader)

    first_label_line = next(labels_reader)

    cur_subj = int(first_label_line[0])
    cur_hadm = int(first_label_line[1])
    cur_labels = [first_label_line[2]]

    for row in labels_reader:
        subj_id = int(row[0])
        hadm_id = int(row[1])
        code = row[2]
        #keep reading until you hit a new hadm id
        if hadm_id != cur_hadm or subj_id != cur_subj:
            yield cur_subj, cur_labels, cur_hadm
            cur_labels = [code]
            cur_subj = subj_id
            cur_hadm = hadm_id
        else:
            #add to the labels and move on
            cur_labels.append(code)
    yield cur_subj, cur_labels, cur_hadm

def next_notes(notesfile):
    """
        Generator for notes from the notes file
        This will also concatenate discharge summaries and their addenda, which have the same subject and hadm id
    """
    nr = csv.reader(notesfile)
    #header
    next(nr)

    first_note = next(nr)

    cur_subj = int(first_note[0])
    cur_hadm = int(first_note[1])
    cur_text = first_note[3]
    
    for row in nr:
        subj_id = int(row[0])
        hadm_id = int(row[1])
        text = row[3]
        #keep reading until you hit a new hadm id
        if hadm_id != cur_hadm or subj_id != cur_subj:
            yield cur_subj, cur_text, cur_hadm
            cur_text = text
            cur_subj = subj_id
            cur_hadm = hadm_id
        else:
            #concatenate to the discharge summary and move on
            cur_text += " " + text
    yield cur_subj, cur_text, cur_hadm



check=concat_data(
    labelsfile=f'{MIMIC_4_SAVE_DIR}/ALL_CODES_filtered.csv', 
    notes_file=f'{MIMIC_4_SAVE_DIR}/disch_10_filtered.csv', 
    output_note_labeled_file=f'{MIMIC_4_SAVE_DIR}/note_labels_icd10_filtered.csv'
)