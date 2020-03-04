# This is my exercise solve for ARM
# Oleg Gusarov

# Goal:
# Write a command line tool to issue a query on Treasure Data and query a
# database and table to retrieve the values of a specified set of columns in a
# specified date/time range.

import tdclient

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


def check_arguments(db_name, table_name,
               col_list=None, min_time=None, max_time=None, engine="presto", format_file="tabular", limit=None):
    # Check required
    if db_name is None:
        print("DB name is required")
    if table_name is None:
        print("Table name is required")
    # Then I drop app with this text (will think how to do it better)

    # For columns - there is no required separator
    # Need to check somehow, if columns names are correct and then drop if not
    if col_list is None:
        columns = []
    else:
        columns = col_list.split(",")
    # Later

    # For time part
    # Well, at least it works correct
    # Because it is console input - we always expect String or None
    # Check if user input min_time:
    if min_time is not None:
        if not(min_time[0] == '-' and min_time[1:].isdigit() or min_time.isdigit()):
            print("Please, input correct number for min time - UNIX time required")
        elif int(min_time) < MIN_MIN_TIME:
            print("Min time should be larger then " + str(MIN_MIN_TIME))

    # Check if user input max_time:
    if max_time is not None:
        if not(max_time[0] == '-' and max_time[1:].isdigit() or max_time.isdigit()):
            print("Please, input correct number for max time - UNIX time required")
        elif int(max_time) < MIN_MAX_TIME:
            print("Max time should be larger then " + str(MIN_MAX_TIME))

    # Sad, but I did not find beauty way to compare with None, so check it again for now
    if min_time is not None and max_time is not None:
        # Also we can expect the int here (because we check it in previous already)
        # Probably change it later with the whole model (I still not sure which model to use)
        if int(max_time) <= int(min_time):
            print("Max time should be larger, then min time")

    # Engine check
    if engine not in LIST_ENGINES:
        print("Unrecognised engine option")

    # Format checks:
    if format_file not in LIST_FORMAT:
        print("Unrecognised file format")

    # And limits
    # Leave like this for now, think about it later
    if not(limit[0] == '-' and limit[1:].isdigit() or limit.isdigit()):
        print("Please, input correct number for limit")
    elif int(max_time) < MIN_LIMIT:
        print("Limit should be larger then " + str(MIN_LIMIT))
