# Exercise 2 - Environments, Documenting, and Sharing your Project (65 mins)

## Library snapshots using environments (25 mins)
Most projects require a set of code libraries in order to run, which means a project you started on your laptop won't necessarily work on your desktop or on your colleague's computer. And code that runs fine today can quietly stop working in six months — not because the code changed, but because the packages underneath it did. And sometimes, subtle changes as packages are upgraded can have meaningful impacts on your results! So you might have a different set of results and no idea why!

Fixing this means writing down exactly what your environment looked like when everything originally worked.

### Venv environments
Venv is a system for managing python packages using environments. It can install packages from a big archive and is also an environment manager. You can use it to make separate project workspaces called "environments". Using separate environments means you can have different versions of packages for different projects. This is surprisingly important when working with python libraries.

So, venv is for 1. installing packages and 2. managing reproducible environments.

**Open your project folder.** In Visual Studio Code, use `Open Folder` to open the folder of the project you are working in, 

**Create an environment**
Open a terminal window and run:

`python -m venv project-dna`

**Activate it**. To work with an environment, it has to be activated. You can also deactivate it with `deactivate`.

Mac:
`source project-dna/bin/activate`

Windows:
`source project-dna/Scripts/activate`

**Install packages**.
First install a general python package:

`pip install pandas==2.3.3 jupyter`

Then look up a package online relevant to your project and install it:

`pip install <YOUR PACKAGE HERE>`

**Take a snapshot**. Export the list of packages in the environment and save it to file:

`pip freeze > requirements-project-dna.txt`

**Add the file to your github repository**. We want to add the requirements file but not the whole venv folder. First, make sure your terminal is in the right folder (you can change it by using `Open Folder` in Visual Studio Code - you will have to open a new Terminal and activate the env again). Add the venv folder path to the `.gitignore` file from earlier, then add files to the repo using the Source Control extension we saw last week - how much do you remember?!

**Test it** Could we run the workshops from week 1 using this environment? How do we know what packages we need to use? Can you install everything we need to run it? Stretch goal...

**(Optional) Partner check**: swap repos with someone nearby. Can they clone your repo, rebuild your environment from the file you just committed, and get your code running — without asking you anything? If not, what's missing?

This is the bridge from everything you've done in W1 and W2 to the HPC session — you'll rebuild this exact environment on the cluster.

**Menti check**: who does capturing your environment actually help? [Link]

## Documentation with README files (15 mins)
Humans like stories more than lists. Github repos are no different. A good github repo always has a README file (or similar) that provides a clear and simple overview of the repo. It helps us understand the aims of the project and navigate the repo.

**Write a README that lets someone rerun your project cold.** At minimum it should answer:
- what does this project do, and on what data?
- how do you set up the environment? (point to requirements file)
- what order do you run things in, to get from raw data to the results?
- where does the raw data actually live? (link to RDSS or wherever you put it)

Keep it short (takes 1-2 minutes to read).

## Publishing your project (25 mins)
All of this work is building towards an Open Science project. Making things publicly available, easy to understand and FAIR means that 1. your work will be found and appreciated and 2. your results will be more reproducible.

An important part of this is making your project findable and citable. Now we will practice doing that with Zenodo. Zenodo is a free, open repository that archives outputs and gives them a permanent, citable DOI. This means your work can be found, credited and cited even if the GitHub repo (or other original host of the data) changes or disappears.

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

This record is now saved, citable and searchable. Google searches (although not scholar) look through Zenodo so your work could show up in relevant searches. Better than being buried in a supplementary file!

## Publishing real datasets
If your project has a real dataset that should live somewhere more permanent than Zenodo's storage (large data, sensitive data, or data with a natural disciplinary home), have a quick look at [fairsharing.org](https://fairsharing.org) or [re3data.org](https://re3data.org) to see where it would actually belong — you don't need to upload anywhere today, just get a sense of what exists.


**Menti check**: who does documentation, metadata, and a real DOI actually help? [Link]

## Summary
Your project is now structured, environment-captured, documented, and has a real, citable DOI attached to it. Go check your rerun-test sticky note from this morning — how many of those failure points would still happen to someone opening this repo today?
