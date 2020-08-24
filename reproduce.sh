# install the versioned required packages
python3 -m pip install --quiet -r requirements.txt

# navigate to code/ and execute the python file to create figures
cd resources/code/
ipython template-example-notebook.py

# navigate to paper/ and build the latex file
cd ../paper/
pdflatex paper.tex
