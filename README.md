# Description
This is the example program for exercise for Treasure Data
It is console utility, that get several arguments and output result directly into console
It is writen on Python 3.7 Interpreter, but probably run on any 3.* version (I did not check, say that because no magic used)

Main code lie in "query_tool.py" file
  One point - it is possible to split it onto several function or even make class and so on
  But I did not see any reason to do it - it is just one pipeline with option, so let it be it like that in code
  
To manage it behavior (because there are some additional options I want to add), I create file "globals.py"
It should be placed in same folder as main file

In additional, I add "additional_tools.py" with my piece of code from my hobby project
Because I forgot to tell, that I have my python project as a hobby...
It is tiny (because I start it just one month ago), but I try to keep useful things

# Import
I use two libraries to make it

**tabulate** - for better output in tabular option

**argparse** - to get and parse options

Both are just standart and can be installed by 

$ pip install tabulate, argparse

# Globals configuration

**LIST_ENGINES** and **LIST_FORMAT** - 
This is just list, what this program can do, to additional improvement

**MIN_MAX_TIME** and **MIN_MIN_TIME** - I do not know the exact limitation of min/max time - it make sense to make it positive, but maybe 
someone want to change it

**MAX_LINES_OUTPUT** - Too large response is bad for console and, actually, does not make sense, so I limit it here by 100
Although, it is directly overwriten by limit option from user

**BOOL_WITH_KEY_CHECK** - I use standard way to feed the key to client, but it is possible to keep only one key this way
  In additional, maybe someone want to run it from PC without key (but know it from other source)
  So, with this option to True, it is possible to feed the key in console directly

**BOOL_WITH_FILE_OUTPUT** - There is no any sign of file output in requirements, but I think that it is much better this way
Change this option to True - will add '--file' option to parser
If this file option does not presented, nothing will change in behavior of program at all (same limits and output to console)
But if use it like '--file report_1', it write file instead of console output - and this time without any limitation 
(500k from nasdq table is fine)

**BOOL_WITH_MAP** - The 'hive' engine return 'map' in response
I spent some time to understand why, but not get any info not in docs, not in library
So, I just exclude it from result, but leave an option to get it back again
Also it was made bad way, by 'dict' type, so any dict in response would be discarded
But I cannot do it any better, without understand why it happens

# Usage example

$ py query_tool.py -h

Print help of usage

$ py query_tool.py test_db_2 test_table_2 -f tabular -c user_id,username

Correct return for id and name from my table

$ py query_tool.py test_db_2 test_table_2 -f csv -l 0 -vv -c user_id,username,

Last comma in col_list is not a problem!

$ py query_tool.py test_db_2 test_table_2 -f csv -l 0 -v -m 5 -M 10

Although correct - this one does not return any result, but tell it in statistic file

$ py query_tool.py test_db_2 test_table_2 -f csv -l 10 -vv -e presto

Output as csv with debug, check that limit 0 is work (althout I did not get why, probably it comes from python library)

$ py query_tool.py sample_datasets nasdaq -vv -l 1000

Limit has overwrite default limit to output - with debug turn on

$ py query_tool.py sample_datasets nasdaq -v -l 20000 --file report_3 -e hive

Big peice of data will be add to file directly without console
No debug, jsut statistic
Also hive used

Failcases

$ py query_tool.py asd asd -vv -l 1000

It throw that database is incorrect

$ py query_tool.py sample_datasets asd -vv -l 1000

This one throw that table does not exist

$ py query_tool.py test_db_2 test_table_2 -f csv -l 10 -vv -e presto -m 100 -M 10

Throw error about MAX < MIN

$ py query_tool.py test_db_2 -f csv -l 10 -vv -e presto -m 100 -M 10

It throw error, because no table in input

