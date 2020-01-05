
class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
        
class MinStack:
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
        self.size+=1
        
    def pop(self):
        if self.head == None:
            return
        else:
            num=self.getSize()
            cur=self.head            
            for i in range(num-2):
                cur=cur.next
            cur.next=None
        self.size-=1
        
        
    def getSize(self):
        cur=self.head
        count=0
        while cur:
            count+=1
            cur=cur.next
        return count
    
    def top(self):
        if self.head == None:
            return
        else:
            num=self.getSize()
            cur=self.head            
            for i in range(num-2):
                cur=cur.next
            temp=cur.next.val
            return temp
        
        
    def getMin(self):   
        
        if self.head == None:
            return
        
        else:            
            index=self.size
            cur=self.head
            temp=cur.val
            for i in range(index-1):
                if temp < cur.next.val:
                    temp=temp
                else:
                    temp=cur.next.val
                cur=cur.next
        return temp
    
        
    def IsEmpty(self):
        if self.head==None:
            return True
        else:
            return False
          
            


