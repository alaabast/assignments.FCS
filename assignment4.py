#Alaa Albast 
#FCS_c48
#Assignment4





##classes of the exericise 1##
##############################


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
        deleted = int(input("Enter the value you want to delete it"))
        curr = self.head
        prev = None
        flag=0 #check if the value entered by the user is on the list
        while curr: ##from the head to the end of the list
            if curr.info == deleted: #check if the value is availble
                if prev: #if is not the firt node(the head)
                    prev.next = curr.next
                else: #if is the head
                    self.head = curr.next #change the head
                temp = curr # for deleting it from the memory
                curr = curr.next
                #here never change the previous
                del temp
                flag=1 #change the value of flag to know we have the value in this list
            else:
                prev = curr
                curr = curr.next

        if curr is None and prev:
            self.tail = prev
        if(flag==0):
            print(deleted ,"not availble in this list")






##classes of the exericise 2##
##############################


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.items:
            print("Stack is empty")
            return
        m=self.items[-1]
        del self.items[-1]
        return m


    def isEmpty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)
              

    
    
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.items:
            print("Queue is empty")
            return
        n = self.items[0]
        del self.items[0]
        return n

    def isEmpty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)








##classes for exercise3##
################################

class Student:
    def _init_(self,name_student,mid,final,personality):
        self.name=name_student
        self.mid_grade=mid
        self.final_grade=final
        self.good=personality
##getting methods##      
    def getName(self):
        return self.name
    
    def getMid(self):
        return self.mid_grade
    
    def getFinal(self):
        return self.final_grade
    
    def getPersonality(self):
        return self.good
    
##class QueuePriority:
    
    

    
LL=LinkedList()    
Q1=Queue()
S1=Stack()
def main():
    print("Welcome!")

    f=True 
    while(f):
        print("Please choose a number from this menu : \n ")
        print(" 1. Singly Linked List \n 2. Check if Palindrome \n 3. Priority Queue \n 4. Evaluate an Infix Expression \n 5. Graph \n 6. Exit \n")
        x=int(input("Ente the number : "))
        if x==1:
            print("You selected the first choice:")
            singlyLinkedList()
        elif x==2:
            print("You selected the second choice:")
            checkPalandrome()
        elif x==3:
            print("You selected the third choice:")
        elif x==4:
            print("You selected the fourth choice:")
        elif x==5:
            print("You select the fifth:")
        elif x==6:
            print("You selected the sixth choice:")
            print("Closing the menu ")
            f=False
    
    print("End of the  program...\n Bye byee...")
            


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
    



##exercise2##
#############################
def checkPalandrome():
    str = input("Enter a string : ")
    for char in str:  # O(N)
        Q1.enqueue(char)  # insert character into queue
        S1.push(char)  # insert character into stack
    
    i = 0
    mid = S1.size() // 2  # calculate the middle index of the string
    while i<mid :
        s=S1.pop() #pop the last char. from the string
        q=Q1.dequeue() #dequeue the first char from the string
        print("from stack:", s)
        print("from queue:",q)
        if(s!=q): #compare 
            break
        i+=1

    if i == mid: #the while loop has finished
        print(str, " is Palindrome")
    else:
        print(str, " isn't Palindrome")
        
            

main()