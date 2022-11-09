import pytest
from model import Note

def test_if_note_can_be_created():
    note = Note("first note")
    assert note.create