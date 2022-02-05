from fastapi import FastAPI,Path
from pydantic import BaseModel

from myapi import Student
app = FastAPI()

employees = {
    1: {
        "name": "tawfeeq" ,
        "email": "tawfeeq@gmail.com",
        "major": "BackEnd web dev",
        "salary": 999999999
    }
}
class Employee(BaseModel):
    name: str
    email: str
    major: str
    salary: int
class UpdateEmployee(BaseModel):
    name: str = None
    email: str = None
    major: str = None
    salary: int = None

@app.get("/get-employees")
def getAll():
    return employees

@app.get("/get-employee/{id}")
def get_student(id: int = Path(None,description="The ID of the employee you want to view" , gt = 0)):
    return employees[id]

@app.get("/get-by-name")
def get_employee(name: str = None):
    for id in employees:
        if employees[id]["name"] == name:
            return employees[id]
    return{"Data": "Not Found"}

@app.post("/create-employee/{id}")
def createStudent(id: int , employee : Employee):
    if id in employees:
        return{"Error": {"Employee exists"}}
    employees[id] = employee
    return employees[id]

@app.put("/update-employee/{id}")
def UpdateEmployee(student_id: int , employee: UpdateEmployee):
    if id in employees:
        return {"Error": "This Student does not exist"}
    if employee.name != None:

        employees[id].name=employee.name
    if employee.major != None:
        employees[id].major = employee.major
    if employees[id].email != None:
        employees[id].email = employee.email
    if employees[id].salary != None:
        employees[id].salary = employee.salary
    
    return employees[id]

@app.delete("/delete-employee/{id}")
def delete_employee(id: int):
    if id not in employees:
        return {"Error": "Cant Find The Employee"}
    del employees[id]
    return {"Data": "Employee Deleted Succseesfuly"}
