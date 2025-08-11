import pandas as pd 
import numpy as np
import csv
import string

dataset = pd.read_csv('C:\Emotion Classification\data\\full_dataset\goemotions_1.csv')

with open('C:\Emotion Classification\data\\text.txt', "w", encoding="utf-8") as f:
    for i in range(len(dataset)):
        f.write(dataset["text"][i].lower() + "\n")