import numpy as np
from pandas import Series, DataFrame
import pandas as pd

# Heres an example of what a JSON (JavaScript Object Notation) looks like:
json_obj = """
{   "zoo_animal": "Lion",
    "food": ["Meat", "Veggies", "Honey"],
    "fur": "Golden",
    "clothes": null, 
    "diet": [{"zoo_animal": "Gazelle", "food":"grass", "fur": "Brown"}]
}
"""

#Let import json module
import json

#Lets load json data
data = json.loads(json_obj)

#Show
data

#We can also convert back to JSON
json.dumps(data)

#We can simply open JSON data after loading with a DataFrame
dframe = DataFrame(data['diet'])

# Theres lost of custom selection you can do, based on what you do or dont want in your DataFrame (you can specify columns..etc)

#Next up, XML and HTML file format with python!