#Alaa Albast 
#FCS_c48
#Assignment4

##functions of the exericise 1##
class Node:

    def __init__(self, info):
        self.info = info
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.current = self.head ##when we use current the complexity of adding a node is O(1) not O(N)
        

    def addNode(self):
        num = int(input("Enter a number to add it to the LL :")) #the info entered by the user
        
        node = Node(num) #create a node
        if self.head is None:  #if this node is the first node in the LL
            self.head = node 
            self.current = node
            LL.head = node
        else: # if isn't
            self.current.next = node
            self.current = node
        print("we add ", num) 

    def displaysNodes(self):
        a = self.head
        while a != None:
            print(a.info, end=" ")
            a = a.next
        print()

    def deleteNode(self):
        deleted=int(input("Enter the value you want to delete it"))
        curr = self.head
        if self.head is not None:
            if self.head.info == deleted:
                temp = self.head
                curr = self.head.next
                del temp
            prev = None
            while curr is not None:
                if curr.info == deleted:
                    prev.next = curr.next
                    del curr
                else:
                    prev = curr
                curr = curr.next

    
    
    
LL=LinkedList()    

def main():
    print("Welcome!")


    while(True):
        print("Please choose a number from this menu : \n ")
        print(" 1. Singly Linked List \n 2. Check if Palindrome \n 3. Priority Queue \n 4. Evaluate an Infix Expression \n 5. Graph \n 6. Exit \n")
        x=int(input("Ente the number : "))
        if x==1:
            print("You selected the first choice:")
            singlyLinkedList()
        elif x==2:
            print("You selected the second choice:")
            
              

##exerice1##
#################################
def singlyLinkedList():
    x=1
    while(x==1):
        print("\nPlease choose a character from this menu : \n ")
        print(" a. Add Node \n b. Display Nodes \n c. Search for & Delete Node \n d. Return to main menu \n")
        y=input("Enter the char. : ")
        if y=="a":
            LL.addNode()
        elif y=="b":
            LL.displaysNodes()
        elif y=="c":
            LL.deleteNode()
        elif y=="d":
            print("Returning to the main menu ...")
            x=0
        else:
            print("Enter :a or b or c or d only ")
    




main()