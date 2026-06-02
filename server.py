from fastapi import FastAPI, HTTPException
from shape_manager import ShapeManager
from pydantic import BaseModel
from typing import Optional



class ShapeCreate(BaseModel):
    shape_type: str

    side: Optional[float] = None
    radius: Optional[float] = None
    width: Optional[float] = None
    height: Optional[float] = None



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
    if not manager.shapes:
        raise HTTPException(status_code=404, detail="No shapes found to calculate area")

    area = manager.get_total_area()
    round_area = round(area, 2)
    return {"total_shapes_area": round_area}

@app.get("/shapes/count")
def get_shape_count():
    total_shape = len(manager.shapes)
    return {"total shape:": total_shape}

@app.get("/shapes/type/{type}")
def get_shape_by_type(type: str):
    shape_of_type = []
    for shape in manager.shapes:
        if shape.shape_type == type:
            shape_of_type.append(shape.to_dict())
    return shape_of_type



@app.get("/shapes/{id}")
def get_shape_by_id(id: int):
    shape = manager.get_shape_by_id(id)

    if shape is None:
        raise HTTPException(status_code=404, detail="Shape not found")
    return shape.to_dict()


@app.post("/shapes", status_code=201)
def create_shape(shape_dic: ShapeCreate):
    id = manager.get_new_id()

    shape_dic = shape_dic.model_dump(exclude_unset=True)

    shape_dic["id"] = id
    new_shape = manager.create_shape(shape_dic)
    manager.save_to_json()
    return new_shape.to_dict()


@app.put("/shapes/{id}")
def update_shape(id: int,new_data: dict):
    new_data = tuple(new_data.values())
    update_shape = manager.update_shape(id,new_data)
    if update_shape is None:
        raise HTTPException(status_code=404, detail="Error in shape update")
    manager.save_to_json()
    return updated_shape.to_dict()

@app.delete("/shapes/{id}")
def delete_shape(id: int):
    status_of_delete = manager.delete_shape(id)
    if status_of_delete is False:
        raise HTTPException(status_code=404, detail=f"Deletion of shape {id} failed.")
    manager.save_to_json()


