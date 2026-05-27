import math
from shape import Shape
import logging

logger = logging.getLogger(__name__)


class Circle(Shape):
    """
        Represents a circle shape, inheriting from the base Shape class.
    """

    def __init__(self,shape_id, radius) -> None:
        """
            Initializes a new Circle instance.
        """
        super().__init__(shape_id, "circle")

        # Input Validity Check
        if not isinstance(radius, (int, float)) or radius <= 0:
            logger.error("Failed to create circle. Invalid radius: %s", radius)
            raise ValueError("Error: The length of a radius of a circle must be a number greater than zero.")

        self.radius = radius
        logger.info("shape circle with id: -%s- created successfully", shape_id)


    def get_area(self) -> float:
        """
            Calculates the area of the circle.
        """
        return math.pi*self.radius**2

    def get_perimeter(self):
        """
            Calculates the perimeter.
        """
        return 2*math.pi*self.radius

    def to_dict(self) -> dict:
        """
            Converts the circle properties into a dictionary format.
        """
        return {"id": self.id,
                "shape_type": self.shape_type,
                "radius": self.radius}


