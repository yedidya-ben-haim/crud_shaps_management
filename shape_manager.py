

class ShapeManager:
    def __init__(self):
        self.shapes = []
        self.load_from_json()

    def create_shape(self, shape):
        self.shapes.append(shape)


    def get_all_shapes(self):
        pass

    def update_shape(self, shape_id, new_data):
        pass

    def delete_shape(self, shape_id):
        pass

    def save_to_json(self):
        pass

    def load_from_json(self):
        pass
