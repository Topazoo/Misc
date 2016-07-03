"""Stack Class: Quickly reversable for use as Queue"""
class Stack_test(object):
    def __init__(self, rnge): #Takes an integer for an inclusive range
        self.stack = [x for x in range(0, rnge + 1)] #List comprehension
        self.count = len(self.stack)

    def print_self(self): 
        x = len(self.stack) - 1 #Should be class repr
        if len(self.stack) == 0:
            print("The stack is empty!")

        while x >= 0:
            print(self.stack[x])
            x -= 1

    def make_queue(self):
        self.stack = self.stack[::-1] #Makes Queue

    def clear(self):
        self.stack = [] #Clears Stack
        self.count = 0

    def add_element(self, element): #Adds a single element
        self.stack.append(element)
        self.count += 1

    def add_elements(self, elements): #Adds a list of elements
        for element in elements:
            self.stack.append(element)
            self.count += 1

    def pop(self):
        get = self.stack[self.count - 1]
        del(self.stack[self.count - 1]) #Pops the top of the stack
        self.count -= 1
        return get

"""new_stack = Stack_test(100)
new_stack.print_self()

new_stack.make_queue()
new_stack.print_self()


new_stack.clear()"""

"""new_stack = Stack_test(0)
new_stack.clear()
new_stack.add_element(10)
new_stack.add_element(20)      #These are tests for the stack class
new_stack.add_element(30)
new_stack.pop()
new_stack.print_self()"""

"""new_stack.clear()
new_stack.add_elements([x for x in range(0, 11)])
new_stack.print_self()"""

"""Queue class that can become a Stack"""
class Queue_test(object):
    def __init__(self, rnge): #Takes an integer for an inclusive range
        self.queue = [x for x in range(0, rnge + 1)] #list comprehension
        self.count = len(self.queue)

    def print_self(self): #Should be class repr

        if len(self.queue) == 0:
            print("The queue is empty!")
            return
        
        x = 0
        
        while x < len(self.queue):
            print(self.queue[x])
            x += 1

    def make_stack(self):
        self.queue = self.queue[::-1] #Makes Stack

    def clear(self):
        self.queue = [] #Clears Queue

    def add_element(self, element): #Adds a single element
        self.queue.append(element)
        self.count += 1

    def add_elements(self, elements): #Adds a list of elements
        for element in elements:
            self.queue.append(element)
            self.count += 1

    def dequeue(self): #dequeue element
        get = self.queue[0]
        del(self.queue[0])
        self.count -= 1
        return get
        
        


"""new_queue = Queue_test(10)
new_queue.print_self()
new_queue.dequeue()
new_queue.print_self()

#new_queue.make_stack()
new_queue.add_element(15)
new_queue.print_self()


new_queue.clear()
new_queue.print_self()"""

"""new_queue.add_element(10)
new_queue.add_element(20)      #These are tests for the queue class
new_queue.add_element(30)

new_queue.print_self()

new_queue.clear()
new_queue.add_elements([x for x in range(0, 11)])
new_queue.print_self()"""

class SortedList(object): #A list with an interchangeable insertion sort

    def __init__(self):
        self.direction = '<'
        self.list = []
        self.count = 0
    
    def clear(self): #Clear the list
        self.list = []
        self.count = 0

    def append(self, element): #Add a single element to the list
        pos = 0

        if self.count == 0: #Always insert the first element at the front
            self.list.append(element)
            self.count += 1

        else:

            if self.direction == '<': #If increasing order sort
                while (pos < self.count) and (self.list[pos] < element) :
                    pos += 1
                
                if pos == len(self.list): #if element should go at the end
                    self.list.append(element) 
                    self.count += 1

                else: #else insert it in it's correct position
                    self.list.insert(pos, element)
                    self.count += 1

            else: #if decreasing order sort
                while (pos < self.count) and (self.list[pos] > element) :
                    pos += 1
                
                if pos == len(self.list): #if element should go at the end
                    self.list.append(element)
                    self.count += 1

                else: #else insert it in it's correct position
                    self.list.insert(pos, element)
                    self.count += 1

    def append_multiple(self, elements): #sort elements in a preexisting list
        for element in elements:
            self.append(element)

    def swap_direction(self): #Change the direction of the sort and clear the list
        print("Clearing list and changing sort")
        self.clear()
        
        if self.direction == '<':
            self.direction = '>'
        else:
            self.direction = '<'

    def print_list(self): #print the list, should be repr
        if len(self.list) == 0:
            print("The list is empty!")
        else:
            print(self.list)
    

"""ll = SortedList()

ll.append(1)
ll.append(2)
ll.append(3)
ll.append(5)
ll.append(4)
ll.append(8)
ll.append(6)
ll.append(7)
ll.print_list()

ll.swap_direction()

ll.append(1)
ll.append(2)
ll.append(3)
ll.append(5)    #Test calls to sorted list functions
ll.append(4)
ll.append(8)
ll.append(6)
ll.append(7)
ll.print_list()

ll.swap_direction()

list2 = [10, 39, 1, 2000, 450, 999, 11, 10, 121, 1000]

ll.append_multiple(list2)
ll.print_list()

ll.swap_direction()

ll.append_multiple(list2)
ll.print_list()"""


"""Using Stacks to add integers of potentially unlimited length"""

class Stack2(object):
    
    def __init__(self):
        self.stack = []
        self.count = 0

    def add_element(self, element): #Adds a single element
        self.stack.append(element)
        self.count += 1

    def pop(self): #Pop element
        get = self.stack[self.count - 1]
        del(self.stack[self.count - 1])
        self.count -= 1
        return get
        

def build_stack(stack, number): #Populate the stack(s) 
    for digit in number:
        stack.add_element((int(digit)))
        
    return stack

def add_stacks(stack1, stack2): #Adds stacks of digits
    final = []
    carry_over = 0

    if stack1.count == stack2.count: #If both numbers are the same size
        
        while stack1.count > 0:
            add = str((stack1.pop() + stack2.pop() + carry_over)) #add numbers and 
            carry_over = 0                                        #and possible extra
                                                                  #digit
            if int(add) >= 10: #if result >= 10, add exra digit                               
                carry_over = 1
                add = str(int(add) % 10) 
                
            final.insert(0, add) #insert into final representation

        if carry_over == 1: #catch final carryover
            final.insert(0, '1')
                        
    elif stack1.count > stack2.count: #If the first number is longer
        
        while stack2.count > 0: #while digits in 2nd number
            add = str((stack1.pop() + stack2.pop() + carry_over)) #add numbers and 
            carry_over = 0                                        #carry over

            if int(add) >= 10:                                    #check for 
                carry_over = 1                                    #carry over
                add = str(int(add) % 10)
                
            final.insert(0, add) #insert into final representation

        while stack1.count > 0: #Add the rest of the digits from the 1st number
            if carry_over == 1:
                add = str((stack1.pop() + carry_over)) #catch carryover
                
                if int(add) >= 10: #catch until no carryover
                    carry_over = 1
                    add = str(int(add) % 10)

                else:
                    carry_over = 0
            else:
                add = str(stack1.pop())

            final.insert(0, add) #insert into final representation
                
        if carry_over == 1:
            final.insert(0, '1') #catch potential final carryover

    else: #If the second number is longer
        
        while stack1.count > 0:
            add = str((stack1.pop() + stack2.pop() + carry_over))  #add numbers and 
            carry_over = 0                                         #carry over

            if int(add) >= 10:                                    #check for 
                carry_over = 1                                    #carry over
                add = str(int(add) % 10)
                
            final.insert(0, add) #insert into final representation

        while stack2.count > 0: #Add the rest of the digits from the 2nd number
            if carry_over == 1:
                add = str((stack2.pop() + carry_over)) #catch carryover
                
                if int(add) >= 10: #catch until no carryover
                    carry_over = 1
                    add = str(int(add) % 10)

                else:
                    carry_over = 0
            else:
                add = str(stack2.pop())

            final.insert(0, add) #insert into final representation
                
        if carry_over == 1:
            final.insert(0, '1') #catch potential final carryover

    return final
                        
def add_ints(): #add two integers of potentially unlimited length

    num1 = Stack2() #create two stacks
    num2 = Stack2()

    entered_number1 = str(input("Enter a number: ")) #get numbers
    entered_number2 = str(input("Enter a second number: "))

    build_stack(num1, entered_number1) #populate stacs
    build_stack(num2, entered_number2)

    print("".join(add_stacks(num1, num2))) #Print result
    

add_ints() #call add_ints()"""


"""Derived stack class with extra feature"""
class Stack3(object):
    stack = []
    count = 0
    
    def __init__(self):
        pass

    def add_element(self, element): #Adds a single element
        self.stack.append(element)
        self.count += 1

    def pop(self): #Pop element
        get = self.stack[self.count - 1]
        del(self.stack[self.count - 1])
        self.count -= 1
        return get
        


class Stack4(Stack3):
    def __init__(self):
        self.greater_than_10_count = 0

    def add_element(self, element): #Adds a single element
        self.stack.append(element)

        if element > 10:
            self.greater_than_10_count += 1 #Track if it's more than 10
            
        self.count += 1

    def pop(self): #Pop element
        get = self.stack[self.count - 1]

        if get > 10:
            self.greater_than_10_count -= 1 #Track if it's more than 10
        del(self.stack[self.count - 1])
        self.count -= 1
        return get

"""Test calls for Stack4"""
"""stack4 = Stack4()
stack4.add_element(11)
stack4.add_element(5)
stack4.add_element(10)
stack4.add_element(12)
print(stack4.stack)
print(stack4.greater_than_10_count)
stack4.pop()
print(stack4.stack)
print(stack4.greater_than_10_count)"""
        

        

