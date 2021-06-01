from common.db import Database
import uuid
import datetime

class Menus():
    def __init__(self, _id=None, item_name, item_description, item_category, item_subcategory, item_cuisine, item_course, item_store_id, item_price, item_discount, is_combo, is_available, created_at=None):
        self._id = uuid.uuid4().hex if _id is None else _id
        self.item_name = item_name
        self.item_description = item_description
        self.item_category = item_category    # denotes veg, non-veg, egg
        self.item_subcategory = item_subcategory  # denotes main_course like biriyani, noodles, fried rice and  side_dish type like gravy, starters
        self.item_cuisine = item_cuisine  # denotes chinese, continental, southindan, northindian, chettinaad, mexican, italian
        self.item_course = item_course    # denotes preferrance for breakfast, lunch, snacks, beverages like juices, shakes, desserts like cakes, icecream
        self.item_store_id = item_store_id
        self.item_price = item_price
        self.item_discount = item_discount
        self.is_combo = is_combo
        self.is_available = True
        self.created_at = datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S') if created_at is None else created_at
        self.updated_at = datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')

    @classmethod
    def find_by_name(cls, table_name):
        return Database.find_one(collection = 'menus', query={'item_name': table_name})

    @classmethod
    def find_by_id(cls, _id):
        return Database.find_one(collection = 'menus', query={'_id': _id})


    @classmethod
    def get_available_menus(cls):
        data = Database.find(collection='menus', {"is_available": True})
        if data is not None:
            return cls(**data)

    def json(self):
        return {
            "_id": self._id,
            "item_name": item_name,
            "item_description": self.item_description,
            "item_category" : self.item_category,
            "item_subcategory" : self.item_subcategory,
            "item_cuisine" : self.item_cuisine,
            "item_course" : self.item_course,
            "item_store_id" : self.item_store_id,
            "item_price" : self.item_price,
            "item_discount" : self.item_discount,
            "is_combo" : self.is_combo,
            "is_available": self.is_available,
            "created_at": self.created_at,
            "updated_at" : self.updated_at
        }

    def save_to_mongo(self):
        Database.insert(collection='menus', self.json())
