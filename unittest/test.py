import unittest
from linked_list import LinkedList
class TestCase(unittest.TestCase):
    def test_add_first(self):
        l = LinkedList()
        l.add_first(1)
        l.add_first(2)
        self.assertEquals(2, len(l))
        self.assertEquals("[2,1]", str(l))
    def test_add_last(self):
        l = LinkedList()
        l.add_last(1)
        l.add_last(2)
        self.assertEquals(2, len(l))
        self.assertEquals("[1,2]", str(l))
    def test_remove_first(self):
        l = LinkedList()
        l.add_first(1)
        l.add_first(2)
        self.assertEquals(2, l.remove_first())
        self.assertEquals(1, len(l))
        self.assertEquals('[1]', str(l))
    def test_remove_last(self):
        l = LinkedList()
        l.add_first(1)
        l.add_first(2)
        self.assertEquals(1, l.remove_last())
        self.assertEquals(1, len(l))
        self.assertEquals('[2]', str(l))
    def test_iter(self):
        l = LinkedList()
        l.add_first(1)
        l.add_first(2)
        self.assertEquals([2,1], [x for x in l])
    def test_empty(self):
        l = LinkedList()
        self.assertEquals(True, l.empty())
        l.add_first(1)
        self.assertEquals(False, l.empty())
        l.remove_first()
        self.assertEquals(True, l.empty())
if __name__ == '__main__':
    unittest.main()