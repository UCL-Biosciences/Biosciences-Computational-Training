## UCL Computer Science Cluster 
The Computer Science Department at UCL runs an in-house HPC facility providing high performance compute, GPU and storage capability, and technical expertise to the wider UCL community and beyond.

The HPC Cluster team provides a wealth of experience going back several decades, with expertise in various scientific domains, such as Astrophysics, Bioinformatics, Machine Learning Optimisation, and Electrical Engineering. In addition to offering efficient infrastructure, we offer regular HPC training and dynamic technical support. The CS cluster is funded by it users through research grant income.

With over 1000 compute nodes, 300k+ GPU cores, 10+ PB of disk, and 10PB of tape capacity we provide a mid-sized, efficient, and focused HPC and storage service.

<img width="750" height="111" alt="image" src="https://github.com/user-attachments/assets/6f48dcbc-44f5-4c76-b716-49eab842ac4e" />


## Visual Studio Code Setup
VSC can log in to HPCs, allowing you to browse files, edit code and run commands within the interface. This provides an alternative to connecting to the cluster through a terminal session, and subsequently editing files with text editors such as nano and vi.

To set-up VSC with the CS cluster,  

## Logging in and setting up a directory
First, we will log in following these [instructions](https://github-pages.arc.ucl.ac.uk/hpc-intro/11-connecting/index.html) and [have a look around](https://github-pages.arc.ucl.ac.uk/hpc-intro/12-cluster/index.html). Make a project folder and move to it:

```
mkdir my_project_dir
cd my_project_dir
```

## Clone your git repository
Then clone your repository: `git clone https://github.com/YOUR-REPO-PATH` (remember to change the path to your repository) to get your code onto the HPC.

Why wouldn't we just copy over the relevant files??

## Load shared software 
We will discuss how programmes are setup on HPCs via path

**CS TO ADD: instructions for loading programmes by adding them to $PATH ✅**
```
PATH=/share/apps/python3.10.0-sharedplus/bin:$PATH
LD_LIBRARY_PATH=/share/apps/python3.10.0-sharedplus/bin:$LD_LIBRARY_PATH
```


## make an environment using venv
We will use venv to create an environment that matches the one we set up locally:

```
#venv creation - Only do this once!
# Will add after testing on cluster
```

```
#venv loading - Do this at the start of each script!
# Will add after testing on cluster
```


```
# load conda
conda  env create -f path/to/requirements.yml
conda activate carpentries
```
### Copy in some data

**CS TO DO: confirm preference for data. see Issue #6 for more info**

Use the data from the repo OR Find the RDSS file location and copy some data to a data folder:

```
mkdir -p data/input
cp /PATH/TO/RDSS/PROJECT data/input
```

Now you should have all the code, libraries and data needed to run your analysis on the HPC!
