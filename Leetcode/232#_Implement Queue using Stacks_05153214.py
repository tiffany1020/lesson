
class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
class MyQueue:
    def __init__(self):
        self.head=None
        self.size=0
        
    def push(self,val):
        if self.head == None:
            self.head=Node(val)
        else:
            cur=self.head
            while cur.next:
                cur=cur.next
            cur.next=Node(val)
 
            
    def pop(self):
        if self.head == None:
            return 
        else:
            temp=self.head.val
            self.head=self.head.next
            return temp
        
    def peek(self):
        return self.head.val
    
    def empty(self):
        if self.head==None:
            return True
        else:
            return False
          
    def getSize(self):
        cur=self.head
        count=0
        while cur:
            count+=1
            cur=cur.next
        return count
        
        
    def printqueue(self):            
        temp=self.head 
        while temp: 
            print(temp.val,end="->") 
            temp=temp.next
               
        
            
