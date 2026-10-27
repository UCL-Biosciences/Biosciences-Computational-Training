"""Load a mole-rat activity matrix, save summary stats and plots to file.

Uses only what is taught in W1: numpy, matplotlib.pyplot and sys.argv.

Input : comma-separated matrix, no header, rows = animals, columns = days/sessions
Output: written to the current working directory (so it can run unattended as a job)
        - activity_mean_per_day.csv
        - activity_mean_per_animal.csv
        - activity_heatmap.png
        - activity_mean_per_day.png
        - activity_mean_per_animal.png

Usage:
    python activity_stats.py                                   # uses the default path below
    python activity_stats.py data/molerat_activity_v2.csv      # or give a file
"""

import sys

import numpy
import matplotlib.pyplot

DEFAULT_FILE = 'data/molerat_activity_v1.csv'


def main():
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = DEFAULT_FILE

    # --- data in ---
    data = numpy.loadtxt(fname=filename, delimiter=',')
    print('Loaded', filename, 'with shape', data.shape, '(animals, days)')

    # --- stats ---
    mean_per_day = numpy.mean(data, axis=0)      # one value per day (column)
    mean_per_animal = numpy.mean(data, axis=1)   # one value per animal (row)

    numpy.savetxt('activity_mean_per_day.csv', mean_per_day, delimiter=',')
    numpy.savetxt('activity_mean_per_animal.csv', mean_per_animal, delimiter=',')

    # --- figures ---
    # Heat map of the whole matrix
    matplotlib.pyplot.imshow(data, aspect='auto')
    matplotlib.pyplot.xlabel('day')
    matplotlib.pyplot.ylabel('animal')
    matplotlib.pyplot.savefig('activity_heatmap.png')
    matplotlib.pyplot.close()

    # Mean across animals, for each day
    matplotlib.pyplot.plot(mean_per_day)
    matplotlib.pyplot.xlabel('day')
    matplotlib.pyplot.ylabel('mean activity')
    matplotlib.pyplot.savefig('activity_mean_per_day.png')
    matplotlib.pyplot.close()

    # Mean across days, for each animal
    matplotlib.pyplot.plot(mean_per_animal)
    matplotlib.pyplot.xlabel('animal')
    matplotlib.pyplot.ylabel('mean activity')
    matplotlib.pyplot.savefig('activity_mean_per_animal.png')
    matplotlib.pyplot.close()

    print('Saved 2 stats files and 3 figures')


if __name__ == '__main__':
    main()
