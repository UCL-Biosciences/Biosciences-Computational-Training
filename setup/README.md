# Training setup

There are a few things to set up before the training. All are widely used tools and will continue to be useful beyond the training series.

We don't schedule time for troubleshooting setup problems. Please ensure you complete them in advance and get in touch if you have any problems.

## 1. Install Python
 
Download it from [python.org/downloads](https://www.python.org/downloads/). **On Windows, tick "Add python.exe to PATH" on the first screen of the installer.**

## 2. Install Git
 
- **Windows:** install [Git for Windows](https://gitforwindows.org/) and accept the default options. This also installs **Git Bash**, which we use as the terminal.
- **Mac:** open Terminal and run `git --version`. If git isn't installed, macOS will offer to install it. Accept.
 
## 3. Install Visual Studio Code
 
1. For week five, it is better to have an older version of Visual Studio Code that is compatible with the HPC system. Download version 1.98 (or below) from [here](https://code.visualstudio.com/updates/v1_98).
2. Open it and go to the Extensions tab (`Ctrl/Cmd + Shift + X`). Search for and install:
   - **Python** (Microsoft)
   - **Jupyter** (Microsoft)

## 4. Create your course folder and software environment
 
An environment is a separate set of Python packages for one project - we discuss this in week 3. We will use `venv`, which comes with Python. Name it exactly `carpentries`: in Week 1 you will select the "carpentries" environment as your kernel.
 
1. In VS Code, choose `File` > `Open Folder`, make a new empty folder called e.g. `biosciences-training`, and open it. **We will keep using this folder throughout the course.**
2. Open a terminal: `Terminal` > `New Terminal`. **On Windows, make sure it is Git Bash**: click the small down arrow next to the `+` at the top right of the terminal panel and choose *Git Bash*. (If it already says bash or git bash, carry on.)
3. Create the environment (use `python3` instead of `python` on Mac/Linux if `python` isn't found):
```
python -m venv carpentries
```
 
4. Activate it:
   - Mac/Linux: `source carpentries/bin/activate`
   - Windows (Git Bash): `source carpentries/Scripts/activate`
   You should see `(carpentries)` at the start of your terminal line.
5. Download [`requirements.txt`](/setup/requirements.txt) and move it into your course folder. It lists the packages we need.
6. Install them:
```
pip install -r requirements.txt
```
 
This takes a few minutes.
 
If VS Code asks "We noticed a new environment has been created. Do you want to select it?", click **Yes**.

## 5. Make a GitHub account
 
Sign up at [github.com](https://github.com/) if you don't have an account. Use an email address you can access, as you will receive an invitation from your partner in Week 2. Please note your **username** and bring it with you.
 
In Week 2 we will connect VS Code to your account.

## 6. Apply for an account on the cluster
In week five, we will get an intro to high performance computing from the Computer Science HPC team. Please complete [this form](https://hpc.cs.ucl.ac.uk/account-form/) to request an account. This needs to be done ahead of the start of the course to give the CS team time to make all your accounts.
