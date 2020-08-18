## A template repository for creating a REMARK.


A REMARK (R[eplications/eproductions] and Explorations Made using ARK) is a self-contained and complete projects written using the Econ-ARK. REMARKs should be `nbreproduce` compatible and reproducible across platforms.

The base structure of REMARK should look like
```
- reproduce.sh / a bash script (required)
- versioned locked requirements.txt (required)
- README.md (required)
- REMARKname.cff (optional CFF format file for the REMARK)
- OriginalPaper.bib (optional bib reference file to the original Paper)
- code/ (if required)
  - file1.py
  - notebook1.ipynb
  - ...
- figures/ (if required)
  - fig1.png
  - fig2.png
  - ...
- paper/ (if required)
  - paper.tex
  - paper.bib
  - paper.pdf
  - ...
- slides/ (if required)
  - slides.tex
  - ....
```
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
$ pip install nbreproduce
```
