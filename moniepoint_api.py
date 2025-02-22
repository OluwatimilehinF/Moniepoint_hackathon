from fastapi import FastAPI
from pydantic import BaseModel
from Oluwatimilehin_Folarin_Moniepoint_hackathon import trans_files_processing
from fastapi.middleware.cors import CORSMiddleware
import os
import uvicorn

class FolderPath(BaseModel):
    path:str


app = FastAPI(title = ' To build analytics software that reads through transactions files and returns some metrics'
              , 
            description = ''' Remember to use **DOUBLE** backslash for the directory folder.

NOTE:            
This analytical app will return the following: Highest sales volume in a day,
Highest sales value in a day,
Most sold product ID by volume,
Highest sales staff ID for each mont, and
Highest hour of the day by average transaction volume
 '''
 )

#This will allow request from front end developer to work on. That is, allow request from any domain.
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials = True,
    allow_methods =["*"],
    allow_headers = ["*"] )


@app.get("/")

def home():
    return{"message": "API is running as analytics software app"}

@app.post("/process")
def processing(request: FolderPath):
    folder = request.path
    if not os.path.isdir(folder):
        return {"ERROR, invalid folder directory"}
    
    result = trans_files_processing(folder)
    return result


#run
if __name__ == '__main__':
    uvicorn.run(app)
    

   
