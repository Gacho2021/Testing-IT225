import unittest
from lock import lock
from scan import Scan
from item import Item
from inventory import inventory
class LockTest(unittest.TestCase):
    def setUp(self):
        self.lock=Lock('3176','BE', 'normal')

    def test_lockstring(self):
        self.assertEqual(str(self.lock), '3176 locked')

    def test_getStatus(self):
        self.assertEqual(self.lock.getStatus(), 'locked')

    def test_setStatus(self):
        self.lock.setStatus('unlocked')
        self.assertEqual(self.lock.getStatus(), 'unlocked')
    
    def test_GetDoor(self):
        self.assertEqual(self.lock.getDoor(), '3176')

class ScanTest(unittest.TestCase):
    def setUp(self):
        self.scan=Scan('3176', 'BE', 'normal', 315643)

    def test_GetCard(self):
        self.assertEqual(self.scan.getCard(), 315643)

class ItemTest(unittest.TestCase):
     def test_Getitem(self):
         self.assertEqual(self.item.getItem(), itemname)

     def test_GetItemPrice(self):
         self.assertEqual(self.item.getItemPrice, itemprice)

class inventoryTest(unittest.TestCase):
     def test_GetItemByNumber(self):
         self.assertEquals(self.item.getItemByNumber, number)


