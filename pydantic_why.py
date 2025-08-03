from pydantic import BaseModel
from typing import List, Dict

class Patient(BaseModel):
    name: str
    age: int
    weight: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]

def insert_patient_data(patient: Patient):  
    print(patient.name)
    print(patient.age)
    print("Inserted")


def update_patient_data(patient: Patient):  
    print(patient.name)
    print(patient.age)
    print("Inserted")


patient_info = {'name': 'pappu', 'age': 30, 'weight': 75.2, 'married': True, 'allergies':['pollen', 'dust'], 'contact_details':{'email':'abc@gmail.com', 'phone':'2353462'}} 

patient1 = Patient(**patient_info)

#insert_patient_data(patient1)
update_patient_data(patient1)