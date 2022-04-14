import re
import pandas as pd

names_file = pd.read_table("./DictionaryExercise/data/names.txt", header=None, names=["name"] )

names_dict = names_file.set_index(names_file["name"])["name"].map(lambda x: 0).to_dict()

with open(r"./DictionaryExercise/data/sentences.txt", "r") as file:
    data = file.read()

    lines = data.split()

    for word in lines:
        word_no_punct = re.findall(r"[\w']+|[.,!?;]", word)[0]
        if  word_no_punct in names_dict:
            names_dict[word_no_punct] += 1
        else:
            continue

print(names_dict)