#!/usr/bin/python3

"""class City inheriting from BaseModel"""
from models.base_model import BaseModel


class City(BaseModel):
    """public class attribute"""
    state_id = ""
    name = ""
