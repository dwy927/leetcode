这种list的题，要注意

1. 起点为None的情况，以及next是不是None, 一定不要对None的节点还去找他的next，val
2. 注意把一个节点粘过来的时候，其实只是要那个节点的val,并不想附带这个节点的next值
