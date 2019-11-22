Insert 新增 
---------------------------
(新增節點，仍必須維持Binary Search Tree的架構。)
1. 每一個加進去的值，都要與root(parent)進行比較，比root小放左邊，比root大放右邊。
2. 若是遇到一樣的數值，擺在左邊。
* 程式寫法:
1. 先確認root.val是否空值
2. 將要插入的值(val)建立一個new_node
3. 開始進行val和root.val的比較
4. 當val <= root.val 時，接著確認他的左節點是否為空值，如果是空值，則直接存new_node，如果不是空值，則再次進行insert(root.left,val)
5. 當val > root.val 時，接著確認他的右節點是否為空值，如果是空值，則直接存new_node，如果不是空值，則再次進行insert(root.right,val)  


Delete 刪除  
---------------------------
(刪除節點後，仍必須維持Binary Search Tree的架構。)
會有以下三種狀況:
1. 無child → 直接砍掉點。
2. 有一個child → 將有child的那邊，直接連接到已刪除節點的父節點。
3. 有兩個child →
    * 在右邊的子樹中找到一個最小值。
    * 用找到的最小值替換要刪除的節點的值。現在，右子樹包含重複項。
    * 用delete function將右側子樹刪除重複項。
* 程式寫法:
1. 先找到target位在哪個節點，當target=root.val時，開始進行有無小孩的判斷
2. 沒有小孩時，直接砍掉
3. 有一個小孩時，則將root指向有小孩的那邊，接著進行檢查，查看是否還有目標值
4. 有兩個小孩時，寫一個 min function 取得右子樹最小值替換，再刪除重複值，接著進行檢查，查看是否還有目標值

Search 查詢 
---------------------------
(查詢特定節點)
* 根據BST特徵：root.left.val < root.val < root.right.val
將欲查詢的數值從root開始向下比較，比root小往左走，比root大往右走，依序再對每一個node逐一比較，比node小往左走，比node大往右走。
* 結果：
1. 找到欲查詢的數值 → return結果
2. 沒有找到 → 回傳False (BST內沒有此數值)


Modify 修改
---------------------------
(將新的數值修改至指定的節點後，仍必須維持Binary Search Tree的架構。)
1. 先刪除目標節點
2. 再加入新的數值
* 程式寫法:
1. 另外寫一個delete_2 一次只能刪除一個
2. 運用insert插入new_val
3. 寫一個 find_2 檢查是否還有target，如果有，則繼續進行modify


參考資料
---------------------------
1. http://alrightchiu.github.io/SecondRound/binary-search-tree-introjian-jie.html
2.	http://alrightchiu.github.io/SecondRound/binary-search-tree-searchsou-xun-zi-liao-insertxin-zeng-zi-liao.html
3.	http://alrightchiu.github.io/SecondRound/binary-search-tree-sortpai-xu-deleteshan-chu-zi-liao.html
4.	http://www.algolist.net/Data_structures/Binary_search_tree/Removal
