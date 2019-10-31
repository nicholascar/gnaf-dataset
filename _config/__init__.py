from os.path import dirname, realpath, join, abspath
import psycopg2

APP_DIR = dirname(dirname(realpath(__file__)))
TEMPLATES_DIR = join(dirname(dirname(abspath(__file__))), 'view', 'templates')
STATIC_DIR = join(dirname(dirname(abspath(__file__))), 'view', 'static')
LOGFILE = APP_DIR + '/flask.log'
DEBUG = True

PAGE_SIZE = 10000

URI_BASE = "http://linked.data.gov.au/dataset/gnaf"  # must _not_ end in a trailing slash
DEF_URI_PREFIX = "http://linked.data.gov.au/def"

MB_2011_COUNT = 347627
URI_MB_2011_CLASS = '/'.join([DEF_URI_PREFIX, 'MB2011'])
URI_MB_2011_INSTANCE_BASE = 'http://linked.data.gov.au/dataset/asgs/MB2011/'

MB_2016_COUNT = 358122
URI_MB_2016_CLASS = '/'.join([DEF_URI_PREFIX, 'MB2016'])
URI_MB_2016_INSTANCE_BASE = 'http://linked.data.gov.au/dataset/asgs/MB2016/'

ADDRESS_COUNT = 14773321 #Aug 2018
URI_ADDRESS_CLASS = '/'.join([DEF_URI_PREFIX, 'gnaf#Address'])
URI_ADDRESS_INSTANCE_BASE = '/'.join([URI_BASE, 'address/'])

ADDRESS_SITE_COUNT = 14773321 #Aug 2018
URI_ADDRESS_SITE_CLASS = '/'.join([DEF_URI_PREFIX, 'gnaf#AddressSite'])
URI_ADDRESS_SITE_INSTANCE_BASE = '/'.join([URI_BASE, 'addressSite/'])

STREET_LOCALITY_COUNT = 711978 #Aug2018
URI_STREETLOCALITY_CLASS = '/'.join([DEF_URI_PREFIX, 'gnaf#StreetLocality'])
URI_STREETLOCALITY_INSTANCE_BASE = '/'.join([URI_BASE, 'streetLocality/'])

LOCALITY_COUNT = 16458 #Aug 2018
URI_LOCALITY_CLASS = '/'.join([DEF_URI_PREFIX, 'gnaf#Locality'])
URI_LOCALITY_INSTANCE_BASE = '/'.join([URI_BASE, 'locality/'])

def from_env(env_var):
    if os.environ[env_var] is None:
        print('You must set an environment variable for the DB connection called ' + env_var)
        exit()
    else:
        return os.environ[env_var]

DB_HOST = from_env('DB_HOST')
DB_PORT = from_env('DB_PORT')
DB_DBNAME = from_env('DB_DBNAME')
DB_USR = from_env('DB_USR')
DB_PWD = from_env('DB_PWD')
DB_SCHEMA = from_env('DB_SCHEMA')

SPARQL_AUTH_USR = from_env('SPARQL_AUTH_USR')
SPARQL_AUTH_PWD = from_env('SPARQL_AUTH_PWD')
SPARQL_QUERY_URI = 'http://10.0.0.5/fuseki/gnaf/query'   #'http://13.210.68.240/fuseki/gnaf/query'