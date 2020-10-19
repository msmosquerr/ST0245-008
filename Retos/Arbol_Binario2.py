import os

class node():
    def __init__(self, dato):
        self.left = None
        self.right = None
        self.dato = dato

class arbol():
   
    def __init__(self):
        self.root = None
        self.cont = 0
    def insert(self, a, dato):
        if a == None:
            a = node(dato)
        else:
            if self.buscar(dato,a) == None:
                d = a.dato
                if dato < d:
                    a.left = self.insert(a.left, dato)
                else:
                    a.right = self.insert(a.right, dato)
            else:
                print("Ya existe")
        return a

    def inorder(self, a):
        if a == None:
            return None
        else:
            
            self.inorder(a.left)
            print(a.dato)
            self.inorder(a.right)
            
    def preorder(self, a):
        if a == None:
            return None
        else:
            print(a.dato)
            self.preorder(a.left)
            self.preorder(a.right)

    def postorder(self, a):
        if a == None:
            return None
        else:
            self.postorder(a.left)
            self.postorder(a.right)
            print(a.dato)

    def buscar(self, dato, a):
        if a == None:
            return None 
        else:
              
            if dato == a.dato:
                return a.dato
                print("Nivel y altura: ", self.cont)
            else:
                self.cont+=1       
                if dato < a.dato:
                    return self.buscar(dato, a.left)
                else:
                    return self.buscar(dato, a.right)
                  
                
        
    def buscarNodo(self, dato, a,anterior):
        if a == None:
            return None
        else:
            if dato == a.dato:
                return [a,anterior]
            else:
                anterior=a
                if dato < a.dato:
                    return self.buscarNodo(dato, a.left,anterior)
                else:
                    return self.buscarNodo(dato, a.right,anterior)

        
    def eliminar(self,dato,nodo):
        if nodo==None:
            return ("No hay elementos para eliminar")
        else:
            lista =self.buscarNodo(dato,nodo,nodo)
            if(lista != None):
                actual = lista[0]
                padre = lista[1]
                padre.left = actual.left
                padre.right = actual.right
                actual = None
                return ("Se a eliminado el nodo",actual)
            return("El elemento no existe")
    


tree = arbol()

while True:
    os.system("cls")
    print("Arbol ABB")
    opc = input("\n1.-Insertar nodo \n2.-Inorden \n3.-Preorden \n4.-Postorden \n5.-Buscar \n6.-Eliminar nodo \n7.-Salir \n\nElige una opcion -> ")
    if opc == '1':
        nodo = input("\nIngresa el nodo -> ")
        if nodo.isdigit():
            nodo = int(nodo)
            tree.root = tree.insert(tree.root, nodo)
        else:
            print("\nIngresa solo digitos...")
    elif opc == '2':
        if tree.root == None:
            print("Vacio")
        else:
            tree.inorder(tree.root)
    elif opc == '3':
        if tree.root == None:
            print("Vacio")
        else:
            tree.preorder(tree.root)
    elif opc == '4':
        if tree.root == None:
            print("Vacio")
        else:
            tree.postorder(tree.root)
    elif opc == '5':
        nodo = input("\nIngresa el nodo a buscar -> ")
        if nodo.isdigit():
            nodo = int(nodo)
            if tree.buscar(nodo, tree.root) == None:
                print("\nNodo no encontrado...")
            else:
                print("\nNodo encontrado -> ",tree.buscar(nodo, tree.root), " si existe...")
        else:
            print("\nIngresa solo digitos...")        
    elif opc == '7':
        print("\nElegiste salir...\n")
        os.system("pause")
        break
    elif opc =='6':
        dato=int(input("Ingrese el nodo a eliminar:"))
        if(tree.buscar(dato,tree.root)==None):
            print("El elemento no está en el arbol")
        else:
            tree.eliminar(dato,tree.root)
            
    else:
        print("\nElige una opcion correcta...")
    print()
    os.system("pause")

print()