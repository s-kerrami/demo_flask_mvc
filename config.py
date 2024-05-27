

scheme = 'postgresql+psycopg2'
username = "postgres"
password = 'postgres'
hostname = 'localhost'
port = '5432'
database_name = 'projet_python_mvc'

URL_DB = f"{scheme}://{username}:{password}@{hostname}:{port}/{database_name}"

SQLALCHEMY_DATABASE_URI = URL_DB