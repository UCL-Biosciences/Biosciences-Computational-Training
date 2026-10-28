## UCL Computer Science Cluster 

The Department of Computer Science at UCL operates an in-house High-Performance Computing (HPC) and virtualization facility, delivering high-throughput compute, GPU acceleration, dedicated virtual machines (VMs), large-scale storage, and technical expertise to the wider UCL community and external partners.

Backed by over 1,000 compute nodes, 100+ GPU accelerators, 10+ PB of disk storage, and deep tape archival capacity, alongside a flexible VM provisioning environment, we deliver an efficient, focused, mid-scale infrastructure service.

Our engineering team brings decades of combined experience across diverse research domains including astrophysics, bioinformatics, machine learning optimisation, and electrical engineering. Alongside infrastructure, we provide regular training programmes and responsive technical support. The facility operates on a cost-recovery model, funded directly by its users through research grants.

<img width="750" height="111" alt="image" src="https://github.com/user-attachments/assets/6f48dcbc-44f5-4c76-b716-49eab842ac4e" />


## Visual Studio Code Setup
VSC can log in to HPCs, allowing you to browse files, edit code and run commands within the interface. This provides an alternative to connecting to the cluster through a terminal session, and subsequently editing files with text editors such as nano and vi.

Older versions of VSC, specifically 1.9.8 or below can integrate with the cluster through the following [instructions](https://hpc.cs.ucl.ac.uk/software/index.html). it is possible to use more recent versions of VSC, however, this requires further tweaking to your local environment through the following [walkthrough]().


## Logging in
First, we will log in to the cluster using the [ssh](https://man7.org/linux/man-pages/man1/ssh.1.html) command.


## Cluster Architecture
- Compute nodes, log-in nodes
- Home directory
- Project storage directory


## Setting up a directory

Make a project folder in your home directory, and move into it:
```
mkdir my_project_dir
cd my_project_dir
```

## Clone your git repository
Then clone your repository: `git clone https://github.com/YOUR-REPO-PATH` (remember to change the path to your repository) to get your code onto the HPC.

Why wouldn't we just copy over the relevant files??

## Load shared software 
- CS Cluster offers a wealth of software, which can be found in /share/apps including:
-   Common programming languages, eg. Python and R
-   Specialized software, eg. Nextflow, and a directory of other tools in /share/apps/genomics

To use a software, two commands are required, which sets your PATH and LD_LIBRARY_PATH variable.
- PATH =
- LD_LIBRARY_PATH=

In this example, we are loading version 3.10.0 of Python:

```
PATH=/share/apps/python3.10.0-sharedplus/bin:$PATH
LD_LIBRARY_PATH=/share/apps/python3.10.0-sharedplus/bin:$LD_LIBRARY_PATH
```


## Setting up Python environments with venv
venv provides a lightweight which can be used across a large amount of infrastructure sustainably. Other offerings such as conda, are problematic due to _, our aim is to keep operations as efficient as possible, to ensure everyone is using an efficient HPC ecosystem!

```
#venv creation - Only do this once!
# Will add after testing on cluster
```

```
#venv loading - Do this at the start of each script!
# Will add after testing on cluster
```

### Copying input data

**Currently discussing datasource. scp?**

```
mkdir -p data/input
cp /PATH/TO/RDSS/PROJECT data/input
```

Now you should have all the code, libraries and data needed to run your analysis on the HPC!
