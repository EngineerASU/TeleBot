from pymongo import MongoClient
from Settings import MONGO_DB
from Settings import MONGODB_LINK

mdb = MongoClient(MONGODB_LINK)[MONGO_DB] # переменная для работы с БД MongoDB

def search_or_save_user(mdb, effective_user, message):
    user = mdb.users.find_one({"user_id": effective_user.id}) # поиск в коллекции users по user.id
    if not user: # если такого нет, создаём словарь с данными
        user={
            "user_id": effective_user.id,
            "first_name": effective_user.first_name,
            "username": effective_user.username,
            "chat_id": message.chat.id
        }
        mdb.users.insert_one(user) # сохраняем в коллекцию users
    return user

# сохраняем - обновляем результаты анкеты и возвращаем результат
def save_user_anketa(mdb, user, user_data):
    mdb.users.update_one(
        {'_id': user['_id']},
        {'$set': {'anketa': {'name': user_data['name'],
                             'age': user_data['age'],
                             'evaluation': user_data['evaluation'],
                             'comment': user_data['comment']
                             }
                  }
         }
    )
    return user

