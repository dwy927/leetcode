问题：找一个字符串中的最长回文子串

我想到的思路：
dp[i] 代表了s 中以 i 为结束点的最长回文子串的长度，
那么 dp[i+1] 就可以依赖于 dp[i]，看和 dp[i] 记录的子串的前一个字母是不是相等，
相等就可以直接+2；
不相等的时候，没有想到想到好的办法，就暴力搜了最长回文子串的长度，不过只需要从dp[i] 记录的子串的那个字母开始搜就好，再往前的就可以不用搜。
有一个边界条件是：在往前找前一个字母的时候，注意判断有没有超过字符串的范围。

中间暴力搜的方法很不优美，搜索了题解，如下：

(一) 最普通的暴力搜索
共有 O(N^2) 个子串，每个子串暴力判断是不是回文串的复杂度为 O(n), 其中 n 是子串的长度，平均值为N/2
故暴力搜索的时间复杂度是 O(N^3)

也可以以每一个字符为中心，向两边寻找回文子串。
在遍历完整个数组后，就可以找到最长的回文子串。但是这个方法的时间复杂度为O(N^2)

(二) 重新定义 dp
dp[j][i] 表示 j 到 i 的字符串是不是回文串
```
for i in range(len(s)): # end
    for j in range(0, i): # start
        dp[j][i] = s[i] == s[j] and (i-j<2 or dp[j+1][i-1])
```
本质是 O(N^2) 找出了每一个回文串，但判断是否为回文串的时间编程了为 O(1)
记录下最大的回文串就能得到结果

(三) 马拉车算法，O(N)复杂度
dp[i] 代表了以 i 为中心的最长回文串的半径。
要额外维护的信息是目前的达到的最靠右边的边界和对应的那个中心点。
这样就可以在右边的点就可以利用中心对应过去左边的点，来复用已有的计算了，
如果没有 cover 住，就只能老老实实的 extend 数过去

此外：由于需要回文串左右对称，故设计了一种巧妙的办法，把偶数长度的回文串，
扩展为奇数长度的，为了左右防止越界，就补上新的符号,如下：
```
aba
#a#b#a#
^#a#b#a#$
```
扩展后的字符串映射回去要仔细对应一下。
