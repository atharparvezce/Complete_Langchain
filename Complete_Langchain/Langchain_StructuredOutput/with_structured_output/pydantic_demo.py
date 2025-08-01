from pydantic import BaseModel, EmailStr, Field
from typing import Optional 

class Student(BaseModel):

    name:str= 'Athar'
    age:Optional[int]=None
    email:EmailStr
    cgpa:float= Field(gt=0, lt=10, default=5, description='A decimal value representation')

 # new_student={'name':'Athar'}

 # new_student={'age':'32'}  # '32' still valid. pydantic will automatically convert it into int 

#new_student={'age':'32', 'email':'abc@gmail.com'} 

# new_student={'age':'32', 'email':'abc@gmail.com','cgpa':8.8 }


new_student={'age':'32', 'email':'abc@gmail.com' }
student=Student(**new_student)

student_dict = dict(student)

print(student_dict['age'])