from __future__ import annotations


class Node:
    value: int

    def __init__(self, value: int):
        self.value = value


class Tree:
    root: Node | None
    left_child: Tree | None
    right_child: Tree | None

    def __init__(self, root: Node | None):
        self.root = root
        self.left_child = None
        self.right_child = None

    def add(self, node: Node) -> None:
        current_value = self.root.value
        value_to_insert = node.value

        if value_to_insert <= current_value:
            if self.left_child is None:
                self.left_child = Tree(root=node)
            else:
                self.left_child.add(node)
        else:
            if self.right_child is None:
                self.right_child = Tree(root=node)
            else:
                self.right_child.add(node)

    def is_leave(self):
        return self.left_child is None and self.right_child is None

    def print(self) -> None:
        print(self.root.value)
        if not self.is_leave():
            if self.left_child is not None:
                self.left_child.print()
            if self.right_child is not None:
                self.right_child.print()

    def traverse_pre_order(self, initial_list: list[int]) -> list[int]:
        if self.root is not None:
            initial_list.append(self.root.value)
            if self.left_child is not None:
                initial_list = self.left_child.traverse_pre_order(initial_list)
            if self.right_child is not None:
                initial_list = self.right_child.traverse_pre_order(initial_list)

        return initial_list

    def traverse_in_order(self, initial_list: list[int]) -> list[int]:
        if self.root is not None:
            if self.left_child is not None:
                initial_list = self.left_child.traverse_in_order(initial_list)
            initial_list.append(self.root.value)
            if self.right_child is not None:
                initial_list = self.right_child.traverse_in_order(initial_list)

        return initial_list

    def traverse_post_order(self, initial_list: list[int]) -> list[int]:
        if self.root is not None:
            if self.left_child is not None:
                initial_list = self.left_child.traverse_post_order(initial_list)
            if self.right_child is not None:
                initial_list = self.right_child.traverse_post_order(initial_list)
            initial_list.append(self.root.value)

        return initial_list


def main():
    tree = Tree(Node(13))
    tree.add(Node(8))
    tree.add(Node(5))
    tree.add(Node(9))
    tree.add(Node(3))
    tree.add(Node(6))
    tree.add(Node(17))
    tree.add(Node(14))
    tree.add(Node(18))
    tree.add(Node(22))

    print("Erwartung pre-order: [3, 5, 6, 8, 9, 13, 14, 17, 18, 22]")
    print(f"Berechnet pre-order: {tree.traverse_in_order([])}")

    print("---")

    print("Erwartung in-order: [13, 8, 5, 3, 6, 9, 17, 14, 18, 22]")
    print(f"Berechnet in-order: {tree.traverse_pre_order([])}")

    print("---")

    print("Erwartung post-order: [3, 6, 5, 9, 8, 14, 22, 18, 17, 13]")
    print(f"Berechnet post-order: {tree.traverse_post_order([])}")


if __name__ == "__main__":
    main()
