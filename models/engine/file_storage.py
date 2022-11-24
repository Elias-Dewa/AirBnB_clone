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
