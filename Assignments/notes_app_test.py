import unittest

from notes_app import *

class NoteAppTestSuite(unittest.TestCase):

    def test_create_note_content(self):
        create_note = NotesApplication(["Note creation"])
        self.assertEqual(
            create_note.create(),
            ["Note creation"],
            msg='should create a new list')

    def test_list_note_content(self): 
    	list_notes =  NotesApplication()
    	self.assertEqual(
    		list_notes.list(),
    		)
    def test_edit(self):
        test = NotesApplication("life",["Life is good"])
        self.assertEqual(test.edit(0,"Life is good"),"Life is good ")
​
    def test_empty_add(self):
        test = NotesApplication("Blessing",[])
        self.assertEqual(test.create(""),"add your note")
​
    def test_noneValue_in_add(self):
        test = NotesApplication("",[])
        self.assertEqual(test.create(None),"add your note")
​
    def test_addedSuccessfully(self):
        test = NotesApplication("",[])
        self.assertEqual(test.create("Blessing Notes"),test.get(0)+" added")
​
    def test_getIndex(self):
        test = NotesApplication("life",["life is good"])
        test.create("life is good")
        test.create("life is good")
        self.assertEqual(test.get(2),"life is good")
​
    def test_getIndexFalseEntry(self):
        test = NotesApplication("kunle",["Is my name"])
        test.create("life is good")
        test.create("life is good")
        self.assertNotEqual(test.get(1),"yes, and game")
​
if __name__== "__main__":

    unittest.main()
