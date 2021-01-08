from typing import List

class Node:

    def __init__(self, key):
        self.data = key
        self.children = []

    def list_tree_breadth_first_queue(self) -> List:
        data_list = []
        queue = [self]

        while len(queue) > 0:
            data_list.append(queue[0].data)
            node = queue.pop(0)

            for child in node.children:
                queue.append(child)

        return data_list

    def list_tree_breadth_first_level(self) -> List:
        data_list = []
        for level in range(1, self.calc_height()+1):
            data_list += (self.list_given_level(level))
        return data_list

    def calc_height(self) -> int:
        children_heights = []
        if len(self.children) == 0:
            return 1
        for child in self.children:
            children_heights.append(child.calc_height())
        tallest_height = max(children_heights)

        return tallest_height + 1

    def list_given_level(self, level) -> List:
        if level == 1:
            return[self.data]
        if level == 2:
            child_list = []
            for child in self.children:
                child_list.append(child.data)
            return child_list
        if level > 2:
            child_list = []
            for child in self.children:
                child_list += child.list_given_level(level - 1)
            return child_list

import unittest

class TreeTests(unittest.TestCase):
    def setUp(self):         
        r'''
             a
            / \
           b   c
          /|\  |
         d e f g
           |   |
           h   i
               /\
              j  k

        '''
        
        
        self.root = Node('a')
        self.root.children = [Node('b'), Node('c')]
        self.root.children[0].children = [Node('d'), Node('e'), Node('f')]
        self.root.children[1].children = [Node('g')]
        self.root.children[0].children[1].children = [Node('h')]
        self.root.children[1].children[0].children = [Node('i')]
        self.root.children[1].children[0].children[0].children = [Node('j'), Node('k')]

    def test_list_tree_breadth_first(self):
        self.assertListEqual(self.root.list_tree_breadth_first_queue(), ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k'])
    
    def test_list_tree_breadth_first_level(self):
        self.assertListEqual(self.root.list_tree_breadth_first_level(), ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k'])

    def test_calc_height(self):
        self.assertEqual(self.root.calc_height(), 5)
        

    def test_print_given_level(self):
        self.assertEqual(self.root.list_given_level(1), ['a'])
        self.assertEqual(self.root.list_given_level(2), ['b', 'c'])
        self.assertEqual(self.root.list_given_level(3), ['d', 'e', 'f', 'g'])
        self.assertEqual(self.root.list_given_level(5), ['j', 'k'])

if __name__ == '__main__':
    unittest.main()