from collections import defaultdict 

class Graph(): 

    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [] 
        self.graph_matrix = [[0 for column in range(vertices)]  
                    for row in range(vertices)] 
          
    def Dijkstra(self, s): 
        
        min=99999999999
        
        distance = [min] * self.V 
        distance[s] = 0
        use = [0] * self.V 

        for c in range(self.V): 
  
            min = 999999999999
  
            for i in range(self.V): 
                if distance[i] < min and use[i] == 0: 
                    min = distance[i] 
                    point = i 
            
            use[point] = 1
            
  
            for t in range(self.V): 
                if self.graph[point][t] > 0 and  use[t] == 0 and distance[t] > distance[point] + self.graph[point][t]: 
                    distance[t] = distance[point] + self.graph[point][t] 
  

        #print(distance)
        d1={}
        for num in range(self.V):
            key='%s'%(num)
            d1[key]=distance[num]
        return d1



    def addEdge(self,u,v,w): 
        self.graph.append([u,v,w]) 
          
    
    def check(self, num, i): 
        if num[i] == i: 
            return i 
        return self.check(num, num[i]) 
         
        
    def Kruskal(self):   
         
        self.graph =  sorted(self.graph,key=lambda item: item[2]) 
  
        num = [] 
        p = []   
        
        for node in range(self.V): 
            num.append(node) 
            p.append(-1) 
      
        ans =[] 
        i = 0  
        e = 0 
        while e < self.V -1 :           
            u,v,w =  self.graph[i] 
            i = i + 1
            x = self.check(num, u) 
            y = self.check(num, v) 
             
            if x != y: 
                e = e + 1     
                ans.append([u,v,w]) 
                
                xroot = self.check(num, x) 
                yroot = self.check(num, y) 

                if p[xroot] < p[yroot]: 
                    num[xroot] = yroot 
                elif p[xroot] > p[yroot]: 
                    num[yroot] = xroot 

                else : 
                    num[yroot] = xroot 
                    p[xroot] += 1
      
        #print(ans)
        
        
        d2={}
               
        for u,v,weight in ans:  
            key='%s-%s'%(u,v)
            d2[key]=weight
            
        #print(d2)
        return d2

