#Paint Shop Management
#Performs
#As an Paint Admin
# 1- Viewing paint
# 2- Adding paint
# 3- Updating paint
# 4- Delete paint


from fastapi import FastAPI,status,HTTPException
from pydantic import BaseModel

app=FastAPI()

#Root
@app.get("/")
def root():
    return "Welcome to Indian Paints"

Todos ={
    1 : {
        "Colour" :"Red",
        "quantity":200
       },
    2 : {
        "Colour" :"Blue",
        "quantity":250
       },
    3 : {
        "Colour" :"Green",
        "quantity":300
       }  
    
}

#request body schema
class TodoItem(BaseModel):
    Colour: str
    quantity : float

#1.view all the existing Paint
@app.get("/todos",status_code=status.HTTP_200_OK)
def get_all_paint_items(Colour: str=""):
    results = {}
    if Colour != "" or Colour != None:
        for id in Todos:
            if Colour in Todos[id]["Colour"]:
                results[id]=Todos[id]
    else:
        results=Todos          
    return results

@app.get("/todos/{id}", status_code=status.HTTP_200_OK)
def get_paint_item(id: int):
    if id in Todos:
        return Todos[id]

    return HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail ="item not found")    


#2.Create / Add Paint
@app.post("/todos",status_code=status.HTTP_201_CREATED)
def add_paint_item(paint_item: TodoItem):
    id=max(Todos)+1
    Todos[id]= paint_item.dict()
    return Todos[id]

#3.Update Paint
@app.put("/todos/{id}",status_code=status.HTTP_200_OK)
def update_paint_item(id:  int,paint_item: TodoItem):
    if id in Todos :
        Todos[id]=paint_item.dict()
        return Todos[id]
    return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found") 

#4.Delete Paint
@app.delete("/todos/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_paint_item(id: int):
    if id in Todos :
        Todos.pop(id)
        return 
    return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found") 

