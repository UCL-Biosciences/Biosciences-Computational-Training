"""Load a mole-rat activity matrix and save summary stats to file.

Uses only what is taught in W1

Input : comma-separated matrix, no header, rows = animals, columns = days/sessions
Output: written to the current working directory
        - activity_mean_per_day.csv
        - activity_mean_per_animal.csv

Usage:
    python activity_stats.py                                   # uses the default path below
"""

import numpy

### change this file to run the code for a different dataset
filename = 'data/molerat_activity_v1.csv'

# --- data in ---
data = numpy.loadtxt(fname=filename, delimiter=',')
print('Loaded', filename, 'with shape', data.shape, '(animals, days)')

# --- stats ---
mean_per_day = numpy.mean(data, axis=0)      # one value per day (column)
mean_per_animal = numpy.mean(data, axis=1)   # one value per animal (row)

numpy.savetxt('activity_mean_per_day.csv', mean_per_day, delimiter=',')
numpy.savetxt('activity_mean_per_animal.csv', mean_per_animal, delimiter=',')

print('Saved 2 stats files')
