class BinaryTree:
    def __init__(self, seq):
        self.seq = seq
        self.tree = [seq[0], None, None]
        self.depths = [1]
        for i in range(1, len(self.seq)):
            self.add_node(i)

    def add_node(self, index):
        current_node = self.tree
        current_height = 1
        while True:
            if self.seq[index] > current_node[0]:
                if current_node[2] is None:
                    current_node[2] = [self.seq[index], None, None]
                    current_height += 1
                    self.depths.append(current_height)
                    break
                else:
                    current_node = current_node[2]
                    current_height += 1
            elif self.seq[index] == current_node[0]:
                break
            else:
                if current_node[1] is None:
                    current_node[1] = [self.seq[index], None, None]
                    current_height += 1
                    self.depths.append(current_height)
                    break
                else:
                    current_node = current_node[1]
                    current_height += 1


bin_tree = BinaryTree(list(map(int, input().split()))[:-1])
print(*bin_tree.depths)
