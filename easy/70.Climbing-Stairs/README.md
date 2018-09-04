本质是斐波那契数列：

```
a = 1
b = 1
for i in range(n):
    a, b = b, a + b
return a
```
