#!/usr/bin/python3

"""Base class for all other classes"""
import json


class Base():
    """The parent class of this project"""
    __nb_objects = 0

    def __init__(self, id=None):
        """init function"""
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or "":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            rec = cls(1, 2, 3, 4)
            rec.update(**dictionary)
            return rec
        else:
            squ = cls(2, 3, 4)
            squ.update(**dictionary)
            return squ
        """if "size" in dictionary:
            squ = cls(2, 3, 4)
            squ.update(**dictionary)
            return squ
        else:
            rec = cls(1, 2, 3, 4)
            rec.update(**dictionary)
            return rec"""

    @classmethod
    def save_to_file(cls, list_objs):
        path = ""
        if cls.__name__ == "Rectangle":
            path = "Rectangle.json"
        elif cls.__name__ == "Square":
            path = "Square.json"

        with open(path, "w", encoding="utf-8") as a_file:
            if list_objs is None:
                b = cls.to_json_string([])
                a_file.write(b)
                return
            else:
                dic = [x.to_dictionary() for x in list_objs]
                b = cls.to_json_string(dic)
                a_file.write(b)
                return
