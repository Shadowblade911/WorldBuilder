class Node:
    def set_node_one(self, n):
        self.one = n

    def set_node_two(self, w):
        self.five = w

    def set_node_three(self, e):
        self.two = e

    def set_node_four(self, sw):
            self.four = sw

    def set_node_five(self, se):
        self.three = se



    def set_all_nodes(self, one, e, se, sw, w):
        self.one = one
        self.two = e
        self.five = w
        self.three = se
        self.four = sw

    def __init__(self, one, two, three, four, five, active):
        self.one = one
        self.two = two
        self.three = three
        self.four = four
        self.five = five
        self.active = active


class WorldSphere:
    def __init__(self):
        self.north_pole = Node( None, None, None, None, None, None, False)

        one = Node(self.north_pole, None, None, None, None, False)
        two = Node(self.north_pole, None, None, None, one, False)
        three = Node(self.north_pole, None, None, None, two, False)
        four = Node(self.north_pole, None, None, None, three, False)
        five = Node(self.north_pole, None, None, None, one, False)

        one.set_node_two(five)
        one.set_node_five(two)

        one.set
        two.set_node_two(five)
        three.set_node_two(five)
        four.set_node_two(five)
        five.set_node_two(five)

        self.north_pole.set_all_nodes(rnnw, rnne, rne, rnse,rnsw, rnw)




        self.south_pole = Node( None, None, None, None, None, None, False)