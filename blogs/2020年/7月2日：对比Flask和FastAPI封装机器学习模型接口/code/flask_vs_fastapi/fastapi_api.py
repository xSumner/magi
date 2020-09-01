from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import traceback
import pandas as pd
import numpy as np

app = FastAPI()

class People(BaseModel):
    model_name: str
    input: list
    
@app.post('/predict')
async def predict(people: People):
    try:
        data = people.input
        lr = joblib.load("model.pkl")
        model_columns = joblib.load("model_columns.pkl")
        query = pd.get_dummies(pd.DataFrame(data))
        query = query.reindex(columns=model_columns, fill_value=0)
        prediction = list(lr.predict(query))
        print(prediction)
        return {'success': True, 'prediction': str(prediction)}
    except:
        return {'success': False, 'trace': traceback.format_exc()}