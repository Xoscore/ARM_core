# This is my exercise solve for ARM
# Oleg Gusarov

# Goal:
# Write a command line tool to issue a query on Treasure Data and query a
# database and table to retrieve the values of a specified set of columns in a
# specified date/time range.

import tdclient
import argparse

# Well, first thing first, I need a skeleton of application

# On input:
# required: database name ​"db_name"
# required: table name "table_name"
# optional: comma separated list of columns "col_list" as string (e.g. "column1,column2,column3"). If not specified,
# all columns are selected.
# optional: minimum timestamp ​"min_time"​ in unix timestamp or ​"NULL"
# optional: maximum timestamp ​"max_time"​ in unix timestamp or ​"NULL"​.
# Obviously ​"max_time"​ ​must be greater​ than ​"min_time"​ or NULL.
# optional: query engine ‘​engine​’: "​hive​" or "​presto​". Defaults to ‘presto’.
# optional: output format ‘​format​’: ‘​csv​’ or ‘​tabular​". Defaults to ‘tabular’.
# optional: a query limit ‘​limit​’: ‘​100​’. If not specified, all records are selected.

# of cause it's just a draw

LIST_ENGINES = ["presto", "hive"]
LIST_FORMAT = ["tabular", "csv"]
MIN_MAX_TIME = 0
MIN_MIN_TIME = 0
MIN_LIMIT = 0

# $ query -f csv -e hive -c "my_col1,my_col2,my_col5" -m 1427347140 -M 1427350725 -l 100 my_db my_table
parser = argparse.ArgumentParser()
parser.add_argument("db_name",
                    help='"string" Name of database to connect')
parser.add_argument("table_name",
                    help='"string" Name of table for query')
parser.add_argument("-c", "--col_list",
                    help='List of columns to query, comma separated. By default everything')
parser.add_argument("-m", "--min_time",
                    help='Time FROM for rows, by default NULL', type=int)
parser.add_argument("-M", "--max_time",
                    help='Time TO fo rows, by default NULL', type=int)
parser.add_argument("-e", "--engine", choices=LIST_ENGINES, default="presto",
                    help='Engine for ???, "hive" or "presto". By default "presto"')
parser.add_argument("-f", "--format", choices=LIST_FORMAT, default="tabular",
                    help='Output file format, "csv" or "tabular". By default "tabular"')
parser.add_argument("-l", "--limit",
                    help='"int"    Limit for rows output. By default unlimited', type=int)
args = parser.parse_args()

columns = "*"
min_time = "NULL"
max_time = "NULL"
# Because we change type of variable, argparse deny this
if args.min_time:
    min_time = args.min_time
    if min_time < MIN_MIN_TIME:
        raise ValueError("MIN TIME should be more then " + str(MIN_MIN_TIME))
if args.max_time:
    max_time = args.max_time
    if max_time < MIN_MAX_TIME:
        raise ValueError("MAX TIME should be more then " + str(MIN_MAX_TIME))
# Improve raise later
if type(min_time) is int and type(max_time) is int and min_time >= max_time:
    raise ValueError("MIN TIME should be less then MAX TIME")
if args.col_list:
    columns = args.col_list.split(",")


print(args)
print(columns)
print(min_time)
print(max_time)
