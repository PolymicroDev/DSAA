class TreeNode:
    def __init__(self, name, des):
        self.name = name
        self.des = des
        self.children = []
        self.parent = None

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

    def print_tree(self,arg):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        if arg == "name":
            print(prefix + self.name)
            if self.children:
                for child in self.children:
                    child.print_tree("name")

        elif arg == "designation":
            print(prefix + self.des)
            if self.children:
                for child in self.children:
                    child.print_tree("designation")

        elif arg == "both":
            print(prefix + self.name + " " + "(" + self.des +")") 
            if self.children:
                for child in self.children:
                    child.print_tree("both")

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

def build_team_tree():
    root = TreeNode("Nilupul","CEO")

    chinmay = TreeNode("Chinmay", "CTO")
    vishwa = TreeNode("Vishwa","Infrastructure Head")
    vishwa.add_child(TreeNode("Dhaval","Cloud Manager"))
    vishwa.add_child(TreeNode("Abhijit","App Manager"))

    chinmay.add_child(vishwa)
    chinmay.add_child(TreeNode("Aamir","Application Head"))

    gels = TreeNode("Gels", "HR Head")
    gels.add_child(TreeNode("Peter","Recruitment Manager"))
    gels.add_child(TreeNode("Waqas","Policy Manager"))
    

    

    root.add_child(chinmay)
    root.add_child(gels)

    return root

def build_location_tree():
    root = TreeNode("Global")

if __name__ == '__main__':
    root_node = build_team_tree()
    root_node.print_tree("name") # prints only name hierarchy
    root_node.print_tree("designation") # prints only designation hierarchy
    root_node.print_tree("both") # prints both (name and designation) hierarchy

