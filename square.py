from shape import Shape
import logging

logger = logging.getLogger(__name__)



class Square(Shape):
    """
        Represents a square shape, inheriting from the base Shape class.
    """
    def __init__(self, shape_id: int, side: int):
        """
            Initializes a new Square instance.
        """
        super().__init__(shape_id, "square")

        # Input Validity Check
        if not isinstance(side, (int, float)) or side <= 0:
            logger.error("Failed to create square. Invalid side: %s", side)
            raise ValueError("Error: The length of a side of a square must be a number greater than zero.")

        self.side = side
        logger.info("shape square with id: -%s- created successfully", shape_id)


    def get_area(self):
        """
            Calculates the area of the square.
        """
        logger.info("")
        return self.side * self.side


    def get_perimeter(self):
        """
            Calculates the perimeter of the square.
        """
        return self.side * 4


    def to_dict(self):
        """
            Converts the square properties into a dictionary format.
        """
        return {"id":self.id,
                "shape_type":self.shape_type,
                "side":self.side}

