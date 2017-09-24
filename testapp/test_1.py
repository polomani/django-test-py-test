import pytest

from testapp.myfactory import PersonFactory 

def test_hello_world(client):
    response = client.get('/testapp/');
    assert response.status_code == 200
    assert response.content == b'Hello, world!'

def test_group_letter(): 
    person = PersonFactory.build(group__name='admins') 
    assert person.group_letter() == 'A'

@pytest.mark.django_db
def test_group_letter_create(): 
    person = PersonFactory.create(group__name='admins') 
    assert person.group_letter() == 'A'

   