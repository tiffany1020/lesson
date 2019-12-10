Queue(First-In-First-Out 先進先出)
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
(把每筆資料視為node，並且以pointer前後連結)
1. Queue的Push()：在list的「尾巴」新增資料。
2. Queue的Pop()：在list的「開頭」刪除資料。


Stack(Last-In-First-Out 後進先出)
-------------
**功能**
1. Push(data)：把資料放進Stack。
2. Pop：把「最上面」的資料從Stack中移除。
3. Top：回傳「最上面」的資料，不影響資料結構本身。
4. IsEmpty：確認Stack裡是否有資料，不影響資料結構本身。
5. getSize：回傳Stack裡的資料個數，不影響資料結構本身。

**應用**
1. 編輯器(如word、sublime等等)中的undo。
2. 網頁瀏覽器的「回到前一頁」功能。
3. 編譯器(compiler)中的Parsing。
4. 任何遞迴(recursion)形式的演算法，都可以用Stack改寫，例如Depth-First Search(DFS，深度優先搜尋)。
5. 於記憶體管理(memory management)中的Call Stack。


參考資料:
1. https://alrightchiu.github.io/SecondRound/queue-introjian-jie-bing-yi-linked-listshi-zuo.html
2. http://alrightchiu.github.io/SecondRound/stack-introjian-jie.html
3. https://www.geeksforgeeks.org/stack-in-python/
