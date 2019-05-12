import unittest
import kund
import kassa

class TestKund(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.kun = kund.Kund()
        
    def test_varTest(self):
        print(self.kun.varDetAllt())
        self.assertTrue((0 < self.kun.varDetAllt()) and (self.kun.varDetAllt() < 10))

    @classmethod
    def tearDown(cls):
        del cls.kun
    
    def test_tickTest(self):
        ticket = self.kun.tick()
        print(ticket)
        self.assertTrue((0 <= ticket) and (10 > ticket))

class TestKassa(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.kas = kassa.Kassa(0)
        cls.kas.openKassa()

    def test_whoami(self):
        self.assertEqual(self.kas.whoami(), 0)

if __name__ == '__main__':
    unittest.main()
