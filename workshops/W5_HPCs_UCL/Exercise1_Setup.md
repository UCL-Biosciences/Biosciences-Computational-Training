## Visual Studio Code Setup
VSC can log in to HPCs, allowing you to browse files, edit code and run commands within the nice interface. It is a good solution and avoids some problems like using more awkward text-editors (e.g. nano and vim) and moving files between the HPC and your machine.

**CS TO DO: add some steps for setting up VSC HPC login - most people will be using new versions of VSC that will need a workaround for the glib library incompatibility issue**

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

**CS TO ADD: instructions for loading programmes by adding them to $PATH**

## make an environment using venv
We will use venv to create an environment that matches the one we set up locally:

**CS TO DO: add preferred venv instructions**

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
