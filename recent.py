from mongo_client import get_db_table


def recent_output(username, query, bot_id):  # Share all the inputs of the user where the query string exists
    db_table_name = 'google_query'
    db = get_db_table(db_table_name=db_table_name)
    return_list = []
    details = db.find({'username': username, 'bot_id': bot_id, 'input': {'$regex': query}})
    for d in details:
        return_list.append(d['input'])
    return return_list
