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
        #this creates a northern pole for us to use as an access point
        self.north_pole = Node( None, None, None, None, None, None, False)

        north_one = Node(self.north_pole, None, None, None, None, False)
        north_two = Node(self.north_pole, north_one, None, None, None, False)

        self.north_pole.set_node_two(north_two)
        north_one.set_node_five(north_two)

        north_three = Node(self.north_pole, north_two, None, None, None, False)
        self.north_pole.set_node_three(north_three)
        north_two.set_node_five(north_three)

        north_four = Node(self.north_pole, north_three, None, None, None, False)

        self.north_pole.set_node_four(north_four)
        north_three.set_node_five(north_four)

        north_five = Node(self.north_pole, north_four, None, None, north_one, False)

        self.north_pole.set_node_five(north_five)

        #this creates the southern pole, using the same pattern as the north pole
        self.south_pole = Node( None, None, None, None, None, None, False)

        south_one = Node(self.south_pole, None, None, None, None, False)
        south_two = Node(self.south_pole, south_one, None, None, None, False)

        self.south_pole.set_node_two(south_two)
        south_one.set_node_five(south_two)

        south_three = Node(self.south_pole, south_two, None, None, None, False)
        self.south_pole.set_node_three(south_three)
        south_two.set_node_five(south_three)

        south_four = Node(self.south_pole, south_three, None, None, None, False)

        self.south_pole.set_node_four(south_four)
        south_three.set_node_five(south_four)

        south_five = Node(self.south_pole, south_four, None, None, north_one, False)

        self.south_pole.set_node_five(south_five)





