from pymongo import MongoClient

port = 27017  # env variable
db_url = 'cluster0-mdmj0.mongodb.net'  # env variable
username = 'admin'                      # env variable
password = "PASSWORD"
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
