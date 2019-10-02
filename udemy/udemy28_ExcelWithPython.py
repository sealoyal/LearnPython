# Now we'll learn how to work with excel files
# IMPORTANT NOTE: NEED TO HAVE xlrd AND openpyxl INSTALLED!!!

import pandas as pd

# Open the excel file as an object
xlsfile = pd.ExcelFile('data/Lec_28_test.xlsx')

# Parse the first sheet of the excel file and set as DataFrame
dframe = xlsfile.parse('Sheet1')

#Show!
dframe

#Now we know how to open various file types! Great!
#Next well learn about various DataFrame Techniques!