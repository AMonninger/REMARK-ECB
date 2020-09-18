## A starter repository for creating a REMARK.

A REMARK `(R[eplications/eproductions] and Explorations Made using ARK)` is a self-contained and complete projects written using the Econ-ARK. REMARKs should be `nbreproduce` compatible and reproducible across platforms.

This is a starter repository to start building your REMARKs, an example of the final product of a REMARK is available at https://github.com/econ-ark/BufferStockTheory, a REMARK which reproduces the [Theoretical Foundations of Buffer Stock Saving]() paper.


[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/econ-ark/REMARK-template/master?filepath=resources%2Fcode%2Ftemplate-example-notebook.ipynb) Binder link for the main notebook in this repository.

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/econ-ark/REMARK-template/master?urlpath=voila%2Frender%2Fresources%2Fdashboard%2Fdashboard.ipynb) Binder link for a voila dashboard in this repository.

The base structure of a REMARK should look like
```
- reproduce.sh / a bash script (required)
- versioned locked requirements.txt (required)
- README.md (required, with Binder links to execute the notebooks and dashboards if they are present in the REMARK)
- code (if required)
  - file1.py
  - notebook1.ipynb
  - ...
- latex (if required)
  - paper.tex
  - paper.bib
  - paper.pdf
- figures (if required)
  - fig1.png
  - fig2.png
  - ....
- equations (if required)
- slides (if required)
  - slides.tex
  - ....
- [REMARKname].cff (optional CFF format file for the REMARK)
- [REMARKname-OriginalPaper].bib (optional bib reference file to the original Paper)
- dashboard (if required)
  - dashboard.ipynb
- .....
```
As you can see the resources directory of the REMARK is largely optional and can be molded as required. The only strict requirements are the bash scripts and the versioned requirements.txt file.

These bash scripts can contain any number of sequential steps, like running a python script, building latex files. Look at the bash script is this repository for an example.

It's possible to have multiple bash scripts too. A script like `reproduce_min.sh` which rebuilds a subset of the project in case the whole rebuild takes a lot of time.

The project should be reproducible using the following command in this directory
```
$ nbreproduce reproduce.sh/reproduce_min.sh/any_other_bash_script.sh
```

### How to install nbreproduce?

To get detailed documentation about `nbreproduce` you can go through https://econ-ark.github.io/nbreproduce/.

`nbreproduce` is available through PyPI and depends on [Docker](https://www.docker.com/products/docker-desktop).
If you already have Docker installed locally you can install `nbreproduce` using
```
$ pip install nbreproduce # make sure you have Docker installed on your machine. 
```

### What is a versioned requirements.txt file?

A requirements file tells the exact dependencies required to run the code. This currently only supports packages available on PyPI.

For example if you use econ-ark, numpy, pandas, seaborn and voila in your REMARK notebooks and code a requirements file would look
```
econ-ark
numpy
pandas
seaborn
voila
```
But this file misses out an important detail which is absolutely necessary to make sure it is reproducible across systems and in the future, python package versions. A versioned requirements file would look like:
```
econ-ark==0.10.7
numpy==1.19.1
seaborn==0.10.1
pandas==1.1.1
voila==0.1.22
```

### How to create mybinder links/buttons?

- Go to https://mybinder.org
- Fill up the URL field with the link to the repository (example: https://github.com/econ-ark/REMARK-template)
- In path to notebook, fill up the path to notebook (in this example: `resources/code/template-example-notebook.ipynb`)
- Click on the launch button to start the build
- Click on the "Copy the text below, then paste into your README to show a binder badge" to get the markdown and rST text required to create the mybinder button.

