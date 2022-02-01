====File Descriptions===
1. Results/ folder contains figures and all the data tables presented in the manuscript. The final figures shown in the manuscript were re-generated and formatted using GraphPad software and in some cases with Adobe Illustrator. The data content is identical to plots output in Results folder.

2. genelists/ folder contains input data files for our analysis.

3. Analysis_Source_Code.ipynb is a Jupyter notebook python code designed to generate all of our RNASeq analyses results.

4. Analysis_Source_Code.pdf is a pdf copy of the jupyter notebook above so the algorithm may be viewed without installing python and jupyter.

5. seq_studies_data.zip can be unzipped and the python file within run to download the raw studies included in the analysis from cbioportal.
    to run the python file, open the anaconda terminal (or another terminal with python installed) in the directory where seq_studies_data is unzipped, preferably preserving folder structure in original package and run the following command:
        python Raw_Studies_Downloader.py
        
===Installation Guide===

A. Running source code - Analysis_Source_Code.ipynb:

The source code was written in python 3.8.5 using Jupyter notebook format. 
The authors recommend installing Anaconda or similar package where the libraries required are conveniently obtained: https://www.anaconda.com/

Jupyter notebook is required to open the source code. This package is installed with Anaconda and can be started using Anaconda Navigator. 

If not using Anaconda, Jupyter can be independently installed at the following link. https://jupyter.org

The source code is present in the file, Analysis_Source_Code.ipynb. To open the file, initiate Jupyter notebook from Anaconda Navigator. 
	The software opens up in the default browser application. Now, change the current working directory to the folder where the has been unzipped. 
	It is important that the whole zipped file is unzipped in the same location preserving the sub-folder structure and files. 
	Once within the folder, clicking on the source code Analysis_Source_Code.ipynb opens the main processing notebook. 
	The commands are divided into blocks which can be run independently by pressing the play button. 
	The whole notebook can be run by scrolling the notebook menu and clicking the tab 'Cell' and then 'Run All'.
	This file generates data and plots corresponding to figures and tables in the manuscript and saves them in a Results folder. 
	Running time is under 20 mins for a processor with a >2Ghz clock and >=8GB RAM. 

A copy of fully run code is present with filename 'Analysis_Source_Code.pdf' in the package home folder which can be viewed using a PDF viewer.


B. Dependencies Required to run the source code:

The following libraries were used in compiling the source code.
1. NumPy 1.19.2
2. pandas 1.1.3

The libraries may be installed/updated using pip command or conda command or Anaconda navigator GUI. Anaconda by default installs the latest version of these three libraries.