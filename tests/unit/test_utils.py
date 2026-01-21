from app.utils import doThing, GLOBAL

def setup():
    GLOBAL["users"].clear()

def test_doThing_create_user():
    result = doThing("user", 1,2,3,4,5,6,7,8,9)
    assert result is True
    assert len(GLOBAL["users"]) == 1

def test_doThing_update_user():
    doThing("user", 1,2,3,4,5,6,7,8,9)
    doThing("user", 9,8,7,6,5,4,3,2,1)
    assert len(GLOBAL["users"]) == 1
