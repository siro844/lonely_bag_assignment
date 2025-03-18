from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from utils.users import users
from models.users import UserRequest, UserResponse, UserUpdateRequest
from fuzzywuzzy import fuzz


router = APIRouter()

@router.post('/', response_model=UserResponse)
async def create_users(request: UserRequest):
    try:
        user_data = request.model_dump()
        users.append(user_data)
        return JSONResponse(status_code=201, content=user_data)
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})



@router.get('/search', response_model=list[UserResponse])
async def get_user_by_name(name: str):
    filtered_users = []
    print(users)
    for user in users:
        similarity = fuzz.partial_ratio(name.lower(), user["name"].lower())
        if similarity > 70:
            filtered_users.append(user)
    
    if not filtered_users:
        raise HTTPException(status_code=404, detail="No users found")
    
    return filtered_users
    
@router.get('/{id}', response_model=UserResponse)
async def get_user_by_id(id: str):
    user = next((user for user in users if user["id"] == id), None)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user



@router.put('/{id}', response_model=UserResponse)
async def update_user(id: str, request: UserUpdateRequest):
    for index, user in enumerate(users):
        if user["id"] == id:
            updated_user = user.copy()
            updated_user.update(request.model_dump(exclude_unset=True))
            users[index] = updated_user
            return users[index]
    raise HTTPException(status_code=404, detail="User not found")


@router.delete('/{id}')
async def delete_user(id: str):
    global users
    users = [user for user in users if user["id"] != id]
    return JSONResponse(status_code=200, content={"message": "User deleted successfully"})
