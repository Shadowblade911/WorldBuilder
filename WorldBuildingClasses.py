class Node:
    def __init__(self, one, two, three, four, five, six):
        self.node_one = one
        self.node_two = two
        self.node_three = three
        self.node_four = four
        self.node_five = five
        self.node_six = six
        self.active = False
        self.elevation = 1

    @property
    def node_one(self):
        return self.node_one

    @node_one.setter
    def node_one(self, one):
        self.node_one = one

    @property
    def node_two(self):
        return self.node_two

    @node_two.setter
    def node_two(self, two):
        self.node_two = two

    @property
    def node_three(self):
        return self.node_three
    
    @node_three.setter
    def node_three(self, three):
        self.node_three = three

    @property
    def node_four(self):
        return self.node_four

    @node_four.setter
    def node_four(self, four):
        self.node_four = four

    @property
    def node_five(self):
        return self.node_five
    
    @node_five.setter
    def node_five(self, five):
        self.node_five = five

    @property
    def node_six(self):
        return self.node_six

    @node_six.setter
    def node_six(self, six):
        self.node_six = six

    def node_bridge(self, node):
        return {
            self.node_one: 1,
            self.node_two: 2,
            self.node_three: 3,
            self.node_four: 4,
            self.node_five: 5,
            self.node_six: 6
        }[node]

    def node_connector(self, node):
        if self.node_one.node_bridge(node) is not None:
            return self.node_one
        elif self.node_two.node_bridge(node) is not None:
            return self.node_two
        elif self.node_three.node_bridge(node) is not None:
            return self.node_three
        elif self.node_four.node_bridge(node) is not None:
            return self.node_four
        elif self.node_five.node_bridge(node) is not None:
            return self.node_five
        elif self.node_six.node_bridge(node) is not None:
            return self.node_six
        else:
            return None

    def all_used_nodes(self):

        nodes = set()

        if self.node_one is not None:
            nodes.add(self.node_one)

        if self.node_two is not None:
            nodes.add(self.node_two)

        if self.node_three is not None:
            nodes.add(self.node_three)

        if self.node_four is not None:
            nodes.add(self.node_four)

        if self.node_five is not None:
            nodes.add(self.node_five)

        if self.node_six is not None:
            nodes.add(self.node_six)

        return nodes

    def find_immediate_connectors(self, node):
        connectors = set()

        if self.node_one.node_bridge(node) is not None:
            connectors.add(self.node_one.node_bridge(node))

        if self.node_two.node_bridge(node) is not None:
            connectors.add(self.node_two.node_bridge(node))

        if self.node_three.node_bridge(node) is not None:
            connectors.add(self.node_three.node_bridge(node))

        if self.node_four.node_bridge(node) is not None:
            connectors.add(self.node_four.node_bridge(node))

        if self.node_five.node_bridge(node) is not None:
            connectors.add(self.node_five.node_bridge(node))

        if self.node_six.node_bridge(node) is not None:
            connectors.add(self.node_six.node_bridge(node))

        return connectors

    def insert_node(self, node):
        if self.node_connector(node) is None:
            return None

        my_connection = self.node_bridge(node)
        node_connection = node.node_bridge(self)

        new_node = Node(node, None, None, None, None, self)

        if my_connection is 1:
            self.node_one = new_node
        if my_connection is 2:
            self.node_two = new_node
        if my_connection is 3:
            self.node_three = new_node
        if my_connection is 4:
            self.node_four = new_node
        if my_connection is 5:
            self.node_five = new_node
        if my_connection is 6:
            self.node_six = new_node

        if node_connection is 1:
            node.node_one = new_node
        if node_connection is 2:
            node.node_two = new_node
        if node_connection is 3:
            node.node_three = new_node
        if node_connection is 4:
            node.node_four = new_node
        if node_connection is 5:
            node.node_five = new_node
        if node_connection is 6:
            node.node_six = new_node

        return node

    def split_node(self, node):
        if self.node_connector(node) is not None:

            new_node_set = set()
            connectors = self.find_immediate_connectors(node)
            bridge_line = self.node_bridge(node)

            new_node = self.insert_node(node)
            new_node_set.add(new_node)

            while connectors:
                existing_node = connectors.pop()

                if self.node_bridge(existing_node) > bridge_line or \
                        (bridge_line == 5 and self.node_bridge(existing_node) == 1):
                    right_side = True
                else:
                    right_side = False

                two_or_five = existing_node.insert_node(node)
                three_or_four = self.insert_node(existing_node)

                new_node_set.add({two_or_five, three_or_four})

                if right_side:
                    new_node.node_two = two_or_five
                    two_or_five.node_five = new_node

                    new_node.node_three = three_or_four
                    three_or_four.node_four = new_node

                    two_or_five.node_four = three_or_four
                    three_or_four.node_five = two_or_five

                else:

                    new_node.node_five = two_or_five
                    two_or_five.node_two = two_or_five

                    new_node.node_four = three_or_four
                    three_or_four.three = new_node

                    two_or_five.node_three = three_or_four
                    three_or_four.node_two = two_or_five

        else:
            # this is the case where the line has already been split
            pass

    def set_all_nodes(self, one, two, three, four, five, six):
        self.node_one = one
        self.node_two = two
        self.node_three = three
        self.node_four = four
        self.node_five = five
        self.node_six = six

    def set_active(self, val):
        self.active = val

    def set_elevation(self, val):
        self.elevation = val


class WorldSphere:
    def add_layer(self):
        active_set = {self.north_pole}.add(self.north_pole.all_used_nodes())
        finalized_set = set()
        while active_set:
            node = active_set.pop()
            finalized_set.add(node)
            new_nodes = active_set.difference(node.all_used_nodes())
            active_set += new_nodes

    def __init__(self):
        # this creates a northern pole for us to use as an access point
        self.north_pole = Node(None, None, None, None, None, None)

        north_one = Node(self.north_pole, None, None, None, None, None)
        north_two = Node(self.north_pole, north_one, None, None, None, None)

        self.north_pole.node_two = north_two
        north_one.node_five = north_two

        north_three = Node(self.north_pole, north_two, None, None, None, None)
        self.north_pole.node_three = north_three
        north_two.node_five = north_three

        north_four = Node(self.north_pole, north_three, None, None, None, None)

        self.north_pole.node_four = north_four
        north_three.node_five = north_four

        north_five = Node(self.north_pole, north_four, None, None, north_one, None)

        self.north_pole.node_five = north_five

        # this creates the southern pole, using the same pattern as the north pole
        self.south_pole = Node(None, None, None, None, None, None)

        south_one = Node(self.south_pole, None, None, None, None, None)
        south_two = Node(self.south_pole, south_one, None, None, None, None)

        self.south_pole.node_two = south_two
        south_one.node_five = south_two

        south_three = Node(self.south_pole, south_two, None, None, None, None)
        self.south_pole.node_three = south_three
        south_two.node_five = south_three

        south_four = Node(self.south_pole, south_three, None, None, None, None)

        self.south_pole.node_four = south_four
        south_three.node_five = south_four

        south_five = Node(self.south_pole, south_four, None, None, north_one, None)

        self.south_pole.node_five = south_five

        # we now have the two halves of the sphere. Now we connect the two at a slight rotation.
        north_one.node_three = south_two
        north_one.node_four = south_one

        north_two.node_three = south_one
        north_two.node_four = south_five

        north_five.node_three = south_three
        north_five.node_four = south_two

        north_four.node_three = south_four
        north_four.node_four = south_three

        north_three.node_three = south_five
        north_three.node_four = south_four

        south_one.node_three = north_two
        south_one.node_four = north_one

        south_two.node_three = north_one
        south_two.node_four = north_five

        south_three.node_three = north_five
        south_three.node_four = north_four

        south_four.node_three = north_four
        south_four.node_four = north_three

        south_five.node_three = north_three
        south_five.node_four = north_two
