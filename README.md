# Youtube Analysis Tool

The code provided in this repo allows an user to scrape any youtube video for metadata and comments. This achieved using
selenium to automatically load the target youtube url and scroll to the bottom of the page until all comments are loaded.
The target data could easily be retreived using the youtube API as well (a feature to be added in the future), but in 
order to minimize the requirements for running this application (i.e needing an API key) I chose an automated scrape 
approach. Also, I thought this way was cooler and I made this in a weekend.

## Configuration
To set up the app simply source the setup.sh script provided. This will install all pre-requisits and set up the basic
directories needed. All data generated or required should be placed in the data directory created. All plots generated 
by the analysis tool should be saved in the output directory.

## Running The Tool
Currently there is no overarching main script that guides you through full process (a feature to be added).

* First scrape the page source of your target video by using 'youtube_scraper.py --name <simple name>'.
This will generate a <simple name>_source.html file in your data folder.

* Then run comment_parser.py --name <simple name> to load the source html and parse it into a json and csv format. The 
resulting files are stored in the data folder as well.

* Lastly to visualize your content run the visualize.py --name <simple name> command to read your generated files in the
data dir. This will automatically generate word clouds and place them in the output directory. 