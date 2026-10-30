# Running Jobs on HPCs

We use HPCs to run our code on powerful computers. We do this by writing job scripts and submitting them to the HPC queue, which then sends them to the powerful computers.

First we will have a quick look at HPC nodes and the difference between login and compute nodes.

Then we will look at job scripts, which is how we tell the cluster what we want to do.

## Creating .py script

Now, we will submit the python code we wrote in week 1 as a job.
First, convert the notebook to a python file:
- Install the Visual Studio Code Jupyter extension. Makes it easier to work with Jupyter notebooks, including providing easy option to convert notebooks to scripts (or PDFs or htmls). Open the extensions tab (via the icon on the panel on the left or press `Ctrl/Command + Shift + X`). Search for "Jupyter" and install it.
- Open the notebook (`.ipynb`) file you want to run as a job. At the top, under the file tabs, it says "+ Code + Markdown | Outline ...". Click on the `...` > `Export` > `Python Script`. Save the python script.
- Don't forget to add the python script to your github repo - use the VSC github extension to add, commit and push the `.py` file!

Have a look at the python (`.py`) file - how is it different to the notebook? Why would these differences be needed in order to submit the code as a job on an HPC?

File paths will be different on the HPC. Go through the python script and make sure the file paths are correct. We do this in the terminal using `pwd`, `ls` and `cd`. 

To run the python script (`.py`) from within the job script (`.sh`), we add this to your job script. Open the file in Visual Studio Code or use `nano /path/to/script.sh` from the command line:

## HPC Cluster Architecture
A HPC cluster contains three main entities:

### Log-in Node
The log-in node is the front-end computer through which users access and interact with the HPC cluster. This is where you arrive after connecting via SSH.

As the log-in node is shared by multiple users, only lightweight tasks are permitted. These include:

- Editing and compiling code
- Transferring data
- Submitting and monitoring jobs

Computationally intensive tasks should not be run on the log-in node, as they can affect the experience of other users.

### Compute Nodes
Compute nodes provide the processing power required to execute computationally intensive workloads.

Unlike log-in nodes, compute nodes are not typically accessed directly via SSH. Instead, users submit a **job script** (see below) which requests computational resources through the job scheduler that allocates access to the appropriate compute nodes.

### Job Scheduler
As compute nodes are shared among multiple users, access to their computational resources must be managed to ensure fair and efficient utilisation.

Rather than running computationally intensive tasks directly, users submit jobs to the scheduler, typically through a **job script** specifying the resources required (e.g., number of CPUs, memory, and execution time).

The scheduler manages the allocation of computational resources across the cluster, considering factors such as resource availability and scheduling policies.

When sufficient resources become available, the scheduler allocates the requested resources and starts the job on the appropriate compute node(s).

If the requested resources are not immediately available, the job remains in a queue until it can be scheduled. Larger resource requests may experience longer waiting times, depending on cluster utilisation and scheduling policies.

<img width="322" height="264" alt="image" src="https://github.com/user-attachments/assets/e4f14f92-6985-46d9-ae2c-be1ad8ce674f" />

## Job Scripts

```
# MEMORY AND RESOURCES
#$ -l tmem=152M
#$ -l h_vmem=152M
#$ -l h_rt=00:15:00

# OTHER
#$ -S /bin/bash
#$ -j y
#$ -o logs/
#$ -N test-python
#$ -cwd
#------------
echo "Running on host: $(hostname)"
echo "Start time: $(date)"
echo "Job ID: $JOB_ID"

PATH=/share/apps/python3.10.0-sharedplus/bin:$PATH
LD_LIBRARY_PATH=/share/apps/python3.10.0-sharedplus/lib:$LD_LIBRARY_PATH

source path/to/venv/bin/activate

python3 file.py

echo "End Time: $(date)"

```

Save and close the file and submit it: `qsub /path/to/script.sh`. Some things to check on its progress:
- `qstat` tells you the status of all your jobs, including their unique job IDs
- You can use the job ID to find its output. By default it will be `test-python.o${JOB_ID}` and will be saved in the folder you were in when you submitted the job.

Finally, download the output and check it on your local computer. You can download it in Visual Studio Code by right-clicking on a file and selecting `Download` - simples!
