# MEMORY AND RESOURCES
#$ -l tmem=256M
#$ -l h_vmem=256M
#$ -l h_rt=00:15:00

# OTHER
#$ -S /bin/bash
#$ -j y
#$ -o logs/
#$ -N test-python
#------------
echo "Running on host: $(hostname)"
echo "Start time: $(date)"
echo "Job ID: $JOB_ID"

PATH=/share/apps/python3.10.0-sharedplus/bin:$PATH
LD_LIBRARY_PATH=/share/apps/python3.10.0-sharedplus/lib:$LD_LIBRARY_PATH

source path/to/venv/bin/activate ## EDIT this so it leads to your project

python3 path/to/your_file.py ## EDIT to make sure the path leads to your python script

echo "End Time: $(date)"
