from fastapi import FastAPI, Response, status, HTTPException
from pydantic import BaseModel
from random import randrange
import datetime

app = FastAPI()


class Emp(BaseModel):
    name: str
    company: str
    place: str
    joining_date: datetime.date = datetime.datetime.now().date()


emps = [
    {"id": 1, "name": "Arun", "company": "Company1", "place": "Chennai",
     "joining_date": datetime.datetime.now().date()},
    {"id": 2, "name": "Antostalin", "company": "Company2", "place": "Bangalore",
     "joining_date": datetime.datetime.now().date()}
]


def find_emp(id):
    for emp in emps:
        if emp['id'] == id:
            return emp


def find_emp_index(id):
    for i, emp in enumerate(emps):
        if emp['id'] == id:
            return i


@app.get("/")
async def root():
    return {"message": "Hello World!!"}


@app.get("/emp")
def get_emps():
    print('emp_list')
    return {"data": emps}


@app.get("/emp/{id}")
def get_emp(id: int):
    emp = find_emp(id)
    if emp is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="{} is not a valid employee id".format(id))

    return {"data": emp}


@app.post("/emp", status_code=status.HTTP_201_CREATED)
def create_emp(emp: Emp):
    emp = emp.dict()
    emp['id'] = randrange(3, 1000)
    emps.append(emp)
    return {"data": emp}


@app.put("/emp/{id}")
def update_emp(id: int, emp: Emp):
    index = find_emp_index(id)
    if index is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="{} is not a valid employee id".format(id))
    emp = emp.dict()
    emp['id'] = id
    emps[index] = emp
    return {"data": emp}


@app.delete("/emp/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_emp(id: int):
    index = find_emp_index(id)
    if index is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="{} is not a valid employee id".format(id))
    emps.pop(index)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
