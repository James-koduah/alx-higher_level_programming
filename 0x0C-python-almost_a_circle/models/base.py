#!/usr/bin/python3

"""Base class for all other classes"""
import json
import csv

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
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                rec = cls(1, 3)
                rec.update(**dictionary)
                return rec
            else:
                squ = cls(2)
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

    @classmethod
    def load_from_file(cls):
        path = ""
        if cls.__name__ == "Rectangle":
            path = "Rectangle.json"
        elif cls.__name__ == "Square":
            path = "Square.json"

        try:
            with open(path) as a_file:
                b = a_file.read()
                items = cls.from_json_string(b)
                last = [cls.create(**i) for i in items]
                return last
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ Serialize an object to csv format"""
        path = cls.__name__ + ".csv"
        with open(path, "w", newline="") as a_file:
            if list_objs and list_objs != []:

                if cls.__name__ == "Rectangle":
                    fieldnames = ['id', 'width', 'height', 'x', 'y']
                else:
                    fieldnames = ['id', 'size', 'x', 'y']

                writer = csv.DictWriter(a_file, fieldnames=fieldnames)
                for i in list_objs:
                    writer.writerow(i.to_dictionary())
            else:
                a_file.write("[]")

    @classmethod
    def load_from_file_csv(cls):
        """ Deserialize an object from a csv file"""
        path = cls.__name__ + ".csv"
        try:
            with open(path, 'r', newline="") as a_file:
                if cls.__name__ == "Rectangle":
                    fieldnames = ['id', 'width', 'height', 'x', 'y']
                else:
                    fieldnames = ['id', 'size', 'x', 'y']

                csv_r = csv.DictReader(a_file, fieldnames=fieldnames)
                final = []
                for row in csv_r:
                    for k, v in row.items():
                        row[k] = int(v)
                    final.append(row)
                return [cls.create(**item) for item in final]
        except IOError:
            pass
