class BinaryTree:
    def __init__(self, seq):
        self.seq = seq
        self.tree = [seq[0], None, None]
        for i in range(1, len(self.seq)):
            self.add_node(i)

    def add_node(self, index):
        current_node = self.tree
        while True:
            if self.seq[index] > current_node[0]:
                if current_node[2] is None:
                    current_node[2] = [self.seq[index], None, None]
                    break
                else:
                    current_node = current_node[2]
            elif self.seq[index] == current_node[0]:
                break
            else:
                if current_node[1] is None:
                    current_node[1] = [self.seq[index], None, None]
                    break
                else:
                    current_node = current_node[1]


def leaves(tree):
    if tree[1] is not None:
        leaves(tree[1])
    if tree[2] is not None:
        leaves(tree[2])
    if tree[2] is None and tree[1] is None:
        print(tree[0])


bin_tree = BinaryTree(list(map(int, input().split()))[:-1])
leaves(bin_tree.tree)
