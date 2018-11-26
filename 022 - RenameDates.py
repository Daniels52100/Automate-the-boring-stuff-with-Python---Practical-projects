# This program renames files with european DD-MM-YYYY date format
# to American MM-DD-YYYY

import shutil, os, re

# The regex can be adapted from the program proposed in the book,
# by changing day and month lines.
datePattern = re.compile(r"""
    ^(.*?)          # text before the date
    (([0-3])?\d)-|/ # 1 or 2 digits for day
    ((0|1)?\d)-|/   # 1 or 2 digits for month
    ((19|20)\d\d)   # 4 digits for year
    (.*?)$          # text after date
    """, re.VERBOSE)

# Loop over the files in the working directory.
for euroFilename in os.listdir('.'):
    mo = datePattern.search(euroFilename)
    # Skip files without a date.
    if mo == None: continue
    # Get different parts of the filename.
    beforePart = mo.group(1)
    dayPart    = mo.group(2)
    monthPart  = mo.group(4)
    yearPart   = mo.group(6)
    afterPart  = mo.group(8)
    # Form the American-style filename.
    amerFilename = beforePart + monthPart + '-' + dayPart + '-' + yearPart + afterPart
    # Get the full, absolute file paths.
    absWorkingDir = os.path.abspath('.')
    amerFilename = os.path.join(absWorkingDir, amerFilename)
    euroFilename = os.path.join(absWorkingDir, euroFilename)
    # Rename the files.
    print('Renaming %s to %s...' % (euroFilename, amerFilename))
    #shutil.move(euroFilename, amerFilename) # uncomment after testing