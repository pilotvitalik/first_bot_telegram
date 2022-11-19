import requests

import get_env
import db


def get_update():
    response = requests.get(f'{get_env.url}{get_env.token}/getUpdates')
    results = response.json()['result']
    cursor, connection = db.open_con()
    for result in results:
        from_user = result['message']['from']
        if from_user['is_bot']:
            return
        print(from_user)
        is_absent_user = db.is_data_in_stock(cursor, from_user['id'])
        print(is_absent_user)
        if is_absent_user:
            db.insert_data((cursor, connection, from_user))
        print(is_absent_user)
        print(result)


get_update()
