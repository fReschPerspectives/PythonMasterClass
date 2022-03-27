import pytest

def test_answer():
    with open('./HelloWorld.py') as f:
        lines = f.readlines() # list containing lines of file

    assert len(lines) == 1

def test_contents():
    with open('./HelloWorld.py') as f:
        lines = f.readlines() # list containing lines of file   

    assert lines[0] == "print(\"Hello, Rob.\")" or "print('Hello, Rob.')"
