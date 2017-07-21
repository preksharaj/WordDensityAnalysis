# WordDensityAnalysis
# Problem
List of common topics that best describe the contents of the page<br />
# Steps to run <br />

1.	Ensure that the package is downloaded and run in the virtual environment to make sure all the modules run as required.
For vitual env:<br />
`pip install virtualenv`<br />
`pip version`-----will give you the version installed<br />
`cd my_project_folder/`<br />
`vitrtualenv my_project`<br />
`source virtualenv/bin/activate`<br />
2.	Install the required packages<br />

`pip install nltk`<br />

`pip install BeautifulSoup`<br />

`pip install bs4`<br />

OR<br />
	`sudo apt-get install BeautifulSoup`<br />
	`sudo apt-get install nltk`<br />


3.	Then to install other nltk files do<br />
`python`<br />
`>>>import nltk`<br />
`>>>nltk.download()`<br />
Then a window pops up click on download.
This downloads all the required nltk files.and then close the pop up box.

4.	To run the file :<br />

Go back to the root directory and run
`python main.py [URL]`<br />
The URL you need to scrape should be passed as a command line argument.<br />
Eg: `python main.py http://wkbn.com/2017/07/14/spokeswoman-jimmy-carter-out-of-hospital-after-rehydration/amp/`



