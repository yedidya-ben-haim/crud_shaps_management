from fastapi import FastAPI
from shape_manager import ShapeManager


app = FastAPI()

# Initialize the shape list
manager = ShapeManager()

@app.get("/")
def home():
    return {"Welcome":"For the crud shaps project"}


@app.get("/shapes")
def all_shape():
    return manager.get_all_shapes()



# TODO ברגע שהשרת נסגר לכתוב לקובץ