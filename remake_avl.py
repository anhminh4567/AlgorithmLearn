class BalanceTree():
    value: int = None
    left: "BalanceTree" = None
    right: "BalanceTree" = None
    parent: "BalanceTree" = None
    height: int = 0
    #       more than 0: The node is "right heavy".
    #       less than 0: The node is "left heavy".
    @property
    def is_root(self):
        return self.parent is None
    
    def cal_balance_factor(self):
        if not self.left and not self.right:
            return 0
        if not self.left:
            return self.right.height
        if not self.right:
            return -self.left.height
        return self.right.height - self.left.height
    
    def insert(self, newVal: int):
        pass
    # when right right 
    def rotate_left(self):
        if not self.right:
            return
        right_node = self.right
        left_of_right_node  = right_node.left
        
        parent = self.parent
        
        self.right = left_of_right_node
        right_node.left = self
        right_node.parent = parent
        self.parent = right_node
        if parent:
            if parent.left == self:
                parent.left = right_node
            else:
                parent.right = right_node
        
        if left_of_right_node:
            left_of_right_node.parent = self
            
        #recal height
        
        
        
    # when left left
    def rotate_right(self):
        if not self.left:
            return
        
        left_node = self.left
        right_of_left_node = left_node.right
        
        parent = self.parent
        
        self.left = right_of_left_node
        left_node.right = self
        self.parent = left_node
        left_node.parent = parent
        if parent:

            parent.left = left_node
        
        self.height = self.cal_balance_factor()
        left_node = left_node.cal_balance_factor()
        
    
    