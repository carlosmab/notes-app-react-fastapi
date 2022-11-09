import pytest
from model import Note

class TestNotes():
    def setup_class(self):
        self.note = Note("This is a note for testing", test=True)
        self.collection = self.note.collection
    
    def teardown_method(self):
        self.collection.delete_many({})
            
    def test_if_note_can_be_created(self):
        self.note.create()
        assert self.collection.count_documents({}) == 1
        
    def test_if_note_can_be_updated(self):
        self.note.create()
        self.note.update("Note updated")
        updated_note = self.collection.find_one({"_id": self.note._id})
        assert updated_note["note"] == "Note updated"
    
    def test_if_note_can_be_removed(self):
        self.note.create()
        self.note.remove()
        assert self.collection.count_documents({}) == 0
        