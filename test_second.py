from app import db, Assistant
import pytest
import math_func

@pytest.mark.number
def test_add():
    assert math_func.add(7,3) == 10
    assert math_func.add(7) == 9
    assert math_func.add(5) == 7
    print(math_func.add(7,3), '-----------------')

@pytest.mark.number
def init_database():
    # Create the database and the database table
    db.create_all()
 
    # Insert user data
    assistant1 = Assistant(first_name='Iza', last_name='Piechowiak')
    assistant2 = Assistant(first_name='Martyna', last_name='Olszewska')
    db.session.add(assistant1)
    db.session.add(assistant2)
 
    # Commit the changes for the users
    db.session.commit()
    print('Hello')

    assert db.session.query(Assistant).count() == 2
    print(db.session.query(Assistant))
    assert math_func.add(5) == 7
    db.drop_all()