from time import process_time

#### Import and read 'Treasure Island' ###
file = open("treasure.txt")
s = file.read()
file.close()

### Make a list of the book's words ###
originalTextlst = s.split()

### Print the length of the book ###
print(f"Treasure Island is {len(originalTextlst)} words long")

### Process the highest freq word and note time ###
t0 = process_time()                                 # get start time
wordSet = set(originalTextlst)                      # create set of all unique words
mfw = max(wordSet, key=originalTextlst.count)       # Iterate through wordSet counting umber of occurances in OGTextlst
ProcessTime = process_time() - t0

### Print Final Results ###
print(f"Most frequent word is '{mfw}' found {originalTextlst.count(mfw)} times")
print(f"Took {ProcessTime} seconds to process")