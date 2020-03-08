# This is my exercise solve for ARM
# Oleg Gusarov

# Goal:
# Write a command line tool to issue a query on Treasure Data and query a
# database and table to retrieve the values of a specified set of columns in a
# specified date/time range.

import os
import tdclient
import time
import sys
import tabulate

# Check input somewhere here
db_name = "test_db_2"
table_name = "test_table_2"


# After input, we need to open client and try to connect to it
api_key = os.getenv("TD_API_KEY")
if api_key is None:
    raise ValueError("API key was not setup properly")

query_string = "SELECT * FROM " + table_name
'''
with tdclient.Client(api_key) as client:
    try:
        db = client.database(db_name)
    except Exception as e:
        print(e)
        raise

    try:
        table = client.table(db_name, table_name)
    except Exception as e:
        print(e)
        raise
    columns = []
    for column in table.schema:
        columns.append(column[0])
    print(columns)
    query_job = client.query(db_name, query_string)
    query_job.wait()
    if query_job.error():
        print(query_job.debug['stderr'])
        raise Exception

    option = "csv"
    if option == "tabular":
        table = []
        for row in query_job.result():
            line = []
            for value in row:
                BOOL_STRICT_COLUMNS
                if type(value) is not dict:
                    line.append(value)
            table.append(line)
        print(tabulate.tabulate(table))
    else:
        line = ''
        for row in query_job.result():
            line += ','.join(str(item) for item in row if type(item) is not dict)
            line += '\n'
        print(line)
'''
'''
if args.col_list:
    columns = '('
    for column in args.col_list.split(","):
        if column not in schema:
            print("There is no column " + column + " in this schema")
            print("Maybe you want one of this?")
            print(additonal_tools.tool_list_to_string(schema))
            return -1
        columns += ','.join(column)
    columns += ')'
    '''
b = []
a = ['asd', 'dsa']
b.append(a)
print(b)