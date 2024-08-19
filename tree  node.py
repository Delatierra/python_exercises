class Node:
    def __init__(self, interger, Node_left, Node_right):
        self.interger=interger
        self.Node_left=Node_left
        self.Node_right=Node_right
    
def count(node_list):
    sum_list=0
    for node in node_list:
        if node.Node_left==node.Node_right:
            sum_list+=1
    return sum_list

Node_first=Node(0,1,0)
Node_second=Node(1,None,None)
Node_third=Node(0,1,0)
Node_forth=Node(1,1,1)
Node_fifth=Node(0,None,None)
Node_sixth=Node(1,None,None)
Node_seventh=Node(1,None,None)

list= (Node_first, Node_second, Node_third, Node_forth, Node_fifth, Node_sixth, Node_seventh)

print (count(list))