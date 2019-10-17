About me
---------
洪鈺婷 (Tiffany)
* 星座：天秤座
* 興趣：聽音樂、看書、看電影



Week 2
---------
Linked List
> 1.  Linked-list是由一連串的節點（Node）所構成，每個節點指向下一個節點，而最後一個節點則指向Null（在python裡面是None）。
> 2.  每個節點本身有兩種屬性（attribute）：本身帶有的值或者是資料&指向下一個節點的指標（pointer）。
> 3.  資料散落在記憶體中各處，加入或是刪除元素只需要改變pointer即可完成。



Week 3
--------
Stack & Queue




Week 4
---------
Insertion Sort 
> 將資料分成已排序、未排序兩部份，依序由未排序中的第一筆(正處理的值)，插入到已排序中的適當位置，插入時由右而左比較，直到遇到第一個比正處理的值小的值，再插入。比較時，若遇到的值比正處理的值大或相等，則將值往右移。

> 時間複雜度(Time Complexity)：
  * Best Case：Ο(1)
    當資料的順序恰好為由小到大時，每回合只需比較1次
  * Worst Case：Ο(n2)
    當資料的順序恰好為由大到小時，第i回合需比i次
  * Average Case：Ο(n2)
    第n筆資料，平均比較n/2次

Quick Sort
