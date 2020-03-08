import argparse
import os
import tdclient
import globals
import additonal_tools
import tabulate


def main():
    # $ query -f csv -e hive -c "my_col1,my_col2,my_col5" -m 1427347140 -M 1427350725 -l 100 my_db my_table

    # Collect input options
    # It is all argparse library tool, so do not touch it very deep
    parser = argparse.ArgumentParser()
    if globals.BOOL_WITH_KEY_CHECK:
        parser.add_argument("--key", default=os.getenv("TD_API_KEY"),
                            help="Way to add key directly when call")
    parser.add_argument("db_name",
                        help='Name of database to connect')
    parser.add_argument("table_name",
                        help='Name of table for query')
    parser.add_argument("-c", "--col_list",
                        help='List of columns to query, comma separated')
    parser.add_argument("-m", "--min_time", type=int,
                        help='Time FROM for rows, by default NULL')
    parser.add_argument("-M", "--max_time", type=int,
                        help='Time TO for rows, by default NULL')
    parser.add_argument("-e", "--engine", choices=globals.LIST_ENGINES, default="presto",
                        help='Engine for query, "hive" or "presto". By default "presto"')
    parser.add_argument("-f", "--format", choices=globals.LIST_FORMAT, default="tabular",
                        help='Output file format, "csv" or "tabular". By default "tabular"')
    if globals.BOOL_WITH_FILE_OUTPUT:
        parser.add_argument("--file", default=None,
                            help="Name of file to output")
    parser.add_argument("-l", "--limit",
                        help='Limit for rows output. By default unlimited', type=int)
    args = parser.parse_args()

    # At first, let's check, that user have key at all
    if globals.BOOL_WITH_KEY_CHECK:
        api_key = args.key
        if api_key is None:
            print("API key was not setup properly")
            return -1
    else:
        api_key = os.getenv("TD_API_KEY")
        if api_key is None:
            print("API key was not setup properly")
            return -1

    # It was done like this, because db and table return different exceptions and it should be catched one by one
    # (maybe not, but it can be easily fixed later)
    # By the way, there was no restrictions for performance or count of calls
    with tdclient.Client(api_key) as client:
        # Now, check, that database is accesable
        try:
            client.database(args.db_name)
        except Exception as e:
            print(e)
            return -1

        # And it have the called table
        try:
            table = client.table(args.db_name, args.table_name)
        except Exception as e:
            print(e)
            return -1

    # Now for columns
    # Schema is a list of list for each column, so I expect that first one is for names
    # Maybe it's naive, but I did not find the accurate way to call names from API directly
    # And actually, not need it =P
    schema = []
    for column in table.schema:
        schema.append(column[0])
    schema.append("UNIXTIME")
    # Check, if user make correct names of columns
    header = schema
    columns = ''
    if args.col_list:
        header = args.col_list.split(",")
        for column in args.col_list.split(","):
            # Excluse last comma for comfort and check if name is correct
            if column != '':
                if column not in schema:
                    print("There is no column " + column + " in this schema")
                    print("Maybe you want one of this?")
                    # Yes, this just improvement of "because I can"
                    # I forgot to tell, that I have my own repo, on first interview
                    # It's just tiny, but every tool from it can be used in any place
                    print(additonal_tools.tool_list_to_string(schema))
                    return -1
                columns += column + ','
        # I spent some time to find way to remove last comma, but fail, so let it be like this
        columns = columns[:-1]
    else:
        columns = '*'

    # Let's check time now
    # Default values should be NULL
    min_time = "NULL"
    max_time = "NULL"
    # Because we change type of variable, argparse deny this
    if args.min_time:
        min_time = args.min_time
        if min_time < globals.MIN_MIN_TIME:
            print("MIN TIME should be more then " + str(globals.MIN_MIN_TIME))
            return -1

    if args.max_time:
        max_time = args.max_time
        if max_time < globals.MIN_MAX_TIME:
            print("MAX TIME should be more then " + str(globals.MIN_MAX_TIME))
            return -1

    # And if both are persist, compare them
    if type(min_time) is int and type(max_time) is int and min_time >= max_time:
        print("MIN TIME should be less then MAX TIME")
        return -1

    # And by last, let's check LIMIT
    limit = ''
    if args.limit:
        if args.limit < 0:
            print("LIMIT should be positive integer")
            return -1
        limit = " LIMIT " + str(args.limit)

    # Let's collect the query to ask
    query_string = "SELECT " + columns + " FROM " + args.table_name + " WHERE TD_TIME_RANGE(time, " + min_time + ", " \
                   + max_time + ")" + limit

    # The query is checked and ready, so it's time to call for real DB
    query_job = client.query(args.db_name, query_string, type=args.engine)
    query_job.wait()
    if query_job.error():
        print(query_string)
        print(query_job.debug['stderr'])
        return -1

    output = ''
    # Start to output result
    if args.format == "tabular":
        table = []
        for row in query_job.result():
            line = []
            for value in row:
                if globals.BOOL_STRICT_COLUMNS:
                    if type(value) is not dict:
                        line.append(value)
                else:
                    line.append(value)
            table.append(line)
        output = tabulate.tabulate(table, headers=header)
    elif args.format == "csv":
        output = ','.join(schema) + '\n'
        for row in query_job.result():
            if globals.BOOL_STRICT_COLUMNS:
                output += ','.join(str(item) for item in row if type(item) is not dict)
            else:
                output += ','.join(str(item) for item in row)
            output += '\n'
    else:
        print("Unrecognisable format")
        return -1

    # When we get result use this
    if globals.BOOL_WITH_FILE_OUTPUT:
        if args.file is not None:
            filename = args.file
            if args.format in globals.LIST_FORMAT:
                if args.format == "csv":
                    filename += ".csv"
                elif args.format == "tabular":
                    filename += ".txt"
                else:
                    print("Unrecognisable file format")
                    return -1
            with open(filename, 'w') as file:
                file.write(output)
                pass

    print(output)
    return 0

main()
