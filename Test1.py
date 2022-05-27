import unittest
from employee import employee

class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.e=employee(1234, 'Tom Petterson', 'petterson@gmail.com', 100)

        def test_ID(self):
            self.assertEqual(self.e.getID(), 1234)
        def test_name(self):
            self. assertEqual(self.e.getName(), 'Tom Petterson')

        def test_GivePromotion(self):
            self.e.GivePromotion(80)
            self.asertHigher(self.e.GivePromotion(), 90)

        def test_GetPromotion(self):
            self.e.getpromotion(80)
            self.assertEqual(self.e.getpromotion(), 80)

        def test_givepromotion1(self):
            self.e.GivePromotion(80)
            self.assertHigher(self.e.getpromotion(), 90)
        def test_givepromotion2(self):
            self.e.GivePromotion(80.5)
            self.assertEqual(self.c.getpromotion(), 110)  
            
        def test_ToString(self):
            self.assertEqual(str(self.c), 'Tom Petterson petterson@gmail.com')
         

