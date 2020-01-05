

class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
        
class MyLinkedList(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head=None   
        self.size=0
        

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """

        
        if self.head == None:
            return -1
        if index<0 or index>=self.size:
            return -1
        
        cur = self.head        
        
        for i in range(index):
            cur=cur.next
            print(cur.val)
        return cur.val
        
        
        

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: None
        """
        
        
        new_node=Node(val)
        new_node.next=self.head  
        self.head=new_node
        
        self.size+=1
        

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: None
        """
        

        
        if self.head==None:
            self.head=Node(val)
            
        elif index==0:
            self.addAtHead(val)
            
        elif index < 0 or index >=self.size:
            return    
        
        else:  
            cur=self.head        
            while cur.next:
                cur=cur.next
                
            new_node=Node(val)    
            cur.next=new_node    
            
        self.size+=1
        
        

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: None
        """
    
        
        if index==self.size:
            self.addAtTail(val)
            return
        
        elif index < 0 or index >=self.size:
            return
        
        else:
            cur=self.head           
            new_node=Node(val)
            
            for i in range(index-1):
                cur=cur.next
                 
            new_node.next=cur.next   
            cur.next=new_node        
            
            self.size+=1
             
        
               

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: None
        """
     
        if self.head == None:
            return -1
        
        elif index<0 or index>=self.size:
            return -1
        
        elif index == 0:
            cur = self.head
            self.head = cur.next
            cur = None
            
        elif index == (self.size-1):
            cur=self.head
            for _ in range(index-1):
                cur=cur.next
            cur.next=None
            self.size-=1
        
        else:
            cur=self.head
            for i in range(index-1):
                cur=cur.next
                
            cur.next=cur.next.next   
            
            self.size-=1      
        
    



