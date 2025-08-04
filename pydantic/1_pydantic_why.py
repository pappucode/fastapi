from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    name: Annotated[str, Field(max_length=50, title = 'name of the patient', description='Give the name of the patient in less than 50 chars', examples=['Pappu', 'Rabiul Islam'])]
    email: EmailStr
    linkedin_url: AnyUrl
    age: int = Field(gt=0, lt=120)
    weight: Annotated[float, Field(gt=0, strict=True)]
    married: Annotated[bool, Field(default=None, description='Is the patient married or not')]
    allergies: Annotated[Optional[List[str]], Field(default=None, max_length=5)]
    contact_details: Dict[str, str]

    @field_validator('email')
    @classmethod
    def email_validator(cls, value):

        valid_domains = ['hdfc.com', 'icici.com']
        # abc@gmail.com
        domain_name = value.split('@')[-1]

        if domain_name not in  valid_domains:
            raise ValueError('Not a valid domain')
        
        return value
    

    @field_validator('name')
    @classmethod
    def transform_name(cls, value):
        return value.upper()

def insert_patient_data(patient: Patient): 
    print(patient.name)
    print(patient.email)
    print(patient.age)
    print(patient.married)
    print(patient.allergies)
    print("Inserted")

def update_patient_data(patient: Patient):  
    print(patient.name)
    print(patient.email)
    print(patient.age)
    print(patient.married)
    print(patient.allergies)
    print(patient.weight)
    print("Updated")

patient_info = {'name': 'pappu', 'email': 'abc@icici.com', 'linkedin_url': "https://www.linkedin.com/", 'age': 30, 'weight': 75.2, 'married': True, 'contact_details':{'email':'abc@gmail.com', 'phone':'2353462'}} 

patient1 = Patient(**patient_info)

#insert_patient_data(patient1)
update_patient_data(patient1)