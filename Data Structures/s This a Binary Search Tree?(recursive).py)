import math
def check_binary_search_tree_(root,mini = -math.inf,maxi = math.inf):
    if root is None:
        return True
    if root.data <=mini or root.data > maxi:
        return False
    return check_binary_search_tree_(root.left,mini,root.data) and check_binary_search_tree_(root.right,root.data,maxi)
