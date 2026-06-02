from fastapi import FastAPI, HTTPException
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


@app.get("/shapes/total-area")
def total_area():
    area = manager.get_total_area()
    round_area = round(area, 2)
    return {"total_shapes_area": round_area}


@app.get("/shapes/{id}")
def get_shape_by_id(id: int):
    shape = manager.get_shape_by_id(id)

    if shape is None:
        raise HTTPException(status_code=404, detail="Shape not found")
    return shape.to_dict()










# TODO ברגע שהשרת נסגר לכתוב לקובץ