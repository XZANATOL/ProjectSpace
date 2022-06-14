#  Shopping cart REST API Using Python Django & Mongodb

A REST API that handles CRUD operations for a specific user like create cart, get items, add items and remove items. The API makes use of Djagno and Pymongo. API was tested using Postman tool.

### Note

I wanted to demonstrate my understanding with MongoDB Client, so I used Pymongo instead of Djongo engine in order not to rely on Django models. Why Django? I already have mini API projects built with Flask and I wanted to get out of my safe zone.

pros of my approach:
* Ability to deeper demonstrate my understanding with MongoDB client.

cons of my approach:
* Unavailablity of Document-Object Mapper functionality (Django ORM) to register the model in the admin panel.

<hr>

## Preparation

* Install required libraries:
`$ pip3 install -r requirements.txt`

* Run server:
`$ python3 manage.py runserver`

<hr>

## API Documentation

The API contains 6 endpoints, each of a specific job, and lie in the `http://localhost:8000/api/` URL.

> Note: replace "\<variable\>" with a string data.

### 1. /api/

Allowed Method: any

Data body: none

Description: returns the name, description, and version of the API.

Example reponse: <br>
`{"Name": "shopping cart REST API", "Description": "REST API that handles CRUD operations for a specific user", "Version": "1.0.0"}`

Response Codes:
* 200: always.

### 2. /api/create

Allowed Method: POST

Data body type: JSON <br>
Data body: {"name": \<name\>}

Description: creates a cart with the provided name in the JSON body, and an empty `items` list.

Validation:
* name must contains only alphanumeric characters.

Response Codes:
* 201: Success - cart created.
* 404: Invalid name.
* 405: Invalid method.
* 409: Cart name already exists.

### 3. /api/get_items/\<cart_name\>

Allowed Method: GET

Data body: none

Description: returns a list of items present in the a cart. Name of the card is provided from the URL.

Response Codes:
* 200: Cart found and list of elements are returned.
* 404: Cart name not found.
* 405: Invalid method.

#### 4. /api/add_items

Allowed Method: PUT

Data body type: JSON <br>
Data body: { "name": \<name\>, "items_list": [\<item1\>, \<item2\>, ..] }

Validation:
* name must contains only alphanumeric characters.
* items must contain only numbers and in the string form. (between quotes.)
          
Description: adds the provided list of items in the cart items, if the item already exists then it bypasses the addition of this item.

Response Codes:
* 201: Items added successfully.
* 404: Invalid item carteria OR cart name was not found.
* 405: Invalid method.

### 5. /api/delete_items

Allowed Method: PATCH

Data body type: JSON <br>
Data body: { "name": \<name\>, "items_list": [\<item1\>, \<item2\>, ..] }
          
Description: removes the provided list of items in the cart items, if the item already doesn't exist then it bypasses the removal of this item.

Response Codes:
* 202: Items deleted successfully.
* 404: cart name was not found.
* 405: Invalid method.

### 6. /api/delete_cart

Allowed Method: PATCH

Data body type: JSON <br>
Data body: { "name": \<name\> }
          
Description: Deletes the provided cart name from the database.

Response Codes:
* 202: Cart deleted successfully.
* 404: cart name was not found.
* 405: Invalid method.

<hr>
