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
##setting methods##
    def setName(self,name):
        self.name=name
    def setMid(self,mid):
        self.mid_grade=mid
    def setFinal(self,final):
        self.final_grade=final
    def setPersonality(self,personality):
        self.good=personality





    
class PriorityQueue:

    def __init__(self):
        self.head = None
        self.size = 0

    def displayNodes(self):
        current = self.head
        while current is not None:
            print(current.info.getName(), end=" ")
            current = current.next

    def enqueue(self, value):
        node = Node(value)  # create the node

        if self.size == 0:  # if the queue is empty the node is the head
            self.head = node
            self.size += 1
        else:
            current = self.head

            if value.getPersonality() == True:
                if not self.head.info.getPersonality():  # if all the students in the queue have a bad attitude
                   node.next = self.head
                   self.head = node
                else:
                    while current is not None and current.info.getFinal() > node.info.getFinal() and current.info.getPersonality():
                        previous = current
                        current = current.next

                        if current is not None and current.info.final_grade == node.info.final_grade:  # if the 2 students have the same grade in final and good attitude
                            while current is not None and current.info.getMid() > node.info.getMid() and current.info.getPersonality():
                                previous = current
                                current = current.next

                        previous.next = node
                        node.next = current
                        self.size += 1
                        # add the node before the current if the current has a bad attitude or the node has a final grade > final grade of the current

            else:  # if the new student has a bad attitude, we add it at the end of the queue
                while current.next is not None:
                    current = current.next

                current.next = node

    print("done")


    def dequeueAll(self):
        if self.size == 0:
            print("Queue is empty")
        elif self.size == 1:
            print(self.head.info.getName())   
            del self.head
            self.size-=1

        else:
            current = self.head
            while current is not None:
                print(current.info.getName(), end=" ")
                pre = current
                current = current.next
                del pre
                self.size-=1

        




def addStudent():
    student_name = input("Enter the name of the student: ")
    while True:
        midterm_grade = int(input("Enter the midterm grade of the student: "))
        if 0 <= midterm_grade <= 100:
            break
        else:
            print("Invalid midterm grade. Enter a value between 0 and 100.")
    while True:
        final_grade = int(input("Enter the final grade of the student: "))
        if 0 <= final_grade <= 100:
            break
        else:
            print("Invalid final grade. Enter a value between 0 and 100.")
    while True:
        student_attitude = input("Enter the attitude of the student (Y for good, N for not good): ")
        if student_attitude == "Y" or student_attitude == "N":
            break
        else:
            print("Invalid attitude input. Enter Y for good or N for not good.")
    if student_attitude=="Y":
        good_attitude=True
    else:
        good_attitude=False
    S=Student()
    S.setFinal(final_grade)
    S.setMid(midterm_grade)
    S.setName(student_name)
    S.setPersonality(good_attitude)
    return S



##class of exercise 5##
################################

class Graph:
    def __init__(self):
        self.adj_list = {} #initialize a dictionary

    def addVertex(self):
        vertex=input("Enter the vertex :")
        if vertex not in self.adj_list:
            self.adj_list[vertex] = [] #add a new row to the dictionary

    def removeVertex(self):
        vertex=input("Enter the name of the vertex you want to delete it :")
        if vertex in self.adj_list: #check if the vertex is in the list of vertices 
            del self.adj_list[vertex]
            for neighbors in self.adj_list.values(): #delete the vertex from the neighbor of the other vertices
                if vertex in neighbors:
                    neighbors.remove(vertex)

    def addEdge(self):
        source=input("Enter the name of  the source vertex :")
        destination=input("Enter the name of the destination vertex :")
        if source not in self.adj_list: #add the vertex source to the list of vertices 
            self.adj_list[source] = []
        if destination not in self.adj_list: #add the vertex destination to the list of vertices
            self.adj_list[destination] = []

        self.adj_list[source].append(destination)
        self.adj_list[destination].append(source)

    def removeEdge(self):
        source=input("Enter the name of  the source vertex :")
        destination=input("Enter the name of the destination vertex :")
        if source in self.adj_list and destination in self.adj_list:
            self.adj_list[source].remove(destination)  # remove the destination from the neighbors of the source
            self.adj_list[destination].remove(source) #remove the source from the neighbors of the destination
    
    def displayVertex(self):
        nbr=int(input("Enter the value of the degree :"))
        print("The vertex with degree >",nbr," is :")
        for vertex, neighbors in self.adj_list.items():
            if len(neighbors) >= nbr:
                print(vertex,end=" ")
        print()
            
            
LL=LinkedList()    
Q1=Queue()
S1=Stack()
G=Graph()
PQ=PriorityQueue()
def main():
    print("Welcome!")

    f=True 
    while(f):
        print("Please choose a number from this menu : \n ")
        print(" 1. Singly Linked List \n 2. Check if Palindrome \n 3. Priority Queue \n 4. Evaluate an Infix Expression \n 5. Graph \n 6. Exit \n")
        x=int(input("Ente the number : "))
        if x==1:
            print("You selected the first choice : ")
            singlyLinkedList()
        elif x==2:
            print("You selected the second choice : ")
            checkPalandrome()
        elif x==3:
            print("You selected the third choice : ")
            organizingInterview()
        elif x==4:
            print("You selected the fourth choice : ")
        elif x==5:
            print("You select the fifth choice : ")
            editGraph()
        elif x==6:
            print("You selected the sixth choice : ")
            print("Closing the menu ")
            f=False
    
    print("End of the  program...\nBye byee...")
            


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
        






##exercise3##
###############################
def organizingInterview():
    p=1
    while(p==1):
        print("\nPlease choose a character from this menu : \n ")
        print("a. Add a student \nb. Interview a student \nc. Return to main menu")
        choice=input("Enter the char. :")
        if choice=="a" :
            print("Add all the info of the student:")
            m=addStudent()
            PQ.enqueue(m)
        elif choice=="b" :
            print("The order of the interviews :")
            PQ.dequeueAll()
        elif choice=="c":
            print("Returning to the main menu ...")
            p=0
        else:
            print("Enter :a or b or c  only ")
        



            
##exercise4##
###############################



##exercise5##
###############################
#Adjacency Matrix is better in this problem,because :
##it has less complexity for knowing the len. of each list(list of neighbors of each vertices ) 
##Searching for an edge between v1 and v2  O(1) only
##Removing an edge between v1 and v2 O(1) only

def editGraph():
    q=1
    while(q):
        print("\nPlease choose a character from this menu : \n ")
        print("a. Add vertex \nb. Add edge \nc. Remove vertex \nd. Remove edge \ne. Display vertices with a degree of X or more. \nf. Return to main menu")
        r=input("Enter the char. :")
        if r=="a":
            G.addVertex()
        elif r=="b":
            G.addEdge()
        elif r=="c":
            G.removeVertex()
        elif r=="d":
            G.removeEdge()
        elif r=="e":
            G.displayVertex()
        elif r=="f":
            print("Returning to the main menu ...")
            q=0
        else :
            print("Enter :a or b or c or d or e or f only \n")
            
            
            
            
            
            
            
            
            
main()