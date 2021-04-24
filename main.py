import datetime
import os

from dotenv import load_dotenv
from boto3 import session
from botocore.client import Config

load_dotenv()

backups_path = '/home/penalba/backups/'

def backup() -> str:
    date = datetime.datetime.now()
    date_format = date.strftime("%Y-%m-%d_%H-%M")

    filename = 'strapi-{}.zip'.format(date_format)

    # credentials
    auth_db = os.getenv('AUTH_DB')
    database = os.getenv('DATABASE')
    username = os.getenv('USERNAME')
    password = os.getenv('PASSWORD')

    connection = '--authenticationDatabase={} -d {} -u {} -p {}'.format(auth_db, database, username, password)

    os.system('docker exec database_1 mongodump {} --gzip --archive=/opt/{}'.format(connection, filename))
    os.system('docker cp database_1:/opt/{} {}'.format(filename, backups_path))

    return filename

def upload(path: str, filename: str):
    ACCESS_ID = os.getenv('ACCESS_ID')
    SECRET_KEY = os.getenv('SECRET_KEY')

    client = session.Session().client('s3',
                            region_name='nyc3',
                            endpoint_url='https://nyc3.digitaloceanspaces.com',
                            aws_access_key_id=ACCESS_ID,
                            aws_secret_access_key=SECRET_KEY)

    client.upload_file(path, 'preciososdetallesspace', 'backups/{}'.format(filename))


# run process

filename = backup()

path = '{}{}'.format(backups_path, filename)

upload(path, filename)
