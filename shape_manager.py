import json
from circle import Circle
from rectangle import Rectangle
from square import Square
from circle import Circle
import logging

logger = logging.getLogger(__name__)


class ShapeManager:

    def __init__(self):
        """
            Initializes the ShapeManager, creates an empty list for shapes,
            and loads existing shapes from the JSON file.
        """
        self.shapes = []
        self.load_from_json()
        logger.info("ShapeManager initialized")

    def create_shape(self, shape_dic: dict) -> object:
        """
        Creates a new shape object from a dictionary,
        adds it to the shapes list.
        """
        try:
            if shape_dic["shape_type"] == "rectangle":
                new_shape = Rectangle(shape_dic["id"], shape_dic["width"], shape_dic["height"])
            elif shape_dic["shape_type"] == "circle":
                new_shape = Circle(shape_dic["id"], shape_dic["radius"])
            elif shape_dic["shape_type"] == "square":
                new_shape = Square(shape_dic["id"], shape_dic["side"])
            else:
                logger.error("Shape type not recognized")
                raise ValueError("Shape type not recognized")

            logger.info("Creating new shape: {%s}", new_shape)
            self.shapes.append(new_shape)
            logger.info("Shape: {%s} append to the shape list", new_shape)

            return new_shape



        except ValueError as e:
            # טיפול בשגיאות של ערכים לא חוקיים שהוזנו
            logger.exception("ValueError occurred: %s", e)
            print(f"\n Error in entered values: {e}")
            return None


        except KeyError as e:

            # טיפול בשגיאה שבה חסרים נתונים במילון (למשל, אין מפתח 'radius' עבור מעגל)
            logger.exception("KeyError occurred, missing data: %s", e)
            print(f"\nMissing data {e} to create the shape")
            return None

    def get_all_shapes(self):
        """
            Returns the list of all geometric shapes currently stored in the system.
        """
        pass

    def update_shape(self, shape_id, new_data: int | float):
        """
            Finds a shape by its unique ID and updates its properties with the provided new data.
        """
        pass

    def delete_shape(self, shape_id):
        """
            Removes a shape from the manager's list by its ID and updates the JSON file.
        """
        pass

    def save_to_json(self):
        """
            Converts all shape objects into dictionaries and writes them to the shapes JSON file.
        """
        pass

    def load_from_json(self):
        """
            Reads data from the JSON file, reconstructs the appropriate shape objects,
            and populates the shapes list.
        """
        try:
            with open("shapes.json", "r", encoding="utf-8") as file:
                shape_list = json.load(file)
                logger.info("Shapes loaded from JSON")

                for shape in shape_list:
                    self.create_shape(shape)


        except FileNotFoundError:
            logger.exception("File not found")







