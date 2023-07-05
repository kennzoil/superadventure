from typing import Any
from django.db import models

class User(models.Model):
    username = models.CharField(max_length=30)
    location = models.IntegerField
    held_items = models.CharField # validate_comma_separated_integer_list
    gp = models.IntegerField

    def __init__(self, username, location, held_items, gp):
        self.username = username
        self.location = location
        self.held_items = held_items
        self.gp = gp

class Location(models.Model):
    number = models.IntegerField
    name = models.CharField
    description = models.CharField
    exits = models.CharField # validate_comma_separated_integer_list

    def __init__(self, number, name, description, exits):
        self.number = number
        self.name = name
        self.description = description
        self.exits = exits

class Character(models.Model):
    number = models.IntegerField
    name = models.CharField
    description = models.CharField
    location = models.CharField # validate_comma_separated_integer_list
    is_alive = models.BooleanField

    def __init__(self, number, name, description, location, is_alive):
        self.number = number
        self.name = name
        self.description = description
        self.location = location
        self.is_alive = is_alive

class Item(models.Model):
    number = models.IntegerField
    name = models.CharField
    description = models.CharField

    def __init__(self, number, name, description):
        self.number = number
        self.name = name
        self.description = description
