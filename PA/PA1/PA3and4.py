class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def ListToBinaryTree(list):

    n = len(list)
    if n==0:
        return None
    
    def helper(index: int=0):
        
        if n<=index or list[index] is None:
            return None
        
        node = TreeNode(list[index])
        node.left = helper(2*index+1)
        node.right = helper(2*index+2)
        return node
        
    return helper()

def ToBinary(n):
    if int(n)<2:
        print(int(n),end="")
    else:
        ToBinary(int(n/2))
        print(int(n)%2,end="")

def construct(postStart, postEnd):
    global preIndex

    if postStart > postEnd:
        return None
    
    node = TreeNode(pre[preIndex])
    preIndex = preIndex+1

    if postStart == postEnd:
        return node
    
    for i in range(len(post)):
        if pre[preIndex]==post[i]:
            postIndex = i

    node.left = construct(postStart, postIndex)
    node.right = construct(postIndex+1, postEnd-1)




def constructTreeUtil(pre:list, post:list, l:int, h:int, size:int):
    global preIndex

    if (preIndex >= size or l > h):
        return None
    
    root = TreeNode(pre[preIndex])
    preIndex += 1

    if l==h or preIndex>=size:
        return root
    
    i=l
    while i<=h:
        #print(post[i])
        if pre[preIndex]==post[i]:
            break
        i+=1

    if i<=h:
        root.left = constructTreeUtil(pre, post, l, i, size)
        root.right = constructTreeUtil(pre, post, i+1, h-1, size)

    return root

def constructTree(pre, post, size):
    
    global preIndex

    return constructTreeUtil(pre, post, 0, size-1, size)

def printInorder(node):
    if node is None:
        return
    
    printInorder(node.left)
    print(node.val, end=" ")

    printInorder(node.right)


if __name__ == "__main__":
    #pre = ['I','Q','J','H','L','E','M','V','O','T','S','B','R','G','Y','Z','K','C','A','&','F','P','N','U','D','W','X']
    #post = ['H','E','M','L','J','V','Q','S','G','Y','R','Z','B','T','C','P','U','D','N','F','W','&','X','A','K','O','I']
    pre = [ 1, 2, 4, 8, 9, 5, 3, 6, 7 ]
    post = [ 8, 9, 4, 5, 2, 6, 7, 3, 1 ]
    
    size = len(pre)
    preIndex = 0

    root = constructTree(pre, post, size)

    #print(root.left.left.right.val)
    printInorder(root)

    



