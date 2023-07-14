#!/usr/bin/python3

"""class Review inheriting from BaseModel"""
from models.base_model import BaseModel


class Review(BaseModel):
    """public class attributes"""
    place_id = ""
    user_id = ""
    text = ""
