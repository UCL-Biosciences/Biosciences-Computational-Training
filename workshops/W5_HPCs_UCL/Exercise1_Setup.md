## UCL Computer Science Cluster 

The Department of Computer Science at UCL operates an in-house High-Performance Computing (HPC) and virtualization facility, delivering high-throughput compute, GPU acceleration, dedicated virtual machines (VMs), large-scale storage, and technical expertise to the wider UCL community and external partners.

Backed by over 1,000 compute nodes, 100+ GPU accelerators, 10+ PB of disk storage, and deep tape archival capacity, alongside a flexible VM provisioning environment, we deliver an efficient, focused, mid-scale infrastructure service.

Our engineering team brings decades of combined experience across diverse research domains including astrophysics, bioinformatics, machine learning optimisation, and electrical engineering. Alongside infrastructure, we provide regular training programmes and responsive technical support. The facility operates on a cost-recovery model, funded directly by its users through research grants.

<img width="750" height="111" alt="image" src="https://github.com/user-attachments/assets/6f48dcbc-44f5-4c76-b716-49eab842ac4e" />

## Logging in
First, we will log in to the cluster using the [ssh](https://man7.org/linux/man-pages/man1/ssh.1.html) command. Open a Terminal (Mac) or Git Bash (Windows) shell.

```
#First, log in to a gateway node to enter the CS network. Remember to use your CS username, rather than your centralized UCL username!
#knuckles for taught students
#tails for PhD students or staff
ssh compSciUsername@tails.cs.ucl.ac.uk

#Then, log in to the Biosciences log-in node
ssh compSciUsername@pchuckle.cs.ucl.ac.uk
```
This takes you to a login node on the pchuckle cluster. We will talk about what that means later.

## Setting up a directory

Make a project folder in your home directory, and move into it. In your terminal window, type:
```
mkdir my_project_dir
```
You can check the it was made using `ls`, which will show all folders and files in your current "working directory". 

> **A note on working directories**. When you open a programme for looking at files (e.g. File Explorer on Windows), it opens you to a specific folder. From there, you can see all the files and folders it contains. You can click on a file to open it or click on a folder to show the contents on that folder, and the path at the top of the viewer will change. Command lines have a similar concept, where your current "location" is called a working directory. When you open a terminal, the session starts in a place (same as File Explorer) and you can only view files/folders from that directory.

## Navigating from working directories
There are a few essential things to know about navigating file systems using the command line. For starters:

```
# to see where you are (what your current working directory is)
pwd # print working directory

# to see what your current working directory contains
ls # list

# to change directory
cd my_project_dir # change directory to my_project_dir

```

This is how you can access an HPC from the command line and start some simple activities.

## Visual Studio Code Setup
Visual Studio Code offers a more intuitive way of navigating file systems, as we have seen in previous weeks. VSC can also log in to HPCs, allowing you to browse files, edit code and run commands within the interface. This provides an alternative to connecting to the cluster through a terminal session, and subsequently editing files with text editors such as nano and vim.

### Setting up VSC
#### Older versions of VSC (<= 1.9.8)
Older versions of VSC, specifically 1.9.8 or below can integrate with the cluster through the following [instructions](https://hpc.cs.ucl.ac.uk/software/index.html).

#### New versions of VSC (>1.9.8)
It is possible to use more recent versions of VSC, however this requires further tweaking to your local environment through the following [walkthrough](https://github.com/UCL-Biosciences/Biosciences-Computational-Training/blob/jayChanges/workshops/W5_HPCs_UCL/VSCodeWalkthrough.md).

## Clone your git repository
In Visual Studio Code, you can clone repositories by clicking on the `Source Control` extension, click `Clone Repository` > `Clone from Github`. This should show you a list of github repositories you can clone. If it doesn't, you might not be logged into Github in VSC. Log in by clicking the accounts button (bottom left of VSC, a head and shoulders icon in a circle, above the gear/settings sign) and logging into github.

> Command line equivalent: clone your repository: `git clone https://github.com/YOUR-REPO-PATH` (remember to change the path to your repository)

Why wouldn't we just copy over the relevant files??

## Load shared software 
- CS Cluster offers a wealth of software, which can be found in /share/apps
- This also includes specialized software for bioinformatics, which can be found in /share/apps/genomics

To use installed software, you need to configure two Linux environment variables: **PATH** and **LD_LIBRARY_PATH**.

- **PATH**: Tells Linux where to look for executable programs when you type a command. By adding a software installation's binary (bin) directory to PATH, you can run its commands without specifying their full file paths.

- **LD_LIBRARY_PATH**: Tells the dynamic linker where to look for shared libraries (.so files) required by a program when it starts. In other words, some software depends on libraries installed outside the standard system directories, so their locations must be specified.
  
Below is an example of loading Python version 3.10.0:

```
PATH=/share/apps/python3.10.0-sharedplus/bin:$PATH
LD_LIBRARY_PATH=/share/apps/python3.10.0-sharedplus/lib:$LD_LIBRARY_PATH
```


## Setting up Python environments with venv
We recommend using Python's built-in venv functionality to create lightweight, isolated environments for your projects. These environments are straightforward to manage and help minimise unnecessary overhead on shared HPC infrastructure.

Alternative environment managers, such as Conda, can introduce additional challenges in an HPC environment, particularly due to their storage requirements, large numbers of small files, and filesystem metadata operations. When used extensively across many users, these can place additional pressure on shared storage systems and affect overall performance.

### Setting up a venv
```
# When downloading packages, run a more recent GCC toolchain to support compilation
scl enable devtoolset-11 bash
# Load the version of Python you wish to use
PATH=/share/apps/python3.10.0-sharedplus/bin:$PATH
LD_LIBRARY_PATH=/share/apps/python3.10.0-sharedplus/lib:$LD_LIBRARY_PATH
# Create the venv
python3 -m venv moleRatvenv
# Activate this new venv
source moleRatvenv/bin/activate
# Within the venv, use pip to install required packaes
pip install numpy
pip install matplotlib # if you get a pillow error, try running this first: pip install --no-binary=:all: pillow
# Once finished, get out of the venv
deactivate
```

### Running a pre-existing venv
```
# Importantly, run this at the start of your script if you wish to use the venv
PATH=/share/apps/python3.10.0-sharedplus/bin:$PATH
LD_LIBRARY_PATH=/share/apps/python3.10.0-sharedplus/lib:$LD_LIBRARY_PATH
source moleRatvenv/bin/activate
```

### Copying input data
```
#Run this on your LOCAL device
scp /path/to/your/data jschneid@pchuckle:/home/csUserName/path/you/want
```

Now you should have all the code, libraries and data needed to run your analysis on the HPC!
