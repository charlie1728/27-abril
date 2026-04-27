from Node import Node

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def agregar(self, data):
        nuevo = Node(data)
        if not self.head:
            self.head = nuevo
            self.tail = nuevo
            return
        actual = self.head
        while actual.next:
            actual = actual.next
        actual.next = nuevo
        self.tail = nuevo

    def eliminar_k (self, k):
        if self.head == None:
            return
        
        self.tail.next = self.head
        actual = self.head
        anterior = self.tail

        while actual != anterior:
            for i in range(k-1):
                actual = actual.next
                anterior = anterior.next
            
            print(f"Nodo eliminado {actual.data}")

            anterior.next = actual.next
            actual = actual.next

        return f"Nodo restante ={actual.data}"

    def zigzag(self):

        if not self.head or not self.head.next or not self.head.next.next:
            return
        
        primero = self.head
        segundo = primero.next
        tercero = segundo.next

        while (segundo.next):
            primero.next = tercero
            segundo.next = tercero.next
            tercero.next = segundo
            primero = segundo
            if (not primero.next):
                break
            segundo = primero.next
            if (not segundo.next):
                break
            tercero = segundo.next



lista = LinkedList()

for i in [1,2,3,4,5]:
    lista.agregar(i)

lista.zigzag()

actual = lista.head
while actual.next:
    print(f"{actual}", end=" ->")
    actual = actual.next

print(f"{actual} -> None")
