# Exercise 1 - Rerun Test, Structure Rescue, and What's In The Repo (75 mins)

## The rerun test (15 mins)
Dig out a project you haven't touched in at least 6 months. **Note this is not the project from weeks 1 and 2. We use a different one for this exercise only**

Look at the files. Can you find everything you'd need to understand and rerun this project — raw data, metadata, code, documentation, results? See if you can answer these questions from what is in the files:
- what is the project and what are the aims?
- what and where are the data?
- what analyses have you done? Why and how?
- what is the current state of the project? Who have you shared it with and where is it published?

If there is some code, try to re-run it (**make sure you are not overwriting any important outputs!!**). If it fails, why?

Some common culprits:

- hard-coded paths
- a package that's a different version now, or missing entirely
- a step you did manually and never wrote down
- raw data that's been moved, renamed, or was never saved separately at all
- no idea what half the files even are, six months on
- not recording how each output is produced - which version of code, which input data, which metadata etc.

Make a note of something that broke. At the end of the session, we'll look at everyone's problems and see if we have addressed any of them.

## Project organisation (25 mins)
Here we discuss how naming conventions and project organisation help rescue disorganised projects.

### File Naming
File naming is the cause of a lot of confusion. E.g. see this image from [phdcomics.com](https://phdcomics.com/comics/archive.php?comicid=1323) (copyright Jorge Cham):

<img width="600" height="484" alt="image" src="https://github.com/user-attachments/assets/cf9b7761-47c7-4259-a0de-898dc043802e" />

Read through this [guide](https://datamanagement.hms.harvard.edu/plan-design/file-naming-conventions) for file naming - think about what would be important for you. Which of these is something you have not thought about before? Does anyone have good rules or a good system for file naming?

E.g.:
- use dashes (-) or underscores (_) but not spaces as separators
- letters, numbers, `-`, `_` and `.`. No special characters
- identify important metadata that could be used in names. Order metadata info consistently e.g. always date_project_sample_treatment, not switching to date_sample_treatment_project
- dates should be YYYYMMDD - always sort chronologically
- use version control with git or version with dates, but avoid unclear versioning markers like `final`.

Look at your folder from the first two weeks. Are there any violations of this?

### Project Structure

<img width="1440" height="900" alt="724619122_e634531f5f_o" src="https://github.com/user-attachments/assets/f6b9dd3e-62c5-4002-8f08-ca2054a7ec73" />

(From jeanbaptisteparis [on flickr](https://www.flickr.com/photos/jeanbaptisteparis/724619122/) )

A standardised project would be more suitable, something like this:

```
project-name/
├── README.md
├── .gitignore        # including data, so large files don't get pushed to GitHub
├── data/             # original data should live elsewhere, in shared backed-up storage — but you may want local copies to work on
│   ├── raw/          # if real raw data, must be read-only, never edited
│   └── processed/    # generated, disposable
├── code/             # scripts, in run order or numbered
├── results/          # figures, tables — generated, disposable
├── docs/             # protocols, notes, decisions
└── env/              # renv.lock, environment.yml, requirements.txt
```
#### Reorganise projects
Let's introduce this structure and renaming principles to our project from weeks 1 and 2.

Using a standard project structure is easier and more reliable than starting a new structure every time you start a project. Here is how you can do it:
1. Download [this example project structure](/workshops/W3_Reproducibility_for_Computational_Wellbeing/project-structure.zip) and extract all the contents.
2. Make sure your local and remote repos are synchronised by committing and synchronising in Visual Studio Code (instructions [here](/workshops/W2_VersionControl_Collaboration_Git/Exercise_1.md#adding-files-to-the-repo-20-mins)).
3. Add the project structure to the **online repository, not through VSC**. To do this, open the github page for the repo, click on the `+` button next to the big green `<> Code` button, and drag and drop the files/folders in the "project-name" folder. Note, this means not the project-name folder itself, but go into project-name, select everything, then drag and drop.
4. Now we will do some reorganising. It is easier to move files in VSC so we need to make changes there. First, make sure the new project structure is in the online repo, then `Pull` or `Sync` your project in VSC to get the changes on your local machine.
5. Move the files; data to data folder, plot to results folder. Leave the notebook in the repo root.
6. Try to run notebook 3. It will fail due to broken paths. We change the paths for data in and plot out, then run again.
7. Once working, save and push new changes to repo.

_Having a standard project structure makes you more organised. But on top of that, it also means you will have less filepath errors._

If you finish this, look at a real project you are working on. How could the organisation be improved? Would this help you organise your work?

**Menti check**: who does a clear structure actually help? [Link](https://www.menti.com/alyp8mf53k7h)

## Where do we store data? (35 mins)
### To git or not to git?
Not everything belongs in git. Raw data files should live in appropriate research data storage (see below) and should never be stored on github. Large files may not be appropriate even if they are not raw data as they can make working with github slow and cumbersome. Git limits repos to 10GB (but recommends <5GB) and individuals files to ~100MB. Our projects often have data folders because it is easy to work within a single project folder. But we don't want the data to end up on git - how can we keep the data in the `data` folder but tell git not to push it to github? Git uses `.gitignore` files to know which files and folders should be ignored. Anything listed in the `.gitignore` file will not be tracked or committed, which is what we want to do with the `data` folder. 

E.g. this would ensure everything in the data is ignored and never pushed to github:

```
# file saved in the github project "root" as e.g. my-project/.gitignore
data/
```

Things to consider when deciding whether to ignore something:
1. Security - is there anything sensitive (personal info, passwords) that we never want to be public?
2. Local machine/session files e.g. .DS_Store on mac, .Rproj files or python notebook checkpoints
3. Size - is a file or folder too big to be pushed and pulled? Where else could it be stored? Git limits repos to 10GB and files to ~100MB
4. Reproducibility - which files do we need to understand and reproduce a project?
5. Audience - who is the repo for? Will they want to see your notes, your code, and/or your results?

**In pairs/groups, sort the following into "commit to git", "add to `.gitignore`", or "store elsewhere entirely":**
- your analysis scripts/notebooks
- a 2GB raw sequencing file
- your `results/` figures
- your environment file
- all the libraries/software you have downloaded for a project
- a spreadsheet of sample metadata
- a folder of cached temporary files

Use post-its to decide for each!

Write a working `.gitignore` for your project based on this. (GitHub has good starter templates for Python projects if you want a base to edit.)

**So where does the big raw data actually go?**

### Research data
While we are still working on research data, we need somewhere to store it. This is where institutional storage comes in — UCL's Research Data Storage Service (RDSS). You should already have access to a training project we set up in advance.

1. Mount the RDSS training project using the guides for [Windows](https://www.ucl.ac.uk/research-innovation/advanced-research-computing/platforms-and-services/research-data-storage-service/how-mount-research-data-storage-service-windows) and [Mac](https://www.ucl.ac.uk/research-innovation/advanced-research-computing/platforms-and-services/research-data-storage-service/how-mount-research-data-storage-service-mac-os). If that doesn't work, you can try using the file transfer programmes listed for windows and Mac. Ask if you are having problems!
2. Upload your raw data there

### Other storage solutions
RDSS for most research data but there are lots of options. Some more info [here](https://ucl-biosciences.github.io/Biosciences-Comp-Support/data_storage_at_UCL.html). In particular, sensitive data must not be on RDSS! See TRE for more info.

**Menti check**: who does appropriate data storage actually help? [Link](https://www.menti.com/alyp8mf53k7h)

## Summary
You now have a repo that's structured sensibly, has a working `.gitignore`, and has its raw data sitting somewhere sensible rather than bloating your git history. None of that touches whether the *code itself* still runs elsewhere, though — that's next, after the break.
