# Exercise 2 - Environments, Documenting, and Sharing your Project (65 mins)

## Library snapshots using environments (25 mins)
Most projects require a set of code libraries in order to run, which means a project you started on your laptop won't necessarily work on your desktop or on your colleague's computer. And code that runs fine today can quietly stop working in six months — not because the code changed, but because the packages underneath it did. And sometimes, subtle changes as packages are upgraded can have meaningful impacts on your results! So you might have a different set of results and no idea why!

Fixing this means writing down exactly what your environment looked like when everything originally worked.

### Venv environments
Venv is a system for managing python packages using environments. It can install packages from a big archive and is also an environment manager. You can use it to make separate project workspaces called "environments". Using separate environments means you can have different versions of packages for different projects. This is surprisingly important when working with python libraries.

So, venv is for 1. installing packages and 2. managing reproducible environments. We used venv to make the "carpentries" environment we used in week 1 and week 2. 

Now, we will use venv to create a new environment, installing and recording the packages it downloads. Next, we will show how this works by reusing the carpentries env we made during the setup.

#### Making new environments
1. **Open your project folder.** In Visual Studio Code, use `Open Folder` to open the folder of the project you are working in. Note, this is the project folder, not the repo which lives inside the project folder.

2. **Create an environment**
Open a (git bash) terminal window and run:

`python -m venv project-NMR`

3. **Activate it**. To work with an environment, it has to be activated. You can also deactivate it with `deactivate`.

Mac:
`source project-NMR/bin/activate`

Windows:
`source project-NMR/Scripts/activate`

4. **Install packages**.
First install a general python package:

`pip install pandas==2.3.3 jupyter`

Then look up a package online relevant to your research and install it:

`pip install <YOUR PACKAGE HERE>`

5. **Take a snapshot**. Export the list of packages in the environment and save it to file:

`pip freeze > YOUR-REPO-NAME/env/requirements-project-NMR.txt` (remember to change YOUR-REPO-NAME to the name of the folder containing your repo) and `deactivate`.

6. **Add the file to your github repository**. We want to add the requirements file but not the whole venv folder. First, make sure your terminal is in the right folder (you can change it by using `Open Folder` in Visual Studio Code). Make sure the `project-NMR` venv folder is not in the repo (or add `project-NMR` to your .gitignore!). Add files to the repo using the Source Control extension.

At this point, your environment is safely recorded, including the exact package versions - have a look at the requirements-project-NMR.txt. It is safe to delete the venv project as we can recreate it from the requirements file. Delete `project-NMR` using VSC's file explorer.

#### Recreating environments
Before the course, you all created an environment called 'carpentries' using venv. Now, we will repeat those steps and discuss what they do:
1. Make sure you have the requirements.txt file from the setup somewhere in your project folder.
2. Run workbook 3 (plotting) using the `carpentries` kernel. Open the notebook and find the `Run All` button. Make sure all the cells run. If not, let us know!
3. Save the environment's packages by opening a terminal, activating the venv:

Mac:
`source carpentries/bin/activate`

Windows:
`source carpentries/Scripts/activate`

Then saving the environment to file: `pip freeze > YOUR-REPO-NAME/env/requirements-versions.txt`

How is that different to the original `requirements.txt` file?

5. Now let's see what the `carpentries` folder does. Rename it by right-clicking on the `carpentries` _folder_ in VSC explorer and calling it "carpentries_old". We keep it renamed as a backup in case there are problems recreating the env.
6. Try to run the notebook. It should fail because the packages you need that live in the `carpentries` are no longer found in that folder location.
7. But fear not! The project is not lost! We can recreate the env as we did in the [setup](https://github.com/UCL-Biosciences/Biosciences-Computational-Training/tree/main/setup#4-create-your-course-folder-and-software-environment). Remember to use `YOUR-REPO-NAME/env/requirements-versions.txt` and call it `carpentries` again.
8. Finally, re-run the notebook in the recreated env. VSC will probably be a bit confused, so we help by explicitly selecting the environment again: `Ctrl+Shift+P` → `Python: select interpreter`. Now the notebook should run again.
9. Once it runs, clean up by deleting the "carpentries_old" folder we made as a backup. Push the "reuquirements-versions.txt" to github.

**Menti check**: who does capturing your environment actually help? [Link](https://www.menti.com/alyp8mf53k7h)

## Documentation with README files (15 mins)
Humans like stories more than lists. Github repos are no different. A good github repo always has a README file (or similar) that provides a clear and simple overview of the repo. It helps us understand the aims of the project and navigate the repo.

**Write a README that lets someone rerun your project cold.** At minimum it should answer:
- what does this project do, and on what data?
- how do you set up the environment? (point to requirements file)
- what order do you run things in, to get from raw data to the results?
- where does the raw data actually live? (link to RDSS or wherever you put it)
- What are the key columns in your data and what units are they in?

Keep it short (takes 1-2 minutes to read).

## Publishing your project (25 mins)
All of this work is building towards an Open Science project. Making things publicly available, easy to understand and FAIR means that 1. your work will be found and appreciated and 2. your results will be more reproducible.

An important part of this is making your project findable and citable. Now we will practice doing that with Zenodo. Zenodo is a free, open repository that archives outputs and gives them a permanent, citable DOI. This means your work can be found, credited and cited even if the GitHub repo (or other original host of the data) changes or disappears.

### Citation and Licences
Two small files decide whether anyone can actually use what you publish.

A **licence** sets out what others are allowed to do with your work. Without one, the legal default is that nobody can reuse, modify or redistribute it so an unlicensed public repo is readable but not reusable. On GitHub: `Add file` > `Create new file`, type `LICENSE` as the filename, and a template picker appears. MIT is the simplest permissive choice for code; CC-BY suits data and documents.

A **citation file** tells people how you want to be credited. Add a file called `CITATION.cff` listing the authors (with ORCIDs), a title and a version, and GitHub displays a "Cite this repository" button on the repo page that generates the reference for people.

**Add both to your repo now**, before we publish — the archived version on Zenodo captures whatever is in the repo at the time of the release, so anything missing now is missing in the permanent record.

### Publishing on Zenodo

Today, we will use the _Zenodo sandbox_, which is just used for testing - DOIs are not real and will not represent a real record of anything.

**Publish a citable version of your project:**
1. Make sure your README and environment file are all committed and pushed.
2. Make sure your repository is public. Go to the repo on github > Settings > General > Danger Zone > `Change visibility`.
3. Log in to [Zenodo sandbox](https://sandbox.zenodo.org/) **with your github**. This means we can make Zenodo records directly from github repos.
4. Click on the drop-down menu in the top right >  Github > `Sync now` button. Scroll down to the bottom where you should see all the public repos from your github, and move the button to the `ON` position for your training repo.
5. Go to GitHub and [create a release](https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository). Zenodo will automatically download a .zip-ball of each new release and register a DOI:
  - Go the repo on github and find the Releases section (below About on the right-hand side of the page)
  - Click on `Create a new release`
  - On the "New release" page, click on `Tag: Select tag` and create a new tag (name it what you like).
  - Add a "Release title" and a description.
  - Click on `Publish release`, green button at the bottom.
6. The above will create a "tagged" "release" of your repo. Tags are ways of identifying specific versions of the repo. This could be "Submission 1" so you know exactly which version of code was submitted with a paper or "Version 1" for software. Releases are similar, but they also compile compressed files that contain everything in the repo when the release was published. This is what ends up on Zenodo. So a tag points to a certain commit, a release makes it easy to access a certain state.
7. Go back to the [Zenodo sandbox page](https://sandbox.zenodo.org/account/settings/github/), where you will see a (fake) DOI badge has been created for this repo. You can click on the badge, copy the markdown text and paste it into your repo's README.md, which will create a really cool shiny blue DOI badge. Hooray.
8. You can finally go back to your records on Zenodo sandbox (click on `My dashboard`), where you will find the published record and can edit details to increase its FAIRness.

**Zenodo Metadata**
Here are some things you can fill in to make your work more findable:
- **title** (not just the repo name)
- **authors** add your ORCID here, this is what links the output to you permanently
- **description** a couple of sentences on what the project is and what data it uses
- **licence** (match your LICENSE file)
- **keywords** how would someone searching for this phrase it?

If this was the real zenodo (i.e. not the sandbox), the record would be citable and searchable. Google searches (although not scholar) look through Zenodo so your work could show up in relevant searches. Better than being buried in a supplementary file! And it can be cited (more citations!), the DOI will persist even if Github or other sites disappear, and meets many funder and journal requirements for sharing outputs.

We have simulated an example today based on code and analysis, but this also applies to many outputs: protocols, talks, training, datasets, whitepapers. Anything that you want to publish a record of!

## Publishing real datasets
If your project has a real dataset that should live somewhere more permanent than Zenodo's storage (large data, sensitive data, or data with a natural disciplinary home), have a quick look at [fairsharing.org](https://fairsharing.org) or [re3data.org](https://re3data.org) to see where it would actually belong — you don't need to upload anywhere today, just get a sense of what exists.

Published data should be FAIR. It increases the probability someone else will use it, which increases your citation count while also making best use of the data.

The best solution is to publish them in domain-specific archives e.g. ncbi, [bioimage archive](https://www.ebi.ac.uk/bioimage-archive/) etc. General-purpose repositories are also good if there is not an appropriate specific option, plus UCL has a Research Data Repository where datasets can be published and are discoverable by unique DOIs - more citations!

## Metadata
Research data can be unusable if it doesn't have metadata. At the very least, you need sample metadata to link research data to sample characteristics. This should be enough to reproduce your results. There are domain-specific standards that recommend what we should include.


**Menti check**: who does documentation, metadata, and a real DOI actually help? [Link](https://www.menti.com/alyp8mf53k7h)

## Summary
Your project is now structured, environment-captured, documented, and has a real, citable DOI attached to it. Go check your rerun-test sticky note from this morning — how many of those failure points would still happen to someone opening this repo today?
