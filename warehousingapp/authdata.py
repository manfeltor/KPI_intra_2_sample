from decouple import config

DEBUG = config('DEBUG', default=False, cast=bool)
LOCSERVADDRESS = config('LOCSERVADDRESS')
LOCDB = config('LOCDB')
LOCUSER = config('LOCUSER')
LOCPASS = config('LOCPASS')

server = LOCSERVADDRESS
db = LOCDB
user = LOCUSER
passw = LOCPASS