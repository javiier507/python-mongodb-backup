import datetime
import os

from dotenv import load_dotenv
from boto3 import session
from botocore.client import Config

load_dotenv()

# variables
DATABASE = os.getenv('DATABASE')
DB_USERNAME = os.getenv('DB_USERNAME')
DB_PASSWORD = os.getenv('DB_PASSWORD')
BACKUP_PATH = os.getenv('BACKUP_PATH')
CONTAINER = os.getenv('CONTAINER')

def backup() -> str:
    date = datetime.datetime.now()
    date_format = date.strftime("%Y-%m-%d_%H-%M")

    filename = 'backup-{}.zip'.format(date_format)

    connection = '--authenticationDatabase=admin -d {} -u {} -p {}'.format(DATABASE, DB_USERNAME, DB_PASSWORD)

    os.system('sudo docker exec {} mongodump {} --gzip --archive=/opt/{}'.format(CONTAINER, connection, filename))
    os.system('sudo docker cp {}:/opt/{} {}'.format(CONTAINER, filename, BACKUP_PATH))

    return filename

# run process

filename = backup()
print('backup executed! file {} generated'.format(filename))