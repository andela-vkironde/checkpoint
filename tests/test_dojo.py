import unittest
from models.dojo import Dojo
from models.room import Room

class TestDojo(unittest.TestCase):

    def setUp(self):
        self.dojo = Dojo()

    def test_create_room(self):
        room = Room('Blue', 'Office')
        initial_dojo_rooms = len(self.dojo.rooms)
        self.dojo.create_room(room)
        new_dojo_rooms =  len(self.dojo.rooms)
        self.assertEqual((new_dojo_rooms - initial_dojo_rooms), 1)
        self.assertEqual(self.dojo.rooms[0].name, "Blue")

    def test_office_room_uniqueness():
        room = Room('unique room')
