

# Query example to run:
# SELECT <col_list>
# FROM <table_name>
# WHERE TD_TIME_RANGE(time, <min_time>, <max_time>)
# LIMIT <limit>

# Time limits:
# ●  specifying NULL for the min timestamp value and a valid timestamp for max
# timestamp will SELECT all records whose timestamp is smaller than max timestamp
# ●  specifying NULL for the max timestamp value and a valid timestamp for min
# timestamp will SELECT all records whose timestamp is larger than min timestamp
# ●  specifying NULL for both the min and max timestamp will SELECT all records
# ●  specifying a valid timestamp for both the min and max timestamp will SELECT all
# records whose timestamp is larger than min timestamp and smaller than max timestamp

# Requirements:
# The command will need to:
# 1. run the query in Treasure Data
# 2. wait for the query to complete
# 1. if successful
# 1. download the result
# 2. output the result in the one of the formats the user selected.
# 3. exit with a 0 return value
# 2. if not successful
# show an error
# exit with a non-0 return value

# Command example:
# $ query -f csv -e hive -c "my_col1,my_col2,my_col5" -m 1427347140 -M 1427350725 -l 100 my_db my_table
# where:
# ●  -f / --format is optional and specifies the output format: tabular by default
# ●  -c / --column is optional and specifies the comma separated list of columns to restrict
# the
# result to. Read all columns if not specified.
# ●  -l / --limit is optional and specifies the limit of records returned. Read all records if not
# specified.
# ●  -m / --min is optional and specifies the minimum timestamp: NULL by default
# ●  -M / --MAX is optional and specifies the maximum timestamp: NULL by default
# ●  -e / --engine is optional and specifies the query engine: ‘presto’ by default
