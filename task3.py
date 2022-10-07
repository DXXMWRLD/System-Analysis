import csv
import sys
from io import StringIO

def task(csv_str):

    f = StringIO(csv_str)
    reader = csv.reader(f, delimiter=',')
    data_list = list(reader)

    r1 = list()
    r2 = list()
    r3 = list()
    r4 = list()
    r5 = list()

    for data in data_list:
        r1.append(data)
        r2.append(data[::-1])
        for data_ in [temp for temp in data_list if temp != data]:
            if data[1] == data_[0]:
                r3.append([data[0], data_[1]])
                r4.append([data_[1], data[0]])
            elif data[0] == data_[0]:
                r5.append([data[1], data_[1]])

    classification_list = list()
    classification_list.append(r1)
    classification_list.append(r2)
    classification_list.append(r3)
    classification_list.append(r4)
    classification_list.append(r5)

    out = []
    for classification in classification_list:
      out.append([])
      for pair in classification:
        out[-1].append(int(pair[0]))
      out[-1] = list(set(out[-1]))
    return out
