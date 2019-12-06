from Crypto.Hash import MD5
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyHashSet:
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.data = [None] * capacity
        
    def change(self,word):
        h=MD5.new()
        h.update(word.encode("utf-8"))
        #print (h.hexdigest()) ##16進位
        x=h.hexdigest()
        x1=int(h.hexdigest(),16) ##16轉10進位
        #print(x)
        return (x,x1%self.capacity)


    def add(self, key):
        t,index=MyHashSet().change(key)
        #print(t,index)
                         
        new_node=ListNode(t)

        if self.data[index]==None:      
            self.data[index]=new_node
            #print(self.data)
            #return self.data

        else:
            current=self.data[index]     
            while current.next:
                current=current.next
            current.next = new_node
            #print(self.data)
            #return self.data    
        
        
    
    def contains(self, key):
        t,index=MyHashSet().change(key)
        #print(t,index)     
        
        current=self.data[index]
        
        if current==None:
            return False
        
        else:   

            while current.next and t != current.val:
                current=current.next
            if t != current.val:
                return False
            else:
                return True
            
            
    def remove(self, key):
        t,index=MyHashSet().change(key)
        #print(t,index)
        
        while self.contains(key)==True:
            self.remove2(t,index)
            
                
    def remove2(self,t,index):  
        
        current=self.data[index]
        
        if t==current.val:
            self.data[index]=current.next
            return
        
        else:
            while current.next and t != current.next.val:
                current=current.next
                
            if current.next and current.next.next and t == current.next.val:
                current.next=current.next.next
                return 
            elif current.next and current.next.next==None and t == current.next.val:
                current.next=None
                return
   
