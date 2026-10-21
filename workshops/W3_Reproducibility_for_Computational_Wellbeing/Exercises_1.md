# Exercise 1 - Rerun Test, Structure Rescue, and What's In The Repo (75 mins)

## The rerun test (15 mins)
Dig out a project you haven't touched in at least 6 months.

Look at the files. Can you find everything you'd need to understand and rerun this project — raw data, metadata, code, documentation, results? Note anything missing.
**Make sure you copy/save/protect any important files**. If there is anything too important to lose, don't try to reproduce anything, just assess whether you _could_ reproduce outputs using the info available. If you are trying to reproduce it, try to rerun the code. Without changing anything, see if you can get from raw data to a known output or figure.

Log where it breaks, or where you got stuck just trying to find things in step 1.

Some common culprits:

- hard-coded file paths that only exist on your machine
- a package that's a different version now, or missing entirely
- a step you did manually and never wrote down
- raw data that's been moved, renamed, or was never saved separately at all
- no idea what half the files even are, six months on
- not recording how each output is produced - which version of code, which input data, which metadata etc.

Make a note of something that broke. At the end of the session, we'll look at everyone's problems and see if we have addressed any of them.

## Project rescue (25 mins)
Here we discuss how naming conventions and project organisation help rescue disorganised projects.

### File Naming
File naming is the cause of a lot of confusion. E.g. see this image from [phdcomics.com](https://phdcomics.com/comics/archive.php?comicid=1323) (copyright Jorge Cham):

<img width="600" height="484" alt="image" src="https://github.com/user-attachments/assets/cf9b7761-47c7-4259-a0de-898dc043802e" />

Read through this [guide](https://datamanagement.hms.harvard.edu/plan-design/file-naming-conventions) for file naming - think about what would be important for you. Which of these is something you have not thought about before?

Look at your folder from the first two weeks. Where does it diverge from this? Make a note

### Project Structure
File and folder organisation is the big brother of file naming:

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

Using a standard project structure is easier and more reliable than starting a new structure every time you start a project. Here is how you can do it:
1. Download [this example project structure](https://github.com/UCL-Biosciences/Biosciences-Computational-Training/blob/prep-2026/workshops/W3_Reproducibility_for_Computational_Wellbeing/project-structure.zip) and extract all the contents.
2. Make sure your local and remote repos are synchronised by committing and synchronising in Visual Studio Code (instructions [here](https://github.com/UCL-Biosciences/Biosciences-Computational-Training/blob/prep-2026/workshops/W2_VersionControl_Collaboration_Git/Exercise_1.md#adding-files-to-the-repo-20-mins)).
3. Add the project structure to the **online repository, not through VSC**. To do this, open the github page for the repo, click on the `+` button next to the big green `<> Code` button, and drag and drop the files/folders in the "project-name" folder. Note, this means not the project-name folder itself, but go into project-name, select everything, then drag and drop.

This will integrate the project structure into your current setup without overwriting anything. I tried it and it worked anyway! If there are any problems, you can always return to previous states of the repo, which is one of git's big strengths.

On the other hand, I tried to copy the project structure into a folder that already contained a data and code folder, and it overwrote everything. Silly VSC, clever github!

If you finish this, look at a real project you are working on. How could the organisation be improved? Would this help you organise your work?


**Menti check**: who does a clear structure actually help? [Link]

## Where do we store data? (35 mins)
### To git or not to git?
Not everything belongs in git. Large raw data files bloat your repository and slow down every clone, forever — git never forgets, even if you delete the file later.

Our projects often have data folders because it is easy to work within a single project folder. But we don't want the data to end up on git - how can we keep the data in the `data` folder but tell git not to push it to github? Git uses `.gitignore` files to know which files and folders should be ignored. Anything listed in the `.gitignore` file will not be tracked or committed, which is what we want to do with the `data` folder. 

E.g. this would ensure everything in the data is ignored and never pushed to github:

```
# file saved in the github project "root" as e.g. my-project/.gitignore
data/
```

Things to consider when deciding whether to ignore something:
1. Security - is there anything sensitive (personal info, passwords) that we never want to be public?
2. Local machine/session files e.g. .DS_Store on mac, .Rproj files or python notebook checkpoints
3. Size - is a file or folder too big to be pushed and pulled? Where else could it be stored?
4. Reproducibility - which files do we need to understand and reproduce a project?
5. Audience - who is the repo for? Will they want to see your notes, your code, and/or your results?

**In pairs/groups, sort the following into "commit to git", "add to `.gitignore`", or "store elsewhere entirely":**
- your analysis scripts/notebooks
- a 2GB raw sequencing file
- your `results/` figures
- your environment file
- a spreadsheet of sample metadata
- a folder of cached temporary files

Write a working `.gitignore` for your project based on this. (GitHub has good starter templates for Python projects if you want a base to edit.)

**So where does the big raw data actually go?**
## Research data
While we are still working on research data, we need somewhere to store it. This is where institutional storage comes in — UCL's Research Data Storage Service (RDSS). You should already have access to a training project we set up in advance.

1. Mount the RDSS training project using the guides for [Windows](https://www.ucl.ac.uk/research-innovation/advanced-research-computing/platforms-and-services/research-data-storage-service/how-mount-research-data-storage-service-windows) and [Mac](https://www.ucl.ac.uk/research-innovation/advanced-research-computing/platforms-and-services/research-data-storage-service/how-mount-research-data-storage-service-mac-os). If that doesn't work, you can try using the file transfer programmes listed for windows and Mac. Ask if you are having problems!
2. Upload your raw data there instead of committing it to git.

### Other storage solutions
RDSS for most research data but there are lots of options. Some more info [here](https://github.com/UCL-Biosciences/Biosciences-Comp-Support/blob/main/UCL_comp_guides/data_storage_at_UCL.md). In particular, sensitive data must not be on RDSS! See TRE for more info.

## Publishing data
Published data should be FAIR. Increases probability someone else will use it which increases your citation count while also making best use of the data.

The best solution is to publish them in domain-specific archives e.g. ncbi, [bioimage archive](https://www.ebi.ac.uk/bioimage-archive/) etc. General-purpose repositories are also good if there is not an appropriate specific option, plus UCL has a Research Data Repository where datasets can be published and are discoverable by unique DOIs - more citations!

## Metadata
Research data can be unusable if it doesn't have metadata. At the very least, you need sample metadata to link research data to sample characteristics. This should be enough to reproduce your results. There are domain-specific standards that recommend what we should include.

**Menti check**: who does appropriate data storage actually help? [Link]

## Summary
You now have a repo that's structured sensibly, has a working `.gitignore`, and has its raw data sitting somewhere sensible rather than bloating your git history. None of that touches whether the *code itself* still runs elsewhere, though — that's next, after the break.
