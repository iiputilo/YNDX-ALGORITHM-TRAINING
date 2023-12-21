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


def max_one_children(tree):
    if tree[1] is not None:
        max_one_children(tree[1])
        if tree[2] is None:
            print(tree[0])
    if tree[2] is not None:
        if tree[1] is None:
            print(tree[0])
        max_one_children(tree[2])


bin_tree = BinaryTree(list(map(int, input().split()))[:-1])
max_one_children(bin_tree.tree)
