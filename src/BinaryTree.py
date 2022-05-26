class BinaryTree:
    def __init__(self, infoVal, leftChild=None, rightChild=None):
        self.info = infoVal
        self.left = leftChild
        self.right = rightChild

    def modifyLeft(self, item):
        self.left = BinaryTree(item)

    def modifyRight(self, item):
        self.right = BinaryTree(item)

    def getRootVal(self):
        return self.info

    def setRootVal(self, item):
        self.info = item

    def getLeftChild(self):
        return self.left

    def getRightChild(self):
        return self.right

    def hasNoChild(self):
        return (self.left == None) and (self.right == None)

    def __repr__(self):
        return self.inorderToString()

    def inorderToString(self, front="", back=""):
        if self.hasNoChild():
            return str(self.getRootVal())
        else:
            res = front
            if self.left != None:
                res += self.left.inorderToString(front, back)

            res += str(self.getRootVal())

            if self.right != None:
                res += self.right.inorderToString(front, back)
            res += back

            return res
