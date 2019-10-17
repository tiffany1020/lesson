About me
---------
**洪鈺婷 (Tiffany)**
* 主修：企業管理 & 巨量資料
* 星座：天秤座
* 興趣：聽音樂、看書、看電影



Week 2
---------
**Linked List**
> 1.  Linked-list是由一連串的節點（Node）所構成，每個節點指向下一個節點，而最後一個節點則指向Null（在python裡面是None）。
> 2.  每個節點本身有兩種屬性（attribute）：本身帶有的值或者是資料&指向下一個節點的指標（pointer）。
> 3.  資料散落在記憶體中各處，加入或是刪除元素只需要改變pointer即可完成。



Week 3
--------
**Stack & Queue**




Week 4
---------
**HW1**
* [Quick Sort 程式碼](https://nbviewer.jupyter.org/github/tiffany1020/lesson/blob/master/Homework/Quick%20%20Sort.ipynb)
* [Quick Sort 流程圖](https://github.com/tiffany1020/lesson/blob/master/Homework/Quick%20Sort%20Flowchart.jpg)
* [Quick Sort 測值排序流程圖](https://github.com/tiffany1020/lesson/blob/master/Homework/%E6%B8%AC%E5%80%BC%E6%8E%92%E5%BA%8F%E6%B5%81%E7%A8%8B.jpg)

**Insertion Sort**
> 將資料分成已排序、未排序兩部份，依序由未排序中的第一筆(正處理的值)，插入到已排序中的適當位置，插入時由右而左比較，直到遇到第一個比正處理的值小的值，再插入。比較時，若遇到的值比正處理的值大或相等，則將值往右移。

> 時間複雜度(Time Complexity)：
> * Best Case：Ο(1)
>   當資料的順序恰好為由小到大時，每回合只需比較1次
> * Worst Case：Ο(n2)
>   當資料的順序恰好為由大到小時，第i回合需比i次
> * Average Case：Ο(n2)
>   第n筆資料，平均比較n/2次

**Bubble Sort**
> 從陣列的最前面開始，一次比較陣列中兩兩相鄰的元素，然後根據大小將它們調換順序，大的移到後面：
> 當我們比較過所有元素一次後，可以確保數值最大的元素在最後面
> 接著扣掉陣列中的最後一個元素（因為已經確定它是最大的），接著重複上面的步驟進行兩兩比較
> 重複上述動作，直到排序完畢。假設這個陣列有 6 個元素一共需重複這個動作 5 次（Array.length - 1）才能確保排序完畢。

**Quick Sort**
> 選定一個基準值(Pivot)，將比基準值(Pivot)小的數值移到基準值左邊，形成左子串列，將比基準值(Pivot)大的數值移到基準值右邊，形成右子串列，分別對左子串列、右子串列作上述三個步驟 ⇒ 遞迴(Recursive)，直到左子串列或右子串列只剩一個數值或沒有數值。

> 時間複雜度(Time Complexity)：
> * Best Case：Ο(n log n)
    第一個基準值的位置剛好是中位數，將資料均分成二等份
> * Worst Case：Ο(n2)　
    當資料的順序恰好為由大到小或由小到大時，有分割跟沒分割一樣
> * Average Case：Ο(n log n)
