from fastapi import HTTPException

from schemas.user import user_entity, user_entity_list
from bson import ObjectId
from config.db import conn
from passlib.hash import sha256_crypt
connection = conn.local.users


class UserRequest():

    def create_user(self, user):
        new_user = dict(user)
        del new_user["id"]
        new_user["password"] = sha256_crypt.encrypt(new_user["password"])
        user_id = connection.insert_one(new_user).inserted_id
        user = connection.find_one({"_id": ObjectId(user_id)})
        if user:
            return user_entity(user)

    def get_users(self):
        users = connection.find()
        return user_entity_list(users)

    def get_user(self, user_id):
        user = connection.find_one({"_id": ObjectId(user_id)})
        if user:
            return user_entity(user)
        raise HTTPException(status_code=404, detail="User not found")

    def update_user(self, user_id, user):
        new_user = dict(user)
        new_user["password"] = sha256_crypt.encrypt(new_user["password"])
        connection.find_one_and_update(
            {"_id": ObjectId(user_id)}, {"$set": new_user})
        return user_entity(connection.find_one({"_id": ObjectId(user_id)}))

    def delete_user(self, user_id):
        user = connection.find_one({"_id": ObjectId(user_id)})
        if user:
            connection.delete_one({"_id": ObjectId(user_id)})
            return {"message": "User deleted successfully"}
        raise HTTPException(status_code=404, detail="User not found")
