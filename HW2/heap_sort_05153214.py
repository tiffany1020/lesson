class Solution(object):
    def heap_sort(self,nums):
        """
        :type nums: List[int] ex:[3,2,-4,6,4,2,19],[5,1,1,2,0,0]
        :rtype: List[int] ex:[-4,2,2,3,4,6,19],[0,0,1,1,2,5]
        """        
        
        alist=nums
          

        def change(c1,c2):
            alist[c1],alist[c2]=alist[c2],alist[c1]
            return alist[c1],alist[c2]


        def heap(alist,i,L,R): 
            if L in index_sum and R in index_sum:
                if alist[L]>=alist[R] and alist[L]>=alist[i]:            
                    change(L,i)
                    #print(alist)
                    return            
                elif alist[R]>=alist[L] and alist[R]>=alist[i]:          
                    change(R,i)           
                    #print(alist)
                    return        
                else:
                    return

            elif L in index_sum:
                #print('只有左節點存在')
                if alist[L]>=alist[i]:
                    change(L,i)
                    #print(alist)   
                    return 
                else:
                    return

            elif R in index_sum:
                #print('只有右節點存在')
                if alist[R]>=alist[i]:
                    change(R,i)           
                    #print(alist)
                    return 
                else:
                    return

            return


        new_list=[]

        index_sum=[]
        for i in range (len(alist)-1,-1,-1):
            index_sum.append(i)
        #print(index_sum)


        new_list=[]
        while len(alist) !=0:
            index_count=int((len(alist)/2)-1) ## 4


            for i in range(index_count,-1,-1):
                L=2*i+1
                R=2*i+2    
                # print('一開始:',alist)
                #print(i,L,R) #印出來看看
                heap(alist,i,L,R)
                #print('變動後:',alist)
                #print('-----')

            alist[0],alist[len(alist)-1]=alist[len(alist)-1],alist[0]
            #print('交換後:',alist)



            new_list.insert(0,alist[len(alist)-1])

            del alist[len(alist)-1]
            del index_sum[0]

            #print('alist長度:',len(alist))
            #print('*****',index_sum,new_list,alist)


        print(new_list)


output=Solution().heap_sort([3,2,-4,6,4,2,19])
output
