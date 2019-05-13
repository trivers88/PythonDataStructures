class BinaryTree(object):

    def __init__(self, rootObj):
        self.key = rootObj
        self.left = None
        self.right = None

    def insert_left(self, newNode):
        if self.left == None:
            self.left = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.left = self.left
            self.left = t
    
    def insert_right(self, newNode):
        if self.right == None:
            self.right = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.right = self.right
            self.right = t
    
    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right

    def set_root_val(self, obj):
        self.key = obj

    def get_root_val(self):
        return self.key

