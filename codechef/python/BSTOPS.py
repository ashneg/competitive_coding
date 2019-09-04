class Node:
    def __init__(self,val,pos):
        self.val = val
        self.pos = pos
        self.right = None
        self.left = None

def insert(node,val,pos):
    if(node == None):
        print(pos)
        return Node(val,pos)
    if(val < node.val):
        node.left = insert(node.left, val,2*pos)
    else:
        node.right = insert(node.right, val,2*pos+1)
    return node
    
def min(val):
    curnode = val
    while(curnode.left!= None):
        curnode = curnode.left
    return curnode
    
def delete(node,val):
    if(node == None):
        return node
    if(val<node.val):
        node.left = delete(node.left,val)
    elif(val>node.val):
        node.right = delete(node.right,val)
    else:
        print(node.pos)
        if(node.left is None):
            temp = node.right   
            node = None
            return temp
        elif(node.right is None):
            temp = node.left
            node = None
            return temp
        temp = min(node.right)
        node.val = temp.val
        node.right = delete(node.right,temp.val)
    return node

q = None
root = None    
q = int(input())
pos = -1
for _ in range(q):
    operation,node = map(str,input().split())
    if(operation == 'i'):
        root = insert(root,int(node),1)
    elif(operation == 'd'):
        root = delete(root, int(node))
