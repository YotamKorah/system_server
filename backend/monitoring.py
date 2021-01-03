# monitoring.py

# Imports
import randominfo
import pymongo
import time

# Constants
client = pymongo.MongoClient(
    "mongodb://localhost:27017"
)
DB = client['menahem']
TEST = DB['test']


def get_test_data():
    data = []
    data.append({"title": "name", "text": randominfo.get_full_name()})
    data.append({"title": "birthday", "text": randominfo.get_birthdate()})
    if randominfo.randint(0, 1):
        data.append({"title": "phoneNumber", "text": randominfo.get_phone_number()})
    return data


if __name__ == '__main__':
    while True:
        try:
            TEST.delete_many({})
            TEST.insert_many(get_test_data())
        except:
            continue
        finally:
            time.sleep(10)

