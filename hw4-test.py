import unittest

from hw4 import *

class tester(unittest.TestCase):
    
    # we are not providing a test case for list length
    # use the examples below to construct some!
    
    def test_add_head(self):
        """
        Test for adding an element to the head of the linked list.

        Test Coverage:
            - nullity
            - head elements equal
        """
        head = None
        for element in range(1, 10):
            head = add_head(head, element)
            self.assertIsNotNone(head)
            self.assertEqual(head.data, element)


    def test_add_tail(self):
        node_a = Node(1)
        node_b = Node(2)
        node_a.next_node = node_b
        
        node_a = add_tail(node_a, 3)
        self.assertEqual(node_a.next_node.next_node.data, 3)
        
    
    def test_remove_position(self):
        a = Node(2, Node(3, Node(4)))
        a = remove_position(a, 1)
        self.assertEqual(a.next_node.data, 4)


    def test_find_cycle(self):
        node_a = Node(1)
        node_b = Node(2)
        node_c = Node(3)
        
        node_a.next_node = node_b
        node_b.next_node = node_c
        
        # create cycle between node_b and node_b
        node_c.next_node = node_b

        self.assertTrue(find_cycle(node_a))


if __name__ == '__main__':
    unittest.main(module=__name__, buffer=True, exit=False)
