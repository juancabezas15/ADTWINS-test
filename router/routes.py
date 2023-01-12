from fastapi import APIRouter
from router.user_requests import UserRequest
from models.dbmodel import User


router = APIRouter(
    prefix="/api",
    tags=["User API Rest"]
)


@router.post("/user", response_model=User)
def create_user(user: User):
    '''
    # Create a new user
    ## This route creates a new user in the database and returns the user created
    The id is not required, it is generated automatically.
    '''
    return UserRequest().create_user(user)


@router.get("/users", response_model=list[User])
def get_all_users():
    '''
    # Get all users
    ## This route returns all users in the database
    '''
    return UserRequest().get_users()


@router.get("/user/{user_id}", response_model=User)
def get_user(user_id: str):
    '''
    # Get a user by id
    ## This route returns a user by id
    '''
    return UserRequest().get_user(user_id)


@router.put("/user/{user_id}", response_model=User)
def update_user(user_id: str, user: User):
    '''
    # Update a user by id
    ## This route updates a user by id
    '''
    return UserRequest().update_user(user_id, user)


@router.delete("/user/{user_id}")
def delete_user(user_id: str):
    '''
    # Delete a user by id
    ## This route deletes a user by id
    '''
    return UserRequest().delete_user(user_id)
