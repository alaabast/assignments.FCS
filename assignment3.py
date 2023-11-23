#Assignment_3
#FCS_48
#Name: Alaa Albast
#Date: 30/10/2023


def main():
  name = input("Enter your name: ")
  print("Welcome", name, "!")
  
  while True:
      print("Please choose from this menu what do you want:")
      print("1. Add Matrices \n2. Check Rotation \n3. Invert Dictionary \n4. Convert Matrix to Dictionary \n5. Check Palindrome \n6. Search for an Element & Merge Sort \n7. Exit")
      choice = int(input("Enter your choice: "))
      if choice == 1:
          addMatrices()
          print("\n___________________________\n")
      elif choice == 2:
          checkRotation()
          print("\n___________________________\n")
      elif choice == 3:
          invertDictionary()
          print("\n___________________________\n")
      elif choice == 4:
          matrixToDictionary()
          print("\n___________________________\n")
      elif choice == 5:
          checkPalindrome()
          print("\n___________________________\n")
      elif choice == 6:
          searchElement()
          print("\n___________________________\n")
      elif choice == 7:
          print("\n End of the program,Thank you")
          break
      else:
          print("\n Enter a number between 1 and 7 \n")
          

def addMatrices():
  rows = int(input("Enter the number of rows: "))
  columns = int(input("Enter the number of columns: "))
  matrix1 = []
  matrix2 = []
  matrix3 = []

  print("Enter the elements of the first matrix: ")
  for i in range(rows): #O(N)
      line = []
      for j in range(columns): #O(N)
          line.append(int(input(f"Enter the {j} element of the {i} row: ")))
      matrix1.append(line)
  #COMPLEXITY: O(N^2)
  print("Enter the elements of the second matrix: ")
  for i in range(rows):
      line = []
      for j in range(columns):
          line.append(int(input(f"Enter the {j} element of the {i} row: ")))
      matrix2.append(line)
  #SAME COMPLEXITY: O(N^2)
  for i in range(rows):
      line = []
      for j in range(columns):
          line.append(matrix1[i][j] + matrix2[i][j])
      matrix3.append(line)
  #SAME COMPLEXITY: O(N^2)
  print("The first matrix is:", matrix1)
  print("The second matrix is:", matrix2)
  print("The sum of these two matrices is:", matrix3)
    #COMPLEXITY: O(N^2)
def checkRotation():
  rows = int(input("Enter the number of rows: "))
  columns = int(input("Enter the number of columns: "))
  matrix1 = []
  print("Enter the elements of the matrix: ")
  for i in range(rows):
      line = []
      for j in range(columns):
          line.append(int(input(f"Enter the {j} element of the {i} row: ")))
      matrix1.append(line)
  #COMPLEXITY: O(N^2)
  matrix2=[]
  for i in range(columns):#We inverse the colunms and the rows because the  number of columns and rows are different
    line=[]
    for j in range(rows):
      line.append(matrix1[j][i])
    matrix2.append(line)
   #COMPLEXITY: O(N^2)
  print("The first matrix is:", matrix1)
  print("The second matrix is:", matrix2)
    #COMPLEXITY: O(N^2)
def invertDictionary():
  dict={}
  number=int(input("Enter the number of elements: "))
  for i in range(number): 
    key=input("Enter the key: ")
    value=input("Enter the value: ")
    dict[key]=value
  print("The dictionary is:", dict)
  dict2={}
  l=[]
  i=1
  for k,v in dict.items() :
    if v in l:
      print("we can't invert this dictionary")
      i=2
      break
    l.append(v)
    dict2[v]=k
  if i ==1 :
    print("The inverted dictionary is:", dict2)
    #COMPLEXITY: O(N)
def matrixToDictionary():
    company_info = [["Alaa", "Albast", 1220, "programmer", "meta"],["Ahmad", "Ali", 1243, "nurse", "M hospital"],["Reem", "MM", 2411, "dr.", "Z hospital"]]
    dict = {}
    list1 = []
    m = 1
    for i in range(len(company_info)):
        list2 = []
        for j in range(len(company_info[i])):
            if j == 2:
                if company_info[i][j] not in list1:
                    list1.append(company_info[i][j])
                else:
                    print("we can't create the dictionary because we have the same key in 2 elements (same ID)")
                    m = 2
                    break
            else:
                list2.append(company_info[i][j])
        if m == 2:
            break
        dict[list1[i]] = list2
    print(dict)
    #COMPLEXITY: O(N^2)
def checkPalindrome():
  s = input("Enter a string :")
  if(test(s)) :
    print("it is a palindrome")
  else:
    print("it is not a palindrome")

def test(s):
  if len(s)==0 or  len(s)==1 :
    return True
  return s[0]==s[-1] and test(s[1:-1]) 
    #COMPLEXITY: O(lg N)
def searchElement():

  list = [2, 42, 22, 5, 7, 79, 16, 7, 3, 0, 5, 4, 10]
  x = int(input("Enter the number: "))
  found = False
  for i in range(len(list)):#COMPLEXITY: O(N)
    if list[i] == x:
      m=i
      found = True
      print("The element is found at index", m)
      break

  if not found:
    print("The element is not found")
  else:
    print("The list before sorting:",list)
    print("The sorted list is:",sortList(list))
    
  def sortList(list):#COMPLEXITY: O(N^2)
  for i in range(len(list) - 1):
    for j in range(i + 1, len(list)):
      if list[i] > list[j]:
        list[i], list[j] = list[j], list[i]

  return list
    #COMPLEXITY: O(N^2)

main()
