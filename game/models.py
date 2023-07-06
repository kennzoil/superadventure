from typing import Any
from django.db import models

class User(models.Model):
    username = models.CharField(max_length=30, db_column='name')
    location = models.IntegerField(db_column='location')
    held_items = models.TextField(db_column='held_items') # validate_comma_separated_integer_list
    gp = models.IntegerField(db_column='gp')

    # def __init__(self, username, location, held_items, gp):
    #     self.username = username
    #     self.location = location
    #     self.held_items = held_items
    #     self.gp = gp

class Location(models.Model):
    number = models.IntegerField(db_column='number')
    name = models.CharField(max_length=30, db_column='name')
    description = models.TextField(db_column='description')
    exits = models.CharField(max_length=30, db_column='exits') # validate_comma_separated_integer_list

    # def __init__(self, number, name, description, exits):
    #     self.number = number
    #     self.name = name
    #     self.description = description
    #     self.exits = exits

class Character(models.Model):
    number = models.IntegerField(db_column='number')
    name = models.CharField(max_length=30, db_column='name')
    description = models.TextField(db_column='description')
    location = models.CharField(max_length=30, db_column='location') # validate_comma_separated_integer_list
    is_alive = models.BooleanField(db_column='is_alive')

    # def __init__(self, number, name, description, location, is_alive):
    #     self.number = number
    #     self.name = name
    #     self.description = description
    #     self.location = location
    #     self.is_alive = is_alive

class Item(models.Model):
    number = models.IntegerField(db_column='number')
    name = models.CharField(max_length=30, db_column='name')
    description = models.TextField(db_column='description')

    # def __init__(self, number, name, description):
    #     self.number = number
    #     self.name = name
    #     self.description = description
