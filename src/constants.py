import datetime

# Error messages
DOWNLOAD_INTERVAL_ERROR = "Can't fetch that regularly."
MISSING_EMAIL_ERROR = "Email is missing."

# Messages

CHANGES = f"Changes detected"
EXIT = "\nExiting..."
DOWNLOAD = f"Fetching..."

# Folder configuration
TEMP_FOLDER = "tmp"
BASE_FOLDER = "tmp/base"
NEW_FOLDER = "tmp/new"

# Constants 
MIN_INTERVAL = 5
DEFAULT_INTERVAL = 5*60

# Instructions
EMAIL_HELP = "Email to notify when changes are made."
INTERVAL_HELP = f"Change the interval between fetching. Must be more than {MIN_INTERVAL} seconds."