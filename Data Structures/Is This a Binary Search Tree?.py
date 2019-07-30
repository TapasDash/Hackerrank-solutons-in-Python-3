l = []
def inorder(root):
    global l
    if root:
        inorder(root.left)
        l.append(root.data)
        inorder(root.right)
        

def check_binary_search_tree_(root):
    global l
    if l == sorted(l):
        return True
    else:
        return False
