#!/usr/bin/python3

import json
import os


class FileStorage():
    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        pass

    def all(self):
        return self.__objects

    def new(self, obj):
        obj_name = type(obj).__name__
        obj_id = obj.id
        FileStorage.__objects[obj_name + "." + obj_id] = obj

    def save(self):
        with open(FileStorage.__file_path, "w") as f:
            f.write(json.dumps(FileStorage.__objects))

    def reload(self):
        if not os.path.isFile(FileStorage.__objects):
            return
        with open(FileStorage.__file_path) as f:
            if (f.read()):
                FileStorage.__objects = json.loads(f.read())
     def attributes(self):

        """Returns the valid attributes and their types for classname"""

        attributes = {

            "BaseModel":

                     {"id": str,

                      "created_at": datetime.datetime,

                      "updated_at": datetime.datetime},

            "User":

                     {"email": str,

                      "password": str,

                      "first_name": str,

                      "last_name": str},

            "State":

                     {"name": str},

            "City":

                     {"state_id": str,

                      "name": str},

            "Amenity":

                     {"name": str},

            "Place":

                     {"city_id": str,

                      "user_id": str,

                      "name": str,

                      "description": str,

                      "number_rooms": int,

                      "number_bathrooms": int,

                      "max_guest": int,

                      "price_by_night": int,

                      "latitude": float,

                      "longitude": float,

                      "amenity_ids": list},

            "Review":

            {"place_id": str,

                         "user_id": str,

                         "text": str}

        }

        return attributes
