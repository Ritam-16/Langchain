from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):
    name: str
    age: Optional[int] = None #default value
    email: EmailStr
    cgpa: float = Field(gt=0, lt=10, default=5, description='A decimal value representing the CGPA of the student')

new_student = {'name':'Ritam', 'email':'abd@gmail.com', 'cgpa':'7.8'} # 'age':30
#In Pydantic, type coercion means automatically converting an incoming piece of data into the specific type your model expects

student = Student(**new_student)

print(student)
student_dict = dict(student)
print(student_dict['age'])
student_json = student.model_dump_json()
print(student_json)