# Acronym Sorter
# Input: Excel filename without extension
# Output: Excel file
# Comments: file must be in same directory
# Date: June 4th, 2022

# Needed Libraries:
#   Pandas
#   openpyxl

import numpy as np
import pandas as pd

# Obtain file name from user
filename = input('Enter Excel file name: ')
filename = filename + '.xlsx'

# Read excel into data Frame
df = pd.read_excel(filename)

# Sorts dataframe alphabetically by acronym
# assumes there is a column named 'Acronym'
sorted = df.sort_values(by = 'Acronym')

# Writes back to Original File
sorted.to_excel(filename, index= False)
