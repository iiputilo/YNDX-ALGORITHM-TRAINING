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

    def in_ascending_order(self, tree):
        if tree[1] is not None:
            self.in_ascending_order(tree[1])
            print(tree[0])
        else:
            print(tree[0])
        if tree[2] is not None:
            self.in_ascending_order(tree[2])


bin_tree = BinaryTree(list(map(int, input().split()))[:-1])
bin_tree.in_ascending_order(bin_tree.tree)
