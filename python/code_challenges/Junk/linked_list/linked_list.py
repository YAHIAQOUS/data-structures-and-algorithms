
class Node:
    def __init__(self,value=""):
        self.value=value
        self.next = None
    def __str__(self):
        return str(self.value)

class LinkedList():
    def __init__(self):
        self.head = None

    def __str__(self):
        current = self.head
        string = ""
        while current:
            string += str(current) + " -> "
            current = current.next
        string += "None"
        return string

    # CC07
    def kth(self,number):
        # current = self.head
        # counter = 0
        # value = 0

        # def recursion_method():
        #     nonlocal current
        #     nonlocal counter
        #     nonlocal value

        #     if current.next != None:
        #         # print('hi')
        #         current = current.next
        #         counter +=1
        #         if number == counter:
        #             # print('bye')
        #             value = current
        #             print(current)
        #         recursion_method()

        # verb = recursion_method()
        # print(value)
        # return value

        current = self.head
        list_length=1
        while current.next:
            list_length+=1
            current=current.next
        current=self.head
        # print(list_length)
        if number > list_length:
            return("Input is greater than the length of the linked list")
        elif number < 0:
            return("Input k is not a positive integer")
        target = list_length - number - 1
        print(target)
        for i in range(list_length):
            if i == target:
                print(current.value)
                return(current.value)
            else:
                current=current.next








if __name__ == "__main__":
    # CC05
    # first_instant = LinkedList('hello')
    # print (str(first_instant))
    # print(first_instant.next)

    # CC06
    # new = LinkedList()
    # new.append(3)
    # print(new)

    # CC07
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(6)
    node4 = Node(4)
    node5 = Node(9)
    node6 = Node(25)
    node7 = Node(14)
    node8 = Node(3)

    linked_list = LinkedList()
    linked_list.head = node1
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    node6.next = node7
    node7.next = node8

    print(linked_list)
    print(linked_list.kth(5))
