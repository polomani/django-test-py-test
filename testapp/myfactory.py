import factory 
from testapp.models import Person, Group 

class GroupFactory(factory.Factory): 
    class Meta:
        model = Group
    name = 'Developers'

class PersonFactory(factory.Factory): 
    class Meta:
        model = Person
    first_name = 'John' 
    last_name = 'Doe' 
    group = factory.SubFactory(GroupFactory)
