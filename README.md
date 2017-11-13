# sport_movements_analysis

### Overview

Sport_movement_analysis project is an open-source tool for helping sports scientists to analyse specific sports movements such as sport services, kicking a ball in rugby or footbal, throwing a ball, etc... The idea is, thanks to a python interface, to allow the choices of different machine learning processes. The first analysis proposed is a PCA reduction and a statistics analysis of the PC scores and the loadings.

### DATA STRUCTURE

This toolbox requires two datasets :
  - a standardized body movement dataset - the first column should be the standardized time and the others columns are the recorded body movement. Each body part analyzed should be placed on a different sheet inside a excel document with the same structure than described before.
  - a performance dataset - the first column corresponds to the person of the datasets on the same order than in the body movement dataset.  Then, the next columns correspond to the performance achieved by the sportmen (speed, strength, precisions, etc...)

For now, this tool only accept excel files but csv and text file should be allowed soon too.

### TO DO
Groups division:
Allow to divide the body movement dataset in different groups according by using the K-means methods or by separating the 30% best and worst sportmen for further analysis.

PCA analysis:
  - regression between the loadings and the performance achieved by players.
  - projections along specified principal components.
  - distinguish projections depending on the group categories
  
### TO RUN
After copying this project, you simply run the main.py file. You need some python libraries:
numpy, sklearn, scipy, matplotlib, pandas, pylatex, PyQt4.
I would recommend to download anaconda and run this project thanks to spyder. Most of the libraries' wheel can be downloaded directly on "http://www.lfd.uci.edu/~gohlke/pythonlibs/#pandas" and installed thanks to pip. 
It is possible to run the application without the interface if wanted. A test.py file allows running directly the code.

### OUTPUT
Depending on the algorithms chosen, the programs would plot the figures of the different results in the console. These figures would be stored in the "plot" files. A Latex report can also be rendered with most of the results.

### NEXT STEP

The next steps are to provide the possibility to easily add any algorithm by linking some commented codes to the existing user interface, to allow the use of different type of files for the dataset. Some classifications algorithms would be added (SVM and neural networks) which would use the PC's loadings. The construction of the report would be improved by allowing the user to indicate the sport and a description of the dataset (numbers of samples, observations, and participants). An example of dataset should be uploaded for helping the user to perform the analysis.

Feel free to contribute to this project, write any comments or share it with your communautee.

author: Guillaume ASSOGBA
mail: Guillaume.Assogba@eleves.ec-nantes.fr
