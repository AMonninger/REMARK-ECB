## A template repository for creating a REMARK.


A REMARK `(R[eplications/eproductions] and Explorations Made using ARK)` is a self-contained and complete projects written using the Econ-ARK. REMARKs should be `nbreproduce` compatible and reproducible across platforms.

The base structure of a REMARK should look like
```
- reproduce.sh / a bash script (required)
- versioned locked requirements.txt (required)
- README.md (required)
- resources
    - resources/code (if required)
      - file1.py
      - notebook1.ipynb
      - ...
    - resources/latex (if required)
      - paper.tex
      - paper.bib
      - paper.pdf
    - resources/figures (if required)
      - fig1.png
      - fig2.png
      - ....
    - resources/equations (if required)
    - resources/slides (if required)
      - slides.tex
      - ....
    - resources/[REMARKname].cff (optional CFF format file for the REMARK)
    - resources/[REMARKname-OriginalPaper].bib (optional bib reference file to the original Paper)
    - resources/dashboard (if required)
      - dashboard.ipynb
    - resources/....
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

For example if you use econ-ark, numpy, pandas, seaborn in your REMARK notebooks and code a requirements file would look
```
econ-ark
numpy
pandas
seaborn
```
But this file misses out an important detail which is absolutely necessary to make sure it is reproducible across systems and in the future, python package versions. A versioned requirements file would look like:
```
econ-ark==0.10.7
numpy==1.19.1
seaborn==0.10.1
pandas==1.1.1
```



