import csv
import datetime
import json
from pprint import pprint

LIAM_CSV = 'Purcell,Washington,Vancouver,1990-Dec-25,"programming in Python baby!"'

# Dictionary in Python - Goal: make the csv look like this to make data more useablecle
LIAM = {
  "surname": "Purcell",
  "state": "Washington",
  "city": "Vancouver",
  "dob": "1990-Dec-25",
  "hobbies": "programming in Python baby!"
}

liam_json = json.dumps(LIAM)



# using the laureates.csv that is included in this filepath
with open("laureates.csv","r") as f:
  readfile = csv.DictReader(f)
  friends = list(readfile)

#print everything
# for friend in friends:
#   pprint(friend)

#print specifics
for friend in friends:
  if friend["surname"] == "Einstein":
    pprint(friend)
