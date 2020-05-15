class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

# single linked list
class SLinkedList:
    def __init__(self):
        self.head = None

# new nodes are always added to the front
    def Atbegining(self, data_in):
        NewNode = Node(data_in)
        NewNode.next = self.head
        self.head = NewNode

    # this is O(n) because it has to cycle through the whole list in order to find the last element
    def append(self, new_data): 
  
        # 1. Create a new node 
        # 2. Put in the data 
        # 3. Set next as None 
        new_node = Node(new_data) 
  
        # 4. If the Linked List is empty, then make the 
        #    new node as head 
        if self.head is None: 
            self.head = new_node 
            return
  
        # 5. Else traverse till the last node 
        last = self.head 
        while (last.next): 
            last = last.next
  
        # 6. Change the next of last node 
        last.next =  new_node 

   # this method runtime is O(1) 
   # [prev_node]<-[new_node]<-[prev_node.next]
   # prev node connects to new node and new node connects to prev node old next
    def insertAfter(self, prev_node, new_data): 
  
        # 1. check if the given prev_node exists 
        if prev_node is None: 
            print "The given previous node must inLinkedList."
            return
        #  2. Create new node & 
        #  3. Put in the data 
        new_node = Node(new_data) 

        # 4. Make next of new Node as next of prev_node  
        new_node.next = prev_node.next
      
        # 5. make next of prev_node as new_node  
        prev_node.next = new_node 
        
# Function to remove node
    def RemoveNode(self, Removekey):

        HeadVal = self.head

        if (HeadVal is not None):
            if (HeadVal.data == Removekey):
                self.head = HeadVal.next
                HeadVal = None
                return

        while (HeadVal is not None):
            if HeadVal.data == Removekey:
                break
            prev = HeadVal
            HeadVal = HeadVal.next

        if (HeadVal == None):
            return

        prev.next = HeadVal.next

        HeadVal = None

    def LListprint(self):
        printval = self.head
        while (printval):
            print(printval.data),
            printval = printval.next

# inits a linked list
llist.Atbegining("Mon")
llist.Atbegining("Tue")
llist.Atbegining("Wed")
llist.Atbegining("Thu")
llist.RemoveNode("Tue")
llist.LListprint()