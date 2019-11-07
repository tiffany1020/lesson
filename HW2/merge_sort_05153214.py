class Solution(object):
    def merge_sort(self,nums): 
        """
        :type nums: List[int] ex:[3,2,-4,6,4,2,19],[5,1,1,2,0,0]
        :rtype: List[int] ex:[-4,2,2,3,4,6,19],[0,0,1,1,2,5]
        """
        list=nums
        
        def mergesort(list): 
            num = len(list)
            if num<2:
                return list
            else:       
                center=int(len(list)/2)
                #print(center)
                left = mergesort(list[0:center])
                right = mergesort(list[center:len(list)]) 
            return merge(left,right)

        def merge(left,right):      
            p = 0
            q = 0
            a1 = []    
            while p < len(left)  and q < len(right):
                if left[p] < right[q]:          
                    a1.append(left[p])
                    p += 1              
                else:   
                    a1.append(right[q])
                    q += 1         
            a1 += left[p:]
            a1 += right[q:]

            return a1
        
        print(mergesort(list))
        
output=Solution().merge_sort([3,2,-4,6,4,2,19])
output
