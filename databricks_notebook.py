# Databricks notebook source
x = lambda a : a + 10
print(x(5))

# COMMAND ----------

import datetime

x = datetime.datetime.now()
print(x)

# COMMAND ----------

import json

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])

# COMMAND ----------


