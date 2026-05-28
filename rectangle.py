from shape import Shape
import logging

logger = logging.getLogger(__name__)


class Rectangle(Shape):
    """
        Represents a rectangle shape, inheriting from the base Shape class.
    """

    def __init__(self, shape_id, width, height) -> None:
        """
            Initializes a new Rectangle instance.
        """
        super().__init__(shape_id, "rectangle")

        # Input Validity Check
        if not isinstance(width, (int, float)) or width <= 0 or \
                not isinstance(height, (int, float)) or height <= 0:
            logger.error("Failed to create rectangle. Invalid width or height: %s", width, height)
            raise ValueError("The length of width or heigh of a rectangle must be a number greater than zero.")

        self.width = width
        self.height = height
        logger.info("shape rectangle with id: -%s- created successfully", shape_id)

    def get_area(self) -> float:
        """
            Calculates the area of the rectangle (width * height).
        """
        return self.width * self.height

    def get_perimeter(self) -> float:
        """
            Calculates the perimeter of the rectangle (2 * (width + height)).
        """
        return (self.width + self.height)*2

    def to_dict(self) -> dict:
        """
            Converts the rectangle properties into a dictionary format.
        """
        return {"id":self.id,
                "shape_type":self.shape_type,
                "width":self.width,
                "height":self.height}