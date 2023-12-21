current_height = max_height = 1


class BinaryTree:
    def __init__(self, seq):
        self.seq = seq
        self.tree = [seq[0], None, None]
        for i in self.seq[1:]:
            self.add_node(i)

    def add_node(self, number):
        current_node = self.tree
        while True:
            if number > current_node[0]:
                if current_node[2] is None:
                    current_node[2] = [number, None, None]
                    break
                else:
                    current_node = current_node[2]
            elif number == current_node[0]:
                break
            else:
                if current_node[1] is None:
                    current_node[1] = [number, None, None]
                    break
                else:
                    current_node = current_node[1]


def node_height(node):
    global current_height, max_height
    if node[1] is not None:
        current_height += 1
        node_height(node[1])
    if node[2] is not None:
        current_height += 1
        node_height(node[2])
    max_height = max(current_height, max_height)
    current_height -= 1


def avl_balance(tree):
    global current_height, max_height
    node_left_height = node_right_height = 0
    if tree[1] is not None:
        node_left = tree[1]
    else:
        node_left = 0
    if tree[2] is not None:
        node_right = tree[2]
    else:
        node_right = 0
    if node_right != 0:
        current_height = max_height = 1
        node_height(node_right)
        node_right_height = max_height
    if node_left != 0:
        current_height = max_height = 1
        node_height(node_left)
        node_left_height = max_height
    if abs(node_left_height - node_right_height) > 1:
        raise TypeError
    if tree[1] is not None:
        avl_balance(tree[1])
    if tree[2] is not None:
        avl_balance(tree[2])


bin_tree = BinaryTree(list(map(int, input().split()))[:-1])
try:
    avl_balance(bin_tree.tree)
    print("YES")
except TypeError:
    print('NO')
