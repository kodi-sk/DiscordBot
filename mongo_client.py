from pymongo import MongoClient
import os

port = os.environ.get('DB_PORT')  # env variable
db_url = os.environ.get('DB_URL')  # env variable
username = os.environ.get('DB_USERNAME')                      # env variable
password = os.environ.get('DB_PASSWORD')           # env variable
client = MongoClient(f"mongodb+srv://{username}:{password}@{db_url}/test?retryWrites=true&w=majority")
db_name = client.discord_bot


def get_db_table(db_table_name):  # Return Table name from the database according to the requirements.
    db_table_name_dict = {
        'google_query': db_name.google_query
    }
    if db_table_name_dict.get(db_table_name) is None:
        raise ValueError
    else:
        return db_table_name_dict.get(db_table_name)

