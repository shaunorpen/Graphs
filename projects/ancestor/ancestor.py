
def get_parent(ancestors, starting_node):
    for (parent, child) in ancestors:
        if child == starting_node:
            return parent

def earliest_ancestor(ancestors, starting_node, iterations = 0):
    if get_parent(ancestors, starting_node) is None:
        if iterations == 0:
            return -1
        else:
            return starting_node
    else:
        iterations += 1
        return earliest_ancestor(ancestors, get_parent(ancestors, starting_node), iterations)
