import datetime
import os

from dotenv import load_dotenv

load_dotenv()

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
os.system('docker cp database_1:/opt/{} ./backups/'.format(filename))