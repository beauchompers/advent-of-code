from anytree import NodeMixin, RenderTree, search

# classy
class TreeStyle(NodeMixin): 
    def __init__(self, name, location, itemtype, filesize=None, parent=None, children=None):
        super(TreeStyle, self).__init__()
        self.name = name
        self.location = location
        self.itemtype = itemtype
        self.filesize = filesize
        self.parent = parent
        if children:
            self.children = children

with open("day7.txt", "r") as f:
    data = f.read().splitlines()

# get the current working directory
def get_location(location):
    if len(location) == 0:
        return ""
    else:
        return '/'.join(location)

# keep track of current working directory
cwd_location = []

# parse the data and build the tree
for d in data:
    # grab root 
    if d.startswith("$ cd /") : 
        cwd = "/"
        root = TreeStyle("root",cwd,"dir",filesize=0)
    # create the directory and link to parent 
    if d.startswith("dir"):
        directory = d.split(" ")[1]
        current_location = f"{get_location(cwd_location)}"
        if not current_location:
            current_location = "/"
            location_name = f"{directory}"
        else:
            location_name = f"{current_location}/{directory}"
        parent = search.find(root, lambda node: node.location == current_location)
        TreeStyle(d,location_name,"dir",filesize=0,parent=parent)
    # update current working directory
    if d.startswith("$ cd") and not d.startswith("$ cd /") and not d.startswith("$ cd .."):
        directory = d.split(" ")[2]
        cwd_location.append(directory)
    # create the file and link to the parent
    if d[0].isdigit():
        file_size = int(d.split(" ")[0])
        file_name = d.split(" ")[1]
        current_location = f"{get_location(cwd_location)}"
        if not current_location:
            current_location = "/"
            location_name = f"{d}"
        else:
            location_name = f"{get_location(cwd_location)}{d}"
        parent = search.find(root, lambda node: node.location == current_location)
        TreeStyle(d, location_name,"file",filesize=file_size, parent=parent)
    # update current working directory when moving back
    if d == ("$ cd .."):
        cwd_location.pop()

# Part 1

target_filesize = 100000
sizes = []
# add up the sizes and update the file size on the directories in the tree
for pre, fill, node in RenderTree(root):
    if node.itemtype == "dir":
        files = search.findall(node, filter_=lambda node: node.itemtype == "file")
        if files:
            file_size = sum([x.filesize for x in files])
        node.filesize = file_size
        if file_size <= target_filesize:
            print(node.name)
            sizes.append(file_size)

print(f"Small Directories: {sum(sizes)}")

# Part 2
total_size = 70000000
free_space_required = 30000000
current_used = root.filesize
current_free = total_size - current_used
space_required = free_space_required - current_free

smallest = 0
smallest_dir = ""
for pre, fill, node in RenderTree(root):
    if node.itemtype == "dir":
        if node.filesize > space_required:
            smallest = node.filesize
            if node.filesize <= smallest:
                smallest = node.filesize
                smallest_dir = node.name

print(f"Delete {smallest_dir}, size: {smallest}")