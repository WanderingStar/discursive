# Default settings configured by user or overriden by CLI

# ES, SQLITE, S3, FILE
BACKEND = 'FILE'

# Required for ES backend
ES_HOST = ''
AWS_REGION = 'us-east-1'


#SQLITE
DATA_DIR = ''
DATABASE_NAME = 'test'
TABLE_NAME = 'tweets'


#FILE
DATA_DIR = ''
FILE_NAME = 'tweets'

# CSV, JSON
FORMAT = 'JSON'
