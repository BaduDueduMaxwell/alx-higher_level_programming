#!/usr/bin/python3
"""Module for Base class"""
import json
import csv


class Base:
    """Base class for managing id attribute"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialization of Base instance"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @classmethod
    def create(cls, **dictionary):
        """Return instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)  # Dummy instance
        elif cls.__name__ == "Square":
            dummy = cls(1)  # Dummy instance
        else:
            return None
        dummy.update(**dictionary)
        return dummy

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list dict"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list obj to a file"""
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".json"
        with open(filename, "w") as file:
            json_str = cls.to_json_string(
                [obj.to_dictionary() for obj in list_objs]
            )
            file.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string"""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, mode="r", encoding="utf-8") as file:
                objs = cls.from_json_string(file.read())
                return [cls.create(**obj) for obj in objs]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serialize list_objs to CSV file"""
        filename = cls.__name__ + ".csv"
        with open(filename, mode='w', encoding='utf-8') as f:
            writer = csv.writer(f)
            for obj in list_objs:
                if cls.__name__ == "Rectangle":
                    writer.writerow([obj.id, obj.width, obj.height, obj.x, obj.y])
                elif cls.__name__ == "Square":
                    writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """Deserialize CSV file to list of instances"""
        filename = cls.__name__ + ".csv"
        instances = []
        try:
            with open(filename, mode='r', encoding='utf-8') as f:
                reader = csv.reader(f)
                for row in reader:
                    row = [int(x) for x in row]
                    if cls.__name__ == "Rectangle":
                        instance = cls(row[1], row[2], row[3], row[4], row[0])
                    elif cls.__name__ == "Square":
                        instance = cls(row[1], row[2], row[3], row[0])
                    instances.append(instance)
            return instances
        except FileNotFoundError:
            return []
