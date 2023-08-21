import re
import os
import pandas as pd

def get_names_dict(nf: str = os.getcwd() + "/data/names.txt") -> dict:
    names_file = pd.read_table(nf, header=None, names=["name"] )

    names_dict = names_file.set_index(names_file["name"])["name"].map(lambda x: 0).to_dict()

    with open(r"/Users/rob/PycharmProjects/PythonMasterClass/DictionaryExercise/data/sentences.txt", "r") as file:
        data = file.read()

        lines = data.split()

        for word in lines:
            word_no_punct = re.findall(r"[\w']+|[.,!?;]", word)[0]
            if  word_no_punct in names_dict:
                names_dict[word_no_punct] += 1
            else:
                continue

    return names_dict