from googlesearch import search
from mongo_client import get_db_table
import datetime


def get_google_query_list(query, tld, lang, number_of_results, timeout_google):  # Returns Top searches on Google
    return_list = []
    for j in search(query, tld=tld, lang=lang, stop=number_of_results, pause=timeout_google):
        return_list.append(j)
    return return_list


def google_output(username, query, bot_id):  # Method for inserting input into DB and getting top searches from google.
    number_of_results = 5
    timeout_google = 2
    lang = 'en'
    tld = "co.in"
    insert_in_db(username, query, bot_id)
    return get_google_query_list(query, tld, lang, number_of_results, timeout_google)


def insert_in_db(username, query, bot_id):  # insert the input in DB for future reference
    db_table_name = 'google_query'
    user_input = {'username': username, 'bot_id': bot_id, 'input': query, 'created_at': datetime.datetime.now()}
    print(user_input)
    try:
        db = get_db_table(db_table_name=db_table_name)
        db.insert_one(user_input)
    except Exception as e:
        print(e)

