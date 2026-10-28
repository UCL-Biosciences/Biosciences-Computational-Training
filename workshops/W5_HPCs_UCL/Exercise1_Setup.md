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

```
#First, log in to a gateway node to enter the CS network. Remember to use your CS username, rather than your centralized UCL username!
ssh compSciUsername@knuckles.cs.ucl.ac.uk

#Then, log in to the Biosciences log-in node
ssh compSciUsername@pchuckle.cs.ucl.ac.uk
```

## Cluster Architecture
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

Unlike log-in nodes, compute nodes are not typically accessed directly via SSH. Instead, users request computational resources through the job scheduler, which allocates access to the appropriate compute nodes.

### Job Scheduler
As compute nodes are shared among multiple users, access to their computational resources must be managed to ensure fair and efficient utilisation.

Rather than running computationally intensive tasks directly, users submit jobs to the scheduler, typically through a **job script** specifying the resources required (e.g., number of CPUs, memory, and execution time).

The scheduler manages the allocation of computational resources across the cluster, considering factors such as resource availability and scheduling policies.

When sufficient resources become available, the scheduler allocates the requested resources and starts the job on the appropriate compute node(s).

If the requested resources are not immediately available, the job remains in a queue until it can be scheduled. Larger resource requests may experience longer waiting times, depending on cluster utilisation and scheduling policies.

<img width="322" height="264" alt="image" src="https://github.com/user-attachments/assets/e4f14f92-6985-46d9-ae2c-be1ad8ce674f" />


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
pip install matplotlib
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

**Currently discussing datasource. scp?**

```

```

Now you should have all the code, libraries and data needed to run your analysis on the HPC!
