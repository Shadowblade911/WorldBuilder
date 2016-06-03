class Node:
    def set_node_one(self, one):
        self.one = one

    def set_node_two(self, two):
        self.two = two

    def set_node_three(self, three):
        self.three = three

    def set_node_four(self, four):
        self.four = four

    def set_node_five(self, five):
        self.five = five

    def get_node_one(self):
        return self.one

    def get_node_two(self):
        return self.two

    def get_node_three(self):
        return self.three

    def get_node_four(self):
        return self.four

    def get_node_five(self):
        return self.three

    def set_all_nodes(self, one, e, se, sw, w):
        self.one = one
        self.two = e
        self.five = w
        self.three = se
        self.four = sw

    def set_active(self, bool):
        self.active = bool

    def set_elevation(self, val):
        self.elevation = val

    def __init__(self, one, two, three, four, five):
        self.one = one
        self.two = two
        self.three = three
        self.four = four
        self.five = five
        self.active = False
        self.elevation = 1


class WorldSphere:
    def __init__(self):
        #this creates a northern pole for us to use as an access point
        self.north_pole = Node(None, None, None, None, None)

        north_one = Node(self.north_pole, None, None, None, None)
        north_two = Node(self.north_pole, north_one, None, None, None)

        self.north_pole.set_node_two(north_two)
        north_one.set_node_five(north_two)

        north_three = Node(self.north_pole, north_two, None, None, None)
        self.north_pole.set_node_three(north_three)
        north_two.set_node_five(north_three)

        north_four = Node(self.north_pole, north_three, None, None, None)

        self.north_pole.set_node_four(north_four)
        north_three.set_node_five(north_four)

        north_five = Node(self.north_pole, north_four, None, None, north_one)

        self.north_pole.set_node_five(north_five)

        #this creates the southern pole, using the same pattern as the north pole
        self.south_pole = Node(None, None, None, None, None)

        south_one = Node(self.south_pole, None, None, None, None)
        south_two = Node(self.south_pole, south_one, None, None, None)

        self.south_pole.set_node_two(south_two)
        south_one.set_node_five(south_two)

        south_three = Node(self.south_pole, south_two, None, None, None)
        self.south_pole.set_node_three(south_three)
        south_two.set_node_five(south_three)

        south_four = Node(self.south_pole, south_three, None, None, None)

        self.south_pole.set_node_four(south_four)
        south_three.set_node_five(south_four)

        south_five = Node(self.south_pole, south_four, None, None, north_one)

        self.south_pole.set_node_five(south_five)

        # we now have the two halves of the sphere. Now we connect the two at a slight rotation.
        north_one.set_node_three(south_two)
        north_one.set_node_four(south_one)

        north_two.set_node_three(south_one)
        north_two.set_node_four(south_five)

        north_five.set_node_three(south_three)
        north_five.set_node_four(south_two)

        north_four.set_node_three(south_four)
        north_four.set_node_four(south_three)

        north_three.set_node_three(south_five)
        north_three.set_node_four(south_four)

        south_one.set_node_three(north_two)
        south_one.set_node_four(north_one)

        south_two.set_node_three(north_one)
        south_two.set_node_four(north_five)

        south_three.set_node_three(north_five)
        south_three.set_node_four(north_four)

        south_four.set_node_three(north_four)
        south_four.set_node_four(north_three)

        south_five.set_node_three(north_three)
        south_five.set_node_four(north_two)




