from shape import Shape
    """
    Represents a rectangle shape, inheriting from the base Shape class.
    """
class Rectangle(Shape):

    def __init__(self, shape_id, shape_type, width, height) -> None:
        """
            Initializes a new Rectangle instance.
        """
        super().__init__(shape_id, shape_type)
        self.width = width
        self.height = height

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
                "type":self.shape_type,
                "width":self.width,
                "height":self.height}





