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

    def second_max(self):
        current_node = self.tree
        prev_branch = current_node[0]
        left = False
        while True:
            if current_node[2] is not None:
                prev_branch = current_node[0]
                current_node = current_node[2]
            else:
                if current_node[1] is not None:
                    if not left:
                        current_node = current_node[1]
                        left = True
                    else:
                        return current_node[0]
                else:
                    if not left:
                        return prev_branch
                    else:
                        return current_node[0]


bin_tree = BinaryTree(list(map(int, input().split()))[:-1])
print(bin_tree.second_max())
