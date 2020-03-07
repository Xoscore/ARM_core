
import argparse

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

