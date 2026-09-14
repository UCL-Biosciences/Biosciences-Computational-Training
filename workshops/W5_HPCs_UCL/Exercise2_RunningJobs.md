# Running Jobs on HPCs

We use HPCs to run our code on powerful computers. We do this by writing job scripts and submitting them to the HPC queue, which then sends them to the powerful computers.

First we will have a quick look at [HPC nodes](https://github-pages.arc.ucl.ac.uk/hpc-intro/12-cluster/index.html#nodes) and the difference between login and compute nodes.

Then we will look at [job scripts](https://github-pages.arc.ucl.ac.uk/hpc-intro/13-scheduler/index.html), which is how we tell the cluster what we want to do.

Now, we will submit the python code we wrote in week 1 as a job.
First, convert the notebook to a python file:
- Install the Visual Studio Code Jupyter extension. Makes it easier to work with Jupyter notebooks, including providing easy option to convert notebooks to scripts (or PDFs or htmls). Open the extensions tab (via the icon on the panel on the left or press `Ctrl/Command + Shift + X`). Search for "Jupyter" and install it.
- Open the notebook (`.ipynb`) file you want to run as a job. At the top, under the file tabs, it says "+ Code + Markdown | Outline ...". Click on the `...` > `Export` > `Python Script`. Save the python script.
- Don't forget to add the python script to your github repo - use the VSC github extension to add, commit and push the `.py` file!

Have a look at the python (`.py`) file - how is it different to the notebook? Why would these differences be needed in order to submit the code as a job on an HPC?

File paths will be different on the HPC. Go through the python script and make sure the file paths are correct. We do this in the terminal using `pwd`, `ls` and `cd`. 

To run the python script (`.py`) from within the job script (`.sh`), we add this to your job script. Open the file in Visual Studio Code or use `nano /path/to/script.sh` from the command line:

**CS TO DO: add job script example**


```
#!/bin/bash -l
#$ -N test-python
## load modules


## activate your environment

## run the code
python /path/to/your_script.py # remember to change the path
```

Save and close the file and submit it: `pwd && qsub /path/to/script.sh`. Some things to check on its progress:
- `qstat` tells you the status of all your jobs, including their unique job IDs
- You can use the job ID to find its output. By default it will be `test-python.o${JOB_ID}` and will be saved in the folder you were in when you submitted the job.

Finally, download the output and check it on your local computer. You can download it in Visual Studio Code by right-clicking on a file and selecting `Download` - simples!
