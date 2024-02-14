from fastapi import FastAPI

app = FastAPI()

students: dict = {}

students_data = {"id": 0, "name": "", "age": 0, "sex": "", "height": 0.0}


@app.get('/')
def home():
    return "Welcome to the Students Portal"


@app.post("/students")
def create_student(name: str, age: int, sex: str, height: float):
    new_student = students_data.copy()
    new_student["id"] = len(students) + 1
    new_student["name"] = name
    new_student["age"] = age
    new_student["sex"] = sex
    new_student["height"] = height

    students[new_student["id"]] = new_student
    return {"Message": "Student successfully created!", "data": new_student}


@app.get("/students")
def get_all_students():
    return students


@app.get("/students/{id}")
def get_student(id: int):
    student = students.get(id)
    if not student:
        return {"Error": "Student not found!"}
    else:
        return student


@app.put("/students/{id}")
def update_student(id: int, name: str, age: int, sex: str, height: float):
    student = students.get(id)
    if not student:
        return {"Error": "Student not found!"}
    student["name"] = name
    student["age"] = age
    student["sex"] = sex
    student["height"] = height
    return {"Message": "Student updated successfully", "data": student}


@app.delete("/students/{id}")
def delete_student(id: int):
    student = students.get(id)
    if not student:
        return {"Message": "Student not found!"}
    del students[id]
    return {"Message": "Student deleted successfully"}