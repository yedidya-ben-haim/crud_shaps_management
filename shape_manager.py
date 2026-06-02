import json

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

            logger.info("Creating new shape: %s", new_shape.to_dict())
            # print(f"""--- New Shape ---
            #         {new_shape.to_dict()}
            #         added successfully""")
            self.shapes.append(new_shape)
            logger.info("Shape: -%s- %s append to the shape list", new_shape.id, new_shape.shape_type)

            return new_shape
        except ValueError as e:
            # טיפול בשגיאות של ערכים לא חוקיים שהוזנו
            logger.error("ValueError occurred: %s", e)
            raise ValueError (f"\n Error in entered values: {e}")

        except KeyError as e:
            # טיפול בשגיאה שבה חסרים נתונים במילון (למשל, אין מפתח 'radius' עבור מעגל)
            logger.warning("KeyError occurred, missing data: %s", e)
            raise KeyError(f"Missing data {e} to create the shape")

    def get_all_shapes(self):
        """
            Returns the list of all geometric shapes currently stored in the system
            and prints their details.
        """
        if not self.shapes:
            # print("No shapes found in the system.")
            logger.warning("No shapes found in the system.")
            return []
        return self.shapes
        # print("\n--- All Shapes ---")
        # for shape in self.shapes:
        #     # # print id and type
        #     # print(f"ID: {shape.id}")
        #     # print(f"Type: {shape.shape_type.capitalize()}")
        #     #
        #     # shape_dict = shape.to_dict()
        #     # for key, value in shape_dict.items():
        #     #     if key not in ["id", "shape_type"]: # type מעבר רק על השאר הנתונים שהם לא id
        #     #         print(f"{key.capitalize()}: {value}")
        #     #         logger.info(f"shape %s %s was printed", shape.id, shape.shape_type)
        #     # print(f"Area: {shape.get_area():.2f}")
        #     # print(f"Perimeter: {shape.get_perimeter():.2f}")
        #     # print(f"--------------------")


        return self.shapes

    def update_shape(self, shape_id, new_data: tuple):
        """
            Finds a shape by its unique ID and updates its properties with the provided new data.
        """
        for shape in self.shapes:
            if shape.id == shape_id:
                if shape.shape_type == "rectangle":
                    shape.width = new_data[0]
                    shape.height = new_data[1]
                elif shape.shape_type == "circle":
                    shape.radius = new_data[0]
                elif shape.shape_type == "square":
                    shape.side = new_data[0]
                logger.info("Shape: %s %s updated successfully", shape.id, shape.shape_type)
                return shape
        return None

    def delete_shape(self, shape_id) -> bool:
        """
            Removes a shape from the manager's list by its ID and updates the JSON file.
        """

        for shape in self.shapes:
            if shape.id == shape_id:
                self.shapes.remove(shape)
                logger.info("Shape: %s removed successfully", shape.to_dict())
                return True
        return False


    def save_to_json(self):
        """
            Converts all shape objects into dictionaries and writes them to the shapes JSON file.
        """
        try:
            # 1. יצירת רשימה של מילונים מתוך רשימת האובייקטים של הצורות
            # אנחנו משתמשים בפונקציית to_dict שנמצאת בכל צורה כדי לקבל את הנתונים שלה
            shapes_data = [shape.to_dict() for shape in self.shapes]

            # 2. פתיחת קובץ ה-JSON למצב כתיבה ("w") ושמירת הנתונים
            with open("shapes.json", "w", encoding="utf-8") as file:
                # indent=4 דואג שהקובץ יישמר עם ירידות שורות והזחות כדי שיהיה קריא לבני אדם
                json.dump(shapes_data, file, indent=4)

            # רישום בלוג והדפסה למשתמש שהפעולה הצליחה
            logger.info("Successfully saved %s shapes to JSON.", len(self.shapes))
            print("\nAll shapes have been successfully saved to shapes.json")

        except Exception as e:

            logger.exception("Failed to save shapes to JSON: %s", e)
            print(f"\nAn error occurred while saving to JSON: {e}")

    def load_from_json(self):
        """
            Reads data from the JSON file, reconstructs the appropriate shape objects,
            and populates the shapes list.
        """
        try:
            with open("shapes.json", "r", encoding="utf-8") as file:
                shape_list = json.load(file)

                for shape in shape_list:
                    try:
                        self.create_shape(shape)
                    except (ValueError, KeyError) as e:
                        logger.warning("Skipping on invalid shape in JSON, Error: %s", e)
                logger.info("Data loaded successfully from JSON file.")

        except FileNotFoundError:
            logger.warning("shapes.json file not found. Starting with an empty list.")
            self.shapes = []

        except json.decoder.JSONDecodeError:
            logger.warning("shapes.json is empty or invalid. Starting with an empty list.")
            self.shapes = []

    def get_shape_by_id(self, shape_id):
        for shape in self.shapes:
            if shape.id == shape_id:
                return shape
        return None

    def get_new_id(self):
        """Returns a new, free ID."""
        max_id = 0

        for shape in self.shapes:
            if shape.id > max_id:
                max_id = shape.id
        new_id = max_id + 1
        logger.info(f"New ID find: {new_id}")
        return new_id

    def get_total_area(self):
        """
            Return the total area of all shapes
        """
        sum_of_area = 0

        for shape in self.shapes:
            sum_of_area += shape.get_area()
        return sum_of_area






