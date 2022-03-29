COUNT=[10]
class BST:
    def __init__(self, data):
        self.right = None
        self.left = None
        self.data = data


def insert(node, data):
    if node is None:
        return BST(data)
    if data < node.data:
        node.left = insert(node.left, data)
    else:
        node.right = insert(node.right, data)
    return node


def minnode(node):
    tem = node
    while tem.left is not None:
        tem = tem.left
    return tem


def maxnode(node):
    temp = node
    while temp.right is not None:
        temp = temp.right
    return temp


def deletenode(node, data):
    if node is None:
        return node
    if data < node.data:
        node.left = deletenode(node.left, data)
    elif data > node.data:
        node.right = deletenode(node.right, data)
    else:
        if node.left and node.right is None:
            node = None
            return node
        elif node.right or node.left is None:
            if node.left is None:
                node = node.right
                return node
            elif node.right is None:
                node = node.left
                return node
        temp = minnode(node.right)
        node.data = temp.data
        node.right = deletenode(node.right, temp.data)
    return node


def inorder(node):
    if node is not None:
        inorder(node.left)
        print(str(node.data), end=' ')
        inorder(node.right)


def preorder(node):
    if node is not None:
        print(str(node.data), end=' ')
        preorder(node.left)
        preorder(node.right)


def postorder(node):
    if root is not None:
        preorder(node.left)
        preorder(node.right)
        print(str(node.data), end=' ')

def display(root, space):
    global COUNT
    if root is None:
        return
    space = space + COUNT[0]
    display(root.right, space)
    print()
    for i in range(COUNT[0], space):
        print(end=" ")
    print(root.data)
    display(root.left, space)

root = None
while True:
    print("\n1. INSERT")
    print("2. DELETE")
    print("3. MINIMUM VALUE")
    print("4. MAXIMUM VALUE")
    print("5. INORDER")
    print("6. POSTORDER")
    print("7. PREORDER")
    print("8. EXIT")

    ch = int(input("Enter choice: "))

    if ch == 1:
        b = int(input("Enter The Element to Insert: "))
        root = insert(root,b)
    elif ch == 2:
        b = int(input("Enter The Element to Delete: "))
        deletenode(root,b)
    elif ch == 3:
        temp = minnode(root)
        print("\n The Minimum Value is",temp.data)
    elif ch == 4:
        temp = maxnode(root)
        print("\n The Maximum Value is", temp.data)
    elif ch == 5:
        display(root,0)
    elif ch == 6:
        postorder(root)
    elif ch == 7:
        preorder(root)
    elif ch == 8:
        exit(0)
    else:
        print("Invalid choice!")
