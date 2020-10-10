class Node(object):
    def __init__(self, val, nick = None):
        self.val = val
        if nick == None:
            self.nick = str(val)[:4]
        else:
            self.nick = nick
        self.left = None
        self.right = None
        self.offset = None
    def insert_left(self, child):
        if self.left is None:
            self.left = child
        else:
            child.left = self.left
            self.left = child
    def insert_right(self, child):
        if self.right is None:
            self.right = child
        else:
            child.right = self.right
            self.right = child
    def has_left(self):
        return type(self.left).__name__ == 'Node'
    def has_right(self):
        return type(self.right).__name__ == 'Node'
    def has_offset(self):
        return type(self.offset).__name__ == 'int'
    def copy(self, flipped = False):
        lefty = None
        righty = None
        if self.has_left():
            if flipped:
                righty = self.left.copy(flipped)
            else:
                lefty = self.left.copy(flipped)
        if self.has_right():
            if flipped:
                lefty = self.right.copy(flipped)
            else:
                righty = self.right.copy(flipped)
        retval = Node(self.val, self.nick)
        retval.insert_left(lefty)
        retval.insert_right(righty)
        return retval
        
    def set_offsets(self, begin_at = 0, use_nicks = False):
        #begin_at should be nonzero when passed to right children only,
        #and should be how many characters are in the parent and its left subtree.
        #Returns the total length of the strings in the tree.
        left_length = 0
        if self.has_left():
            left_length = self.left.total_length(use_nicks)
            self.left.set_offsets(begin_at, use_nicks)
        self.offset = begin_at + left_length
        if self.has_right():
            to_use = str(self.val)
            if use_nicks:
                to_use = str(self.nick)
            self.right.set_offsets(self.offset + len(to_use), use_nicks)

    def total_length(self, use_nicks = False):
        retval = len(str(self.val))
        if use_nicks:
            retval = len(str(self.nick))
        if self.has_left():
            retval += self.left.total_length(use_nicks)
        if self.has_right():
            retval += self.right.total_length(use_nicks)
        return retval

    def height(self):
        height_left = 0
        height_right = 0
        if self.has_left():
            height_left = self.left.height()
        if self.has_right():
            height_right = self.right.height()
        return max(height_left, height_right)+1

    def shortform(self):
        return self.__str__(use_nicks = True)
    
    def __str__(self, level = 0, matrix = None, use_nicks = False):
        """The node adds its string version to the given level in the matrix.
        If that level does not exist yet, then the node adds it to the matrix first.
        Next, __str__ is called on the left and right children, if they exist."""
        if matrix is None:
            matrix = []
        if level > len(matrix):
            print("ERROR in Node.__str__(): level is greater than length of matrix")
            return
        if level == len(matrix):
            matrix.append("")
        #Now we add the string version to the given level.
        #We compare our offset to the length of the level so far,
        #and add as many spaces as necessary first.
        if level == 0:
            #print("DEBUG: matrix is of length",len(matrix))
            self.set_offsets(use_nicks = use_nicks)
        offset = self.offset
        lenny = len(matrix[level])
        if lenny > offset:
            print("ERROR in Node.__str__(): length of string", matrix[level],
                  "at level", level, "greater than offset", offset)
            return
        to_use = str(self.val)
        if use_nicks:
            to_use = str(self.nick)
        matrix[level] += " " * (offset - lenny) + to_use
        if self.has_left():
            self.left.__str__(level + 1, matrix, use_nicks)
        if self.has_right():
            self.right.__str__(level + 1, matrix, use_nicks)
        return "\n".join(matrix)

