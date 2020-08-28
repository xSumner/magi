from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class People(BaseModel):
    name: str
    age: int
    address: str
    salary: float
    
@app.post('/insert')
async def insert(people: People):
    age_after_10_years = people.age + 10
    msg = f'此人名字叫做：{people.name}，十年后此人年龄：{age_after_10_years}'
    return {'success': True, 'msg': msg}