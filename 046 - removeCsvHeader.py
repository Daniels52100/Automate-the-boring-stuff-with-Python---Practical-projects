# removeCsvHeader.py - Removes the header from all CSV files in the current
# working directory.

import csv, os
os.chdir('.\\automate_online-materials')
os.makedirs('headerRemoved', exist_ok=True)
# Loop through every file in the current working directory.
for csvFilename in os.listdir('.'):
    if not csvFilename.endswith('.csv'):
        continue    # skip non-csv files
    print('Removing header from ' + csvFilename + '...')
    # Read the CSV file in (skipping first row).
    csvRows = []
    csvFileObj = open(csvFilename)
    readerObj = csv.reader(csvFileObj)
    csvNewFileObj = open(os.path.join('headerRemoved', csvFilename), 'w', newline='')
    csvWriter = csv.writer(csvNewFileObj)
    readerObj = list(readerObj)     # Converting the readerObj to a list allows us to index it.
    for row in readerObj[1:]:       # Setting the index right away
           csvWriter.writerow(row)  # is slightly faster then verifying if
    csvFileObj.close()              # it's the first line on every iteration.
    csvNewFileObj.close()
# Also, saving the row in the iteration we read it saves memory and time.