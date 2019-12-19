from collections import defaultdict 

class Graph: 
    def __init__(self): 
        self.graph = defaultdict(list) 

    def addEdge(self,u,v): 
        self.graph[u].append(v) 
        #print(u,v)
        return 
    
    
    def count(self):
        i=0
        for i in self.graph:
            i+=1
        return i
    
    def BFS(self, s): 
        list1=[]
        queue=[]
        
        queue.append(s)
        
        while len(queue) != self.count():            
            for i in self.graph[s]:
                if i not in list1 and i not in queue:
                    list1.append(i)

            s=list1.pop(0)   
            if s not in queue:
                queue.append(s)    
        return queue
    
        
    def DFS(self, s):
        list2=[]
        stack=[]
        
        stack.append(s)
        
        while len(stack) != self.count() :
            for i in self.graph[s]:
                if i not in list2 and i not in stack:
                    list2.append(i)
          
            s=list2.pop(-1)
            if s not in stack:
                stack.append(s)
        return stack               
                        

              
