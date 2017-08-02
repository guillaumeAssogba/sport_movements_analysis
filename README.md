# sport_movements_analysis
========

### Overview

Sport movement analysis project is an open-source tool for helping sport scientists to analyse specific sports movements such as sport services, kicking a ball in rugby or footbal, throwing a ball, etc... The idea is, thanks to a python interface, to allow the choices of different machine learning processes. The first analysis proposed is based on the research made in "Comparison of centre of gravity and centre of pressure patterns in the golf swing" by Aimée C. Smith, Jonathan R. Roberts, Pui Wah Kong & Stephanie E. Forrester.

### DATA STRUCTURE

This toolbox requires two datasets - an example of the datasets structure should be uploaded soon.:
  - a standardized body movement dataset - the first column should be the standardized time and the others columns are the recorded body movement. Each body part analyzed should be placed on a different sheet inside a excel document with the same structure than described before.
  - a performance dataset - the first column correspond to the person of the datasets on the same order.  Then, the next columns correspond to the performance achieved by the sportmen (speed, strength, precisions, etc...)

For now, this tool only accept excel files but csv and text file should be allowed soon too.

### TO DO
Groups division:
Allow to divide the body movement dataset in different groups according by using the K-means methods or by separating the 30% best and worst sportmen for further analysis.

PCA analysis:
  - regression between the loadings and the performance achieved by players.
  - projections along specified principal components.
  - distinguish projections depending on the group categories
  
 ### TO RUN
After copying this project,you simply run the main.py file. You need some python libraries (numpy, sklearn, scipy, matplotlib, pandas, ...). I would recommend to download anaconda and run this project thanks to spyder.

### NEXT STEP

The next steps are to provide the possibility to easily add any algorithm by linking some commented codes to the existing user interface, to allow the use of different type of files for the dataset, to write the results of the analysis directly in a Latex file.
Feel free to contribute to this project, write any comments or share it with your communautee.

author: Guillaume ASSOGBA
mail: Guillaume.Assogba@eleves.ec-nantes.fr
