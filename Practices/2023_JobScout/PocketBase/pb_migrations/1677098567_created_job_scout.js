migrate((db) => {
  const collection = new Collection({
    "id": "0k2sz9jmjznxovl",
    "created": "2023-02-22 20:42:47.566Z",
    "updated": "2023-02-22 20:42:47.566Z",
    "name": "job_scout",
    "type": "base",
    "system": false,
    "schema": [
      {
        "system": false,
        "id": "hmbxqffo",
        "name": "user",
        "type": "relation",
        "required": true,
        "unique": false,
        "options": {
          "maxSelect": 1,
          "collectionId": "_pb_users_auth_",
          "cascadeDelete": true
        }
      },
      {
        "system": false,
        "id": "tbsi9nry",
        "name": "title",
        "type": "text",
        "required": true,
        "unique": false,
        "options": {
          "min": null,
          "max": null,
          "pattern": ""
        }
      },
      {
        "system": false,
        "id": "bafb4ceb",
        "name": "job_url",
        "type": "url",
        "required": true,
        "unique": false,
        "options": {
          "exceptDomains": null,
          "onlyDomains": null
        }
      },
      {
        "system": false,
        "id": "ifqymrhu",
        "name": "cv",
        "type": "file",
        "required": false,
        "unique": false,
        "options": {
          "maxSelect": 1,
          "maxSize": 5242880,
          "mimeTypes": [],
          "thumbs": []
        }
      },
      {
        "system": false,
        "id": "q08wh8t6",
        "name": "questions",
        "type": "text",
        "required": false,
        "unique": false,
        "options": {
          "min": null,
          "max": null,
          "pattern": ""
        }
      },
      {
        "system": false,
        "id": "h4q6ottr",
        "name": "notes",
        "type": "text",
        "required": false,
        "unique": false,
        "options": {
          "min": null,
          "max": null,
          "pattern": ""
        }
      },
      {
        "system": false,
        "id": "m5uydbo2",
        "name": "stage",
        "type": "select",
        "required": true,
        "unique": false,
        "options": {
          "maxSelect": 1,
          "values": [
            "Submitted",
            "Accepted",
            "Rejected"
          ]
        }
      }
    ],
    "listRule": "",
    "viewRule": "",
    "createRule": "",
    "updateRule": "",
    "deleteRule": "",
    "options": {}
  });

  return Dao(db).saveCollection(collection);
}, (db) => {
  const dao = new Dao(db);
  const collection = dao.findCollectionByNameOrId("0k2sz9jmjznxovl");

  return dao.deleteCollection(collection);
})
