#!/usr/bin/python3
"""Module for Base class"""
import json
import csv
import turtle


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
            write = csv.writer(f)
            for ob in list_objs:
                if cls.__name__ == "Rectangle":
                    write.writerow([ob.id, ob.width, ob.height, ob.x, ob.y])
                elif cls.__name__ == "Square":
                    write.writerow([ob.id, ob.size, ob.x, ob.y])

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

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw Rectangles and Squares using the turtle module.
        Args:
            list_rectangles (list): A list of Rectangle objects to draw.
            list_squares (list): A list of Square objects to draw.
        """
        turt = turtle.Turtle()
        turt.screen.bgcolor("#b7312c")
        turt.pensize(3)
        turt.shape("turtle")

        turt.color("#ffffff")
        for rect in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rect.x, rect.y)
            turt.down()
            for i in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)
            turt.hideturtle()

        turt.color("#b5e3d8")
        for sq in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(sq.x, sq.y)
            turt.down()
            for i in range(2):
                turt.forward(sq.width)
                turt.left(90)
                turt.forward(sq.height)
                turt.left(90)
            turt.hideturtle()

        turtle.exitonclick()
