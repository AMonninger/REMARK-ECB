#!/bin/bash

pdflatex --output-directory=latex PortfolioChoiceWithRiskyHousing.tex
bibtex latex/PortfolioChoiceWithRiskyHousing
pdflatex --output-directory=latex PortfolioChoiceWithRiskyHousing.tex
pdflatex --output-directory=latex PortfolioChoiceWithRiskyHousing.tex
