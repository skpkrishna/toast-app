import pymongo
from . import config

class Database():
    DATABASE = None

    @staticmethod
    def initialize():
        client = pymongo.MongoClient(config.MONGO_URI, config.MONGO_PORT)
        Database.DATABASE = client['toast-app']

    @staticmethod
    def insert(collection, data):
        Database.DATABASE[collection].insert_one(data)

    @staticmethod
    def find(collection, query):
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def update(collection, filter, values):
        return Database.DATABASE[collection].update(filter, values, {upsert : True})

    @staticmethod
    def delete(collection, query):
        return Database.DATABASE[collection].delete_one(query)

    @staticmethod
    def find_one(collection, query):
        return Database.DATABASE[collection].find_one(query)
