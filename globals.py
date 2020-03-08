# List of supported engines
LIST_ENGINES = ["presto", "hive"]

# List of supported formats
LIST_FORMAT = ["tabular", "csv"]

# Need to point on something
LIST_POINT_TO = {
    "personal": "You have ",
    "uncertain": "There are ",
    "empty": "",
}

# Limit for minimum time requests
MIN_MAX_TIME = 0
MIN_MIN_TIME = 0

# To print long lists in comfortable way, should be > 5
MAX_PRINT_LIST_NUMBER = 10

# This set of options come not from requirements, but from my view of what I want from this app if make it for myself
# If I want to put key on call, not on default
BOOL_WITH_KEY_CHECK = False

# If I want to output in file, not just on screen
BOOL_WITH_FILE_OUTPUT = False

# Check if we return 'map' field from table
BOOL_STRICT_COLUMNS = True
