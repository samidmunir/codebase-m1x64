from django.db import models

"""
    Model is a way of "modeling" information.
    - add attributes & methods
"""

# Create your models here.

# Creating a database model called ToDoList
class ToDoList(models.Model):
    name = models.CharField(max_length = 200)
    
    def __str__(self):
        return self.name
    

class Item(models.Model):
    todolist = models.ForeignKey(ToDoList, on_delete = models.CASCADE)
    text = models.CharField(max_length = 300)
    complete = models.BooleanField(default = False)
    
    def __str__(self):
        return self.text