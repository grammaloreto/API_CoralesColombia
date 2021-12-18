
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Text, Optional
from datetime import datetime
from uuid import uuid4 as uuid

app = FastAPI()

corals =[]

# establishing the components of the post model
class Post(BaseModel):
    id: Optional[str]
    name: str
    common_name: str
    notes: Text
    created_at: datetime = datetime.now()
    published_at: Optional[datetime]
    published: bool = False


@app.get('/')
def read_root():
    return {'welcome':'welcome to Corales de Colombia REST api'}

@app.get('/corals')
def get_corals():
    return corals    

@app.post('/corals')
def save_coral(post:Post):
    post.id = str(uuid())
    corals.append(post.dict())
    return corals[-1]

@app.get('/corals/{coral_id}')
def get_coral(coral_id: str):
        for coral in corals:
            if coral["id"] == coral_id:
                     return coral
        raise HTTPException(status_code=404, detail='Coral Not Found')

@app.delete('/corals/{coral_id}')
def delete_coral(coral_id:str):
    for index, coral in enumerate(corals):
             if coral["id"] == coral_id:
                       corals.pop(index)
                       return {'message': 'Coral has been deleted successfully'}
    raise HTTPException(status_code=404, detail='Coral Not Found') 

@app.put('/corals/{coral_id}')
def update_coral(coral_id:str, updatedCoral: Post): 
    for index, coral in enumerate(corals):
        if coral["id"] == coral_id:
                 corals[index]['name'] = updatedCoral.name
                 corals[index]['common_name'] = updatedCoral.common_name
                 corals[index]['notes'] = updatedCoral.notes
                 return {'message': 'Coral has been updated successfully'}
    raise HTTPException(status_code=404, detail='Coral Not Found')     


        