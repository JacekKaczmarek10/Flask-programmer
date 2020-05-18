import pytest
import math_func
import app

@pytest.mark.number
def test_add():
    assert math_func.add(7,3) == 10
    assert math_func.add(7) == 9
    assert math_func.add(5) == 7
    print(math_func.add(7,3), '-----------------')

@pytest.mark.number
def test_product():
    assert math_func.product(5, 5) == 25
    assert math_func.product(5) == 10   

@pytest.mark.strings
def test_add_strings():
    result = math_func.add('Hello ','World')
    assert result == 'Hello World'
    assert type(result) is str
    assert 'Hello' in result

@pytest.mark.strings
def test_product_strings():
    assert math_func.product('Hello ', 3) == 'Hello Hello Hello '
    result = math_func.product('Hello ')
    assert result == 'Hello Hello '
    assert type(result) is str

@pytest.mark.strings
def test_product_strings():
    assert math_func.product('Hello ', 3) == 'Hello Hello Hello '
    result = math_func.product('Hello ')
    assert result == 'Hello Hello '
    assert type(result) is str

@pytest.fixture(scope='module')
def init_database():
    # Create the database and the database table
    db.create_all()
 
    # Insert user data
    user1 = User(email='patkennedy79@gmail.com', plaintext_password='FlaskIsAwesome')
    user2 = User(email='kennedyfamilyrecipes@gmail.com', plaintext_password='PaSsWoRd')
    db.session.add(user1)
    db.session.add(user2)
 
    # Commit the changes for the users
    db.session.commit()
 
    yield db  # this is where the testing happens!
 
    db.drop_all()