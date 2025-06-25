class Node:

    def __init__(self, data):
        self.data= data
        self.next= None

class LinkedList:

    def __init__(self,head):
        self.head= head

    # the following method reverses the linked list using the .reverse() function
    def reverse(self):
        values=[]
        current= self.head # start from the head node and call it current
        while current: # as long as current is not None
            values.append(current.data) # append the data of current to the values list
            current= current.next # move to the next node in the list
        values.reverse() # use the reverse () function to reverse the list

        # the following steps rebuild the newly reversed linked list
        if values: # as long as the list values is not empty
            self.head=Node(values[0]) # create a Node object and assign the first element in the newly reversed list to self.head
            current= self.head #start from the head node and call it current
            for i in range(1, len(values)): # loop through the values list starting from the second index
                current.next= Node(values[i]) # create a Node object with one segment of the data in the values list and store it in the next node
                current= current.next # move to the next node in the list
    

    # the following method reverses the linked list manually
    def manual_reverse(self):
        original=[] # create a new list to store the orgial order of the list
        current= self.head # start from the first node and store it in current
        while current: # as long as current is not empty
            original.append(current.data) # append the data of current to the original list
            current= current.next # move to the next node in the list
        
        reversed=[] #create a new list called reversed
        for i in range(len(original)-1,-1,-1): #loop through the orginal list from the last element and go all the way to the first
            reversed.append(original[i]) # append the value of a segment of data in the orginal list to the reversed list
            
        # the following steps rebuild the newly reversed linked list
        if reversed: # as long as the list reversed is not empty
            self.head=Node(reversed[0]) # create a Node object and assign the first element in the newly reversed list to self.head
            current= self.head #start from the head node and call it current
            for i in range(1, len(reversed)): # loop through the reversed list starting from the second index
                current.next= Node(reversed[i]) # create a Node object with one segment of the data in the reversed list and store it in the next node
                current= current.next # move to the next node in the list
    
    # This method prints out the results
    def print(self):
        current= self.head # start from the head node and call it current
        while current: # as long as current is not empty
            print(current.data, end=", ") # print out the data in current and add a comma after each current
            current= current.next # update the current"current" to the next node
        print("None") # indicate that after the end of the list, there's None



n1= Node(1)
n2= Node(2)
n3= Node(3)
n4= Node(4)
n5= Node(5)

n1.next=n2
n2.next=n3
n3.next=n4
n4.next=n5

linked_list=LinkedList(n1)
print("This is the orginal list: ")
linked_list.print()

linked_list.reverse()
print("This is after reversing the list using the .reverse() function: ")
linked_list.print()

# because the list got reversed using the .reverse () function previously, the .manual_reverse() function will reverse the reversed list, making it look like the orginal one
linked_list.manual_reverse()
print("This is after reversing the list manually: ")
linked_list.print()

