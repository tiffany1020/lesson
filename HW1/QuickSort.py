def quicksort(list):
    quicksortHelper(list,0,len(list)-1)     # 0 和 len(list)-1 為傳遞list的index值


def  quicksortHelper(list,begin,last):  
    if begin < last:                                    # 如果開始的位置大於結束，則停止
        pivot = partition(list,begin,last)              # 進行第一次劃分 分成左右兩個序列
        quicksortHelper(list,begin,pivot-1)             # 繼續將左邊序列進行排序 
        quicksortHelper(list,pivot+1,last)              # 繼續將右邊序列進行排序


def partition(list,begin,last):
    pivot=list[begin]                                                  # 設定第一個值為基準點
    L=begin+1                                                          # 因此從第二個值開始進行比較
    R=last
    while L<=R:                                                        # 當L超過R時則停止
        while L<=R and list[L] <= pivot:
            print('L:',L,'R:',R,'list[L]:',list[L],'list[R]:',list[R]) # 檢視當前各值
            L+=1                                                       # 當值大於基準點，則將L(相當於index值)+1，使他往右檢視下一個
                                                                       # 若while條件沒有加上 L<=R 可能會使index值超出範圍
            print('----------')
        while L<=R and list[R] >= pivot:
            print('L:',L,'R:',R,'list[L]:',list[L],'list[R]:',list[R]) # 檢視當前各值
            R-=1                                                       # 當值大於基準點，則將R(相當於index值)-1，使他往左檢視下一個
                                                                       # 若while條件沒有加上 L<=R 可能會使index值超出範圍
            print('----------')
        if L>R:                                                        # 當L超過R時則停止
            break
                
        else: 
            list[L],list[R]=list[R],list[L]                            # 如果不能再向前移動，則將兩者的值交換，再進行while循環
            print('L:',L,'R:',R,'list[L]:',list[L],'list[R]:',list[R]) # 檢視當前各值
            
    list[begin],list[R]=list[R],list[begin]                            # 將pivot值與停止時的R的數值做交換，使pivot
    return R                                                           # 回傳R值



## 測試數值

list=[21,4,8,15,30,6,18,1,15,27]
quicksort(list)     
print(list)
