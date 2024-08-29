import csv
from pprint import pprint

EINSTEIN_CSV = 'Albert,Einstein,1879-03-14,1955-04-18,Germany,"for his services to Theoretical Physics, and especially for his discovery of the law of the photoelectric effect",physics,1921'

#hash tables, dictionary, very popular in python
EINSTEIN = {
    "birthplace": "Germany",
    "name": "Albert",
    "surname": "Einstein",
    "born": "1879-03-14",
    "category": "physics",
    "motivation": "for his services to Theoretical Physics...",
}
# use with keyword will not leave the file open any longer than necessary - 
with open("laureates.csv", "r") as f:  #"r" denotes read mode
    reader = csv.DictReader(f)
    laureates = list(reader)

for laureate in laureates:
    if laureate["surname"] == "Einstein":
        pprint(laureate)
        break
