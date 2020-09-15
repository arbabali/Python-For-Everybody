Simple Python Search Spider, Page Ranker, and Visualizer

This is a set of programs that emulate some of the functions of a 
search engine.  
They store their data in a SQLITE3 database named
'spider.sqlite'.  This file can be removed at any time to restart the
process.   


You should install the SQLite browser to view and modify 
the databases from:

http://sqlitebrowser.org/

This program crawls a web site and pulls a series of pages into the
database, 
recording the links between pages.

Note: Windows has difficulty in displaying UTF-8 characters
in the console so for each console window you open, you may need
 to 
type the following command before running this code:

    chcp 65001

http://stackoverflow.com/questions/388490/unicode-characters-in-windows-command-line-
Win: spider.py

Enter web url or enter: ['http://www.dr-chuck.com']

If you restart the program again and tell it to crawl more
pages, it will not re-crawl any pages already in the database.  
Upon 
restart it goes to a random non-crawled page and starts there.  So 
each successive run of spider.py is additive.

You can have multiple starting points in the same database - 
within the program these are called "webs".  
The spider 
chooses randomly amongst all non-visited links across all
the webs.

If you want to dump the contents of the spider.sqlite file, 
The spdump.py program
only shows pages that have at least one incoming link to them.


Once you have a few pages in the database, you can run Page Rank on the
pages using the sprank.py program.  
You simply tell it how many Page
Rank iterations to run.
