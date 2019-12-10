Queue
--------
**特徵**
1. 隊伍有前方(以front表示)以及後方(以back表示)之分。
2. 若要進入隊伍(Push)，一定是從back進入。
3. 若要離開隊伍(Pop)，一定是從front離開。

**功能**
1. Push(data)：把資料從Queue的「後面」放進Queue，並更新成新的back。
2. Pop：把front所指向的資料從Queue中移除，並更新front。
3. getFront：回傳front所指向的資料。
4. getBack：回傳back所指向的資料。
5. IsEmpty：確認Queue裡是否有資料。
6. getSize：回傳Queue裡的資料個數。

**以Linked list實作**
把每筆資料視為node，並且以pointer前後連結：
1. Queue的Push()：在list的「尾巴」新增資料。
2. Queue的Pop()：在list的「開頭」刪除資料。
