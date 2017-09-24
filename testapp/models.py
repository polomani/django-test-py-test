from django.db import models

class Group(models.Model): 
    name = models.TextField() 

class Person(models.Model): 
    first_name = models.TextField() 
    last_name = models.TextField() 
    group = models.ForeignKey(Group) 
    def group_letter(self): 
        return self.group.name[0].upper()
