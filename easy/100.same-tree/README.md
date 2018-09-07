python
class里面递归调用自己的方法: 需要 `self.isSameTree(p.left, q.left)`
用到`self`, 否则编译出错

还有，python的语法不能`if !self.isSameTree(p.left, q.left):`
要`if self.isSameTree(p.left, q.left) == False:`
