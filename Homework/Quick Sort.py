def  quicksort(list,begin,last):  
    if begin < last:                              # 如果開始的位置大於結束，則停止
        pivot = partition(list,begin,last)        # 進行第一次劃分 分成左右兩個序列
        quicksort(list,begin,pivot-1)             # 繼續將左邊序列進行排序 
        quicksort(list,pivot+1,last)              # 繼續將右邊序列進行排序

        
## 從L開始一個一個值向右檢視、從R開始一個一個值向左檢視

def partition(list,begin,last):
    pivot=list[begin]                          # 設定第一個值為基準點
    L=begin+1                                  # 因此從第二個值開始進行比較
    R=last
    while L<=R:                                # 當兩個值相遇或L超過R時則停止
        while L<=R and list[L] <= pivot:
            L+=1                               # 當值大於基準點，則將L(相當於index值)+1，使他往右檢視下一個
                                               # 若while條件沒有加上 L<=R 可能會使index值超出範圍
            
        while L<=R and list[R] >= pivot:
            R-=1                               # 當值大於基準點，則將R(相當於index值)-1，使他往左檢視下一個
                                               # 若while條件沒有加上 L<=R 可能會使index值超出範圍
        
        if L>R:                                # 當L超過R時則停止
            break
                
        else: 
            list[L],list[R]=list[R],list[L]    # 如果不能再向前移動，則將兩者交換，再進行while循環
                                   
            
    list[begin],list[R]=list[R],list[begin]  
    return R


## 測試數值
list=[21,4,8,15,30,6,18,1,15,27]

quicksort(list,0,len(list)-1)     # 0 和 len(list)-1 為傳遞list的index值
print(list)
