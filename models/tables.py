from common.db import Database
import uuid
import datetime

class Tables():
    def __init__(self, table_name, table_location, is_reserved=False, created_at=None):
        self._id = uuid.uuid4().hex  if _id is None else _id
        self.table_name = table_name
        self.table_location = table_location
        self.is_reserved = is_reserved
        self.created_at = datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S') if created_at is None else created_at
        self.updated_at = datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')


    @classmethod
    def get_available_tables(cls):
        data = Database.find(collection='tables', query={"is_reserved": False})
        if data is not None:
            return cls(**data)

    @classmethod
    def find_by_name(cls, table_name):
        return Database.find_one(collection = 'tables', query={'table_name': table_name})

    @classmethod
    def find_by_id(cls, _id):
        return Database.find_one(collection = 'tables', query={'_id': _id})

    @classmethod
    def find_all_tables(cls):
        data = Database.find(collection='tables', query={})
        return cls(**data)

    @classmethod
    def find_available_tables(cls):
        data = Database.find(collection='tables', query={'is_reserved' : False})
        return cls(**data)

    @classmethod
    def update_by_id(cls, filter, values):
        return Database.update('tables', filters, values)

    @classmethod
    def delete_by_id(cls, _id):
        return Database.delete(collection='tables', query={'_id': _id})

    def json(self):
        return {
            "_id": self._id,
            "table_name": self.table_name,
            "table_location": self.table_location,
            "is_reserved": self.is_reserved,
            "created_at": self.created_at,
            "updated_at" : self.updated_at
        }

    def save_to_mongo(self):
        Database.insert(collection='tables', data=self.json())
