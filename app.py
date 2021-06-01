from common.db import Database
from flask import Flask, request
from models.user import User
from models.tables import Tables
from models.menus import Menus

app = Flask(__name__)
app.secret_key = "911274145d37414da8f3b668d783ad17"


@app.before_first_request
def initialize_database():
    Database.initialize()


#=====================================TABLE ROUTES=======================================
@app.route('/api/table/<string:name>',methods=['GET','POST'])
@app.route('/api/table/<string:id>',methods=['GET','POST'])
@app.route('/api/table',methods=['POST'])
def get_or_post_tables(name=None,id=None):
    if request.method == 'GET':
        if name is not None:
            table = Tables.find_by_name(name)
            if table:
                return table.json(), 200
        if id is not None:
            table = Tables.find_by_id(name)
            if table:
                return table.json(), 200
        return {'message': "No tables found."}, 400
    else:
        table_name = request.json['table_name']
        table_location = request.json['table_location']
        if name is not None:
            table = Tables.find_by_name(name)
            if table:
                return {'message': "The table {} already exists.".format(table_name)}, 400
        if id is not None:
            table = Tables.find_by_id(id)
            if table:
                return {'message': "The table {} already exists.".format(table_name)}, 400
        else:
            new_table = Tables(table_name=table_name, table_location=table_location)
            try:
                new_table.save_to_mongo()
            except Exception as e:
                return {"message": "An error occurred inserting the item." + str(e.args)}, 500
            return {"message": "The new table {} is added.".format(table_name)}, 201

@app.route('/api/tables',methods=['GET'])
def get_all_tables():
    table = Tables.find_all_tables()
    if table:
        return table.json(), 200
    return {"message" : "No Tables are found"}, 400

@app.route('/api/tables/available',methods=['GET'])
def get_available_tables():
    table = Tables.find({'is_reserved' : False})
    if table:
        return table.json(), 200
    return {"message" : "All the Tables are reserved"}, 200

@app.route('/api/table/<string:name>',methods=['PUT'])
@app.route('/api/table/<string:id>',methods=['PUT'])
def update_table(name=None):
    table_name = request.json['table_name'] if name is None else name
    table_location = request.json['table_location']
    if name is not None:
        table = Tables.find_by_name(name)
        if table:
            try:
                Tables.update_by_id({'_id': table['_id']}, {'table_name' : table_name, 'table_location' : table_location})
            except Exception as e:
                return {"message": "An error occurred inserting the item." + str(e.args)}, 500

            return {'message': "The table {} is updated.".format(table_name)}, 400
        else:
            try:
                Tables.save_to_mongo(table.json())
            except Exception as e:
                return {"message": "An error occurred inserting the item." + str(e.args)}, 500
            return {"message": "The table {} is added.".format(table_name)}, 201
    if id is not None:
        table = Tables.find_by_id(id)
        if table:
            try:
                Tables.update_by_id({'_id': table['_id']}, {'table_name' : table_name, 'table_location' : table_location})
            except Exception as e:
                return {"message": "An error occurred inserting the item." + str(e.args)}, 500

            return {'message': "The table {} is updated.".format(table_name)}, 400
        else:
            try:
                Tables.save_to_mongo(table.json())
            except Exception as e:
                return {"message": "An error occurred inserting the item." + str(e.args)}, 500
            return {"message": "The table {} is added.".format(table_name)}, 201

@app.route('/api/table/<string:name>',methods=['DELETE'])
@app.route('/api/table/<string:id>',methods=['DELETE'])
def remove_table(name=None,id=None):
    table_name = request.json['table_name'] if name is None else name
    if name is not None:
        table = Tables.find_by_name(name)
        if table:
            try:
                Tables.delete_by_id({'_id': table['_id']})
            except Exception as e:
                return {"message": "An error occurred deleting the item." + str(e.args)}, 500

            return {'message': "The table {} is deleted.".format(table_name)}, 400
    if id is not None:
        try:
            Tables.delete_by_id({'_id': table['_id']})
        except Exception as e:
            return {"message": "An error occurred deleting the item." + str(e.args)}, 500

        return {'message': "The table {} is deleted.".format(table_name)}, 400
#=====================================TABLE ROUTES=======================================

#=====================================MENUS ROUTES=======================================
@app.route('/api/menu/<string:name>',methods=['GET','POST'])
@app.route('/api/menu/<string:id>',methods=['GET','POST'])
@app.route('/api/menu',methods=['POST'])
def get_or_post_tables(name=None,id=None):
    if request.method == 'GET':
        if name is not None:
            menu = Menus.find_by_name(name)
            if menu:
                return menu.json(), 200
        if id is not None:
            menu = Menus.find_by_id(name)
            if menu:
                return menu.json(), 200
        return {'message': "No menus found."}, 400
    else:
        item_name = request.json['item_name']
        item_description = request.json['item_description']
        item_category = request.json['item_category']
        item_subcategory = request.json['item_subcategory']
        item_cuisine = request.json['item_cuisine']
        item_course = request.json['item_course']
        item_store_id = request.json['item_store_id']
        item_price = request.json['item_price']
        item_discount = request.json['item_discount']
        is_combo = request.json['is_combo']
        is_available = request.json['is_available']

        if name is not None:
            menu = Menus.find_by_name(name)
            if menu:
                return {'message': "The menu {} already exists.".format(item_name)}, 400
        if id is not None:
            menu = Menus.find_by_id(id)
            if menu:
                return {'message': "The menu {} already exists.".format(item_name)}, 400
        else:
            new_menu = Menus(item_name=item_name, item_description=item_description, item_category=item_category, item_subcategory=item_subcategory, item_cuisine=item_cuisine, item_course=item_course, item_store_id=item_store_id, item_price=item_price, item_price=item_price, item_discount=item_discount, is_combo=is_combo, is_available=is_available)
            try:
                new_menu.save_to_mongo()
            except Exception as e:
                return {"message": "An error occurred inserting the item." + str(e.args)}, 500
            return {"message": "The new table {} is added.".format(item_name)}, 201

@app.route('/api/menus',methods=['GET'])
def get_all_menus():
    menu = Menus.find_all_tables()
    if menu:
        return menu.json(), 200
    return {"message" : "No Menus are found"}, 400

@app.route('/api/menus/available',methods=['GET'])
def get_available_menus():
    menu = Menus.find({'is_available' : True})
    if menu:
        return menu.json(), 200
    return {"message" : "No Menus are available."}, 200

@app.route('/api/menu/<string:name>',methods=['PUT'])
@app.route('/api/menu/<string:id>',methods=['PUT'])
def update_menu(name=None):
    item_name = request.json['item_name']
    item_description = request.json['item_description']
    item_category = request.json['item_category']
    item_subcategory = request.json['item_subcategory']
    item_cuisine = request.json['item_cuisine']
    item_course = request.json['item_course']
    item_store_id = request.json['item_store_id']
    item_price = request.json['item_price']
    item_discount = request.json['item_discount']
    is_combo = request.json['is_combo']
    is_available = request.json['is_available']
    if name is not None:
        menu = Menus.find_by_name(name)
        if menu:
            try:
                Menus.update_by_id({'_id': menu['_id']}, {'item_name' : item_name, 'item_description' : item_description, 'item_category' : item_category, 'item_subcategory' : item_subcategory, 'item_cuisine': item_cuisine, 'item_course' : item_course, 'item_store_id' : item_store_id, 'item_price' : item_price, 'item_discount' : item_discount, 'is_combo': is_combo, 'is_available' : is_available})
            except Exception as e:
                return {"message": "An error occurred updating the menu." + str(e.args)}, 500

            return {'message': "The menu {} is updated.".format(item_name)}, 400
        else:
            try:
                Menus.save_to_mongo(table.json())
            except Exception as e:
                return {"message": "An error occurred inserting the item." + str(e.args)}, 500
            return {"message": "The menu {} is added.".format(item_name)}, 201
    if id is not None:
        menu = Menus.find_by_id(id)
        if menu:
            try:
                Menus.update_by_id('_id': menu['_id']}, {'item_name' : item_name, 'item_description' : item_description, 'item_category' : item_category, 'item_subcategory' : item_subcategory, 'item_cuisine': item_cuisine, 'item_course' : item_course, 'item_store_id' : item_store_id, 'item_price' : item_price, 'item_discount' : item_discount, 'is_combo': is_combo, 'is_available' : is_available})
            except Exception as e:
                return {"message": "An error occurred inserting the item." + str(e.args)}, 500

            return {'message': "The menu {} is updated.".format(item_name)}, 400
        else:
            try:
                Menus.save_to_mongo(table.json())
            except Exception as e:
                return {"message": "An error occurred inserting the item." + str(e.args)}, 500
            return {"message": "The menu {} is added.".format(item_name)}, 201

@app.route('/api/menu/<string:name>',methods=['DELETE'])
@app.route('/api/menu/<string:id>',methods=['DELETE'])
def remove_menu(name=None,id=None):
    item_name = request.json['item_name'] if name is None else name
    if name is not None:
        menu = Menus.find_by_name(name)
        if menu:
            try:
                Menus.delete_by_id({'_id': menu['_id']})
            except Exception as e:
                return {"message": "An error occurred deleting the item." + str(e.args)}, 500

            return {'message': "The menu {} is deleted.".format(item_name)}, 400
    if id is not None:
        try:
            Menus.delete_by_id({'_id': menu['_id']})
        except Exception as e:
            return {"message": "An error occurred deleting the item." + str(e.args)}, 500

        return {'message': "The menu {} is deleted.".format(item_name)}, 400
#=====================================MENU ROUTES=======================================


if __name__ == '__main__':
    app.run(debug=True)  # important to mention debug=True
