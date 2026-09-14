# High Performance Compute at UCL
Last week, we applied machine learning to our data and found that it was very slow to run the full analysis on our laptops. Some analyses require too much compute to run on our "local" computers. UCL has a number of High Performance Compute (HPC) clusters that we can use when we need more compute power. Today we will look at how we can run some of our analyses on UCL HPCs.

## Learning objectives

By the end of this session, participants will be able to:
- Explain what problem an HPC solves and when it is (and isn't) the right tool
- Connect to the cluster and navigate the filesystem from the command line
- Move a project onto the cluster by cloning a GitHub repository
- Build a working environment on the cluster from a Conda export
- Bring data onto the cluster
- Write and submit an SGE batch job, and monitor it in the queue
- Retrieve results back to their own machine

## Session plan (3 hours)

| Activity | Time |
|----------|------|
| Why HPC? | 15 min |
| Log in | 20 min |
| Get your code (github) onto the cluster | 10 min |
| Break | 10 min |
| Build your environment | 10 min |
| Transfer data  | 20 min |
| Jobs | 45 min |
| Break | 10 min |
| Download results to your computer | 10 min |
| wrap-up | 10 min |

## Intro activity — why use HPCs?
HPCs are important when we need more compute power. Let's see if any of the participants have run into power problems: menti quiz. [Link] and QR code:

Have you ever had these problems?
- You start a programme or hit run and your laptop is slow/unusable until it has finished
- Started a big job (e.g. doing analysis, downloading data), only to find the computer turned off before you finished and you have to start again
- Dataset too big and won't even load
- You need to run the same analysis across 200 samples and have to do it one at a time

HPCs address some of these problems:
- bigger computers
- jobs run independently so you can walk away or turn off your laptop
- laptop memory isn't needed for big processes so you can use it normally

## Exercises overview

**Exercise 1 — cluster setup** [First](https://github.com/UCL-Biosciences/Biosciences-Computational-Training/blob/prep-2026/workshops/W5_HPCs_UCL/Exercise1_Setup.md) we will get ourselves onto the cluster and set up everything we need - code, environment and data.

**Exercise 2 — Submit a job.** Now we will look at [HPC nodes](https://github-pages.arc.ucl.ac.uk/hpc-intro/12-cluster/index.html#nodes) and the difference between login and compute nodes.

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

## Summary
That's a lot of content! We talked about when and why we use HPCs. We set up HPC access via VSC, including cloning the github repo and copying data to the cluster. We made an environment that we can use to run code then submitted our python script as a job, before downloading the results back to our computer to review, share with colleagues etc.







