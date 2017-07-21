# WordDensityAnalysis
#
#STEPS TO RUN :
1.	Ensure that the package is downloaded and run in the virtual environment to make sure all the modules run as required.
For vitual env:
`pip install virtualenv`<br />
`pip version`-----will give you the version installed<br />
`cd my_project_folder/`<br />
`vitrtualenv my_project`<br />
`source virtualenv/bin/activate`<br />
2.	Install the required packages

`pip install nltk`<br />

`pip install BeautifulSoup`<br />

OR
	`sudo apt-get install BeautifulSoup`<br />
	`sudo apt-get install nltk`<br />


3.	Then to install other nltk files do
`python`<br />
`>>>import nltk`<br />
`>>>nltk.download()`<br />
Then a window pops up click on download.
This downloads all the required nltk files.

4.	To run the file :

`python main.py [URL]`<br />
The URL you need to scrape should be passed as a command line argument.
Eg: $ python main.py http://wkbn.com/2017/07/14/spokeswoman-jimmy-carter-out-of-hospital-after-rehydration/amp/



