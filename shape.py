class Shape:
    """
        A base class to represent a generic geometric shape
    """

    def __init__(self, shape_id: int, shape_type: str):
        """
            Initializes a new Shape instance
        """
        self.id = shape_id
        self.shape_type = shape_type

    def get_area(self) -> float:
        """
            Calculates and returns the area of the shape.
            This method should be overridden by subclasses.
        """
        pass

    def get_perimeter(self) -> float:
        """
            Calculates and returns the perimeter of the shape.
            This method should be overridden by subclasses
        """
        pass

    def to_dict(self) -> dict:
        """
            Converts the shape attributes into a dictionary for JSON file.
        """
        pass