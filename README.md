
## Install Dependecies

```
python3 -m venv venv

pip install sqlalchemy==2.0.6 pydantic[dotenv] ipython

```

## .env Configuration

You need a .env file for the database connection string if you are using postgresql.
```
hostname=myhost
port=5432
username=myuser
password=mypass
database=mydb
```


## Running ncrdb_test.py

```
PYTHONPATH=/path/to/parent ./ncrdb_test.py

```
