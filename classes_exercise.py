class Alumno:
    def __init__(self, nombre):
        self.nombre= nombre
    
    def saludar(self):
        print(f"hola, {self.nombre}")

alumno= Alumno("Dario")
#alumno.saludar()

class Node :
    def __init__(self, node, next):
        self.node=int(node)
        self.next=next

    def info_node(self):
        print(f"The value of this node is {self.node} and is next to {self.next}")

node_head=Node(4,"node_B")
node_B=Node(2,"node_C")
node_C=Node(3,"None")

node_head.info_node()


list_node=(node_head,node_B,node_C)
def countNodes(list_node):
    count=0
    if list_node != False:
        for node in list_node:
            count+=1
    return count
print (countNodes(list_node))