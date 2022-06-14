from django.http import JsonResponse
from pymongo import MongoClient
import json, re

# Mongo Client
def Mongo_Client():
    """Returns database handler"""
    client = MongoClient(host="127.0.0.1",
                        port=27017,
                        )                  
    db_handle = client['Carts_App']
    return db_handle
    

def list_services(request):
    """List available services"""
    res = {
        "Name": "shopping cart REST API",
        "Description": "REST API that handles CRUD operations for a specific user",
        "Version": "1.0.0"
    }
    return JsonResponse(res, status=200)


def create_cart(request):
    """Endpoint for creating a new cart"""
    if request.method == "POST":
        # Parse recieved json data
        name = request.body.decode("UTF-8")
        name = json.loads(name)["name"]
        # Validate name
        if not re.match(r'[a-zA-Z0-9_]', name):
            return JsonResponse({"error":"invalid name"}, status=404)
        # Connect to Carts collection
        db_handle = Mongo_Client()
        collection_handle = db_handle["Carts"]
        # Check if cart name exists
        if collection_handle.count_documents( {"name": name}, limit=1) == 0:
            record = {
                "name": name,
                "items": []
            }
            insert = collection_handle.insert_one(record)
            return JsonResponse({"success":"cart created successfully"}, status=201)
        else:
            return JsonResponse({"error":"name already exists"}, status=409)
    else: # If not POST method
        return JsonResponse({"error":"endpoint requires POST method"}, status=405)


def get_items(request, cart_name):
    """Endpoint for viewing existing items in str:cart_name"""
    if request.method == "GET":
        # Connect to Carts collection
        db_handle = Mongo_Client()
        collection_handle = db_handle["Carts"]
        # Check if cart name exists
        if collection_handle.count_documents( {"name": cart_name}, limit=1) != 0:
            res =  collection_handle.find_one({"name": cart_name})["items"]
            return JsonResponse(res, safe=False, status=200)
        else:
            return JsonResponse({"error":"cart not found"}, status=404)
    else:
        return JsonResponse({"error":"endpoint requires GET method"}, status=405)


def add_items(request):
    """Patches a record if exists and add the item id"""
    if request.method == "PUT":
        # Get data
        name = request.body.decode("UTF-8")
        name = json.loads(name)
        items_list = name["items_list"] # Just saving some memory
        name = name["name"]
        # Validate data - check phase 1
        for item in items_list:
            if not re.match(r'[0-9]+', item):
                return JsonResponse({"error":"invalid item id provided"}, status=404)
        # Connect to Carts collection
        db_handle = Mongo_Client()
        collection_handle = db_handle["Carts"]
        # Update data or return error response cart_name not found
        # check if cart exists - check phase 2
        try:
            new_items_list = collection_handle.find_one({"name": name})["items"]
            # Check if any items are already in the list
            # if yes bypass, if not then add - check phase 3
            for item in items_list:
                if not item in new_items_list:
                    new_items_list += [item]
            collection_handle.update_one({"name": name},
                                            {"$set": {"items": new_items_list}}
                                            )
            return JsonResponse({"success":"item added successfully"}, status=201)
        except:
            return JsonResponse({"error":"cart not found"}, status=404)
    else:
        return JsonResponse({"error":"endpoint requires PUT method"}, status=405)


def delete_items(request):
    """Delete provided items from a cart"""
    if request.method == "PATCH":
        # Get data
        name = request.body.decode("UTF-8")
        name = json.loads(name)
        items_list = name["items_list"] # Just saving some memory
        name = name["name"]
        # Connect to Carts collection
        db_handle = Mongo_Client()
        collection_handle = db_handle["Carts"]
        # Check if cart exists - check phase 1
        if collection_handle.count_documents( {"name": name}, limit=1) != 0:
            document_items_list = collection_handle.find_one({"name": name})["items"]

            for item in items_list:
                # If provided item in the cart then delete
                # else bypass - check phase 2
                if item in document_items_list:
                    document_items_list.remove(item)

            collection_handle.update_one({"name": name},
                                         {"$set": {"items": document_items_list}}
                                         )
            return JsonResponse({"success":"items deleted"}, status=202)
        else:
            return JsonResponse({"error":"cart not found"}, status=404)
    else:
        return JsonResponse({"error":"endpoint requires PATCH method"}, status=405)


def delete_cart(request):
    """Delete provided cart from the database"""
    if request.method == "DELETE":
        # Get data
        name = request.body.decode("UTF-8")
        name = json.loads(name)
        name = name["name"]
        # Connect to Carts collection
        db_handle = Mongo_Client()
        collection_handle = db_handle["Carts"]
        # Check if cart name exists
        if collection_handle.count_documents( {"name": name}, limit=1) != 0:
            collection_handle.delete_one({"name":name})
            return JsonResponse({"success":"cart created successfully"}, status=202)
        else:
            return JsonResponse({"error":"cart not found"}, status=404)
    else:
        return JsonResponse({"error":"endpoint requires DELETE method"}, status=405)

