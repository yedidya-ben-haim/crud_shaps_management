

class ShapeManager:

    def __init__(self):
        """
            Initializes the ShapeManager, creates an empty list for shapes,
            and loads existing shapes from the JSON file.
            """
        self.shapes = []
        self.load_from_json()

    def create_shape(self, shape):
        """
            Adds a new shape object to the manager's list
            and saves the updated list to the JSON file.
        """

    def get_all_shapes(self):
        """
            Returns the list of all geometric shapes currently stored in the system.
        """
        pass

    def update_shape(self, shape_id, new_data):
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
            Reads data from the JSON file, reconstructs the appropriate shape objects, and populates the shapes list.
        """
        pass
