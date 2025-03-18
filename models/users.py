from pydantic import BaseModel,constr
from typing import Optional

class UserRequest(BaseModel):
    id: str
    name: str
    phone_no: constr(pattern=r'^\+91\d{10}$')
    address: str
    
class UserResponse(BaseModel):
    name:str
    phone_no:str
    address:str
    
    
class UserUpdateRequest(BaseModel):
    name:Optional[str]=None
    phone_no: Optional[constr(pattern=r'^\+91\d{10}$')] = None
    address:Optional[str]=None
