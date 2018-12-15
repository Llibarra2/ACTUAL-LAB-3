#Lester Ibarra
#Diego Aguirre 
#Anindita Nath  
#CS 2302 Data Structures
#11/08/2018 



from AVLTrees import AVLTrees
from AVLTrees import Node
from RBTrees import RBTrees


import time
start_time = time.time()


global tree #variable is created to store either the red and black tree or AVL tree
def countAnagram(word, wordtree,  wordlist, prefix=""):#this method finds the number of anagrams for a word given found in a file containing 354,984 words
    if len(word) <= 1:
        str = prefix + word
        currentNode = wordtree.search(str)
        if currentNode is not None:
            wordlist.append(currentNode.key)
    else:
        for i in range(len(word)):
            cur = word [i: i + 1]
            before = word[0:i]
            after = word[i +1:]
            if cur not in before:
                countAnagram(before + after, wordtree,  wordlist, prefix + cur)
    return len(wordlist)#the number of anagrams found in the file are in a list
                        #return the len of list and you'll have the anagrams total

#The following method fills up the AVL tree with the words in the txt file
#provided.
def populateAVLtree(fileName, tree):
    file = open(fileName, "r")
    for line in file:
        current_line = line.split()
        if isinstance(tree, AVLTrees):
            tree.insert(Node(current_line[0]))
        else:
            tree.insert(current_line[0])
    file.close()

#The following method populates a RB Tree with the words in the txt file provided  
def populateRBTree(fileName, tree):
    file = open(fileName, "r")
    for line in file:
        temp = line.split()
        tem = (temp[0].lower())
        tree.insert(tem)
    file.close()
#The method finds anagrams in the populated tree,  if an anagram is found
#the angram is returned
def print_anagram(word, wordtree, prefix=""):
    if len(word) <= 1:
        str = prefix + word
        currentNode = wordtree.search(str)
        if currentNode is not None:
            print(currentNode.key)
    else:
        for i in range(len(word)):
            cur = word [i: i + 1]
            before = word[0:i]
            after = word[i +1:]
            if cur not in before:
                print_anagram(before + after, wordtree, prefix + cur)
                
#Using the words2.txt file as input, the method uses the words found in the file
#to find the maximum number of anagrams for each word, and then returns the word
#with the most anagrams
def findMaxAnagrams(wordfile, tree):
    finalMaxAnagrams = 0
    wordFound = ""
    
    with open(wordfile, "r") as file:
        for line in file:
            #call the countAnagrams function that returns the anagrams of each word
            #we call it with every word found in the file that is passed as parameter
            #and the global tree that contains the 354, 984 words
            listOfWords = []
            currentMaxAnagrams = countAnagram(line.split()[0], tree, listOfWords)
            
            if currentMaxAnagrams > finalMaxAnagrams:#if the value returned is greater than the FinalMax then that means a new max has been found
                finalMaxAnagrams = currentMaxAnagrams
                wordFound = line.split()[0]
        print("The word with the most anagrams is '%s' and it has [%d] anagrams." % (wordFound, finalMaxAnagrams))
        print("\nThe anagrams of the word '%s' are..." % (wordFound))
        print_anagram(wordFound, tree)
        
def main():
    while True:
        user = input("What tree would you like to use? \n\n1)AVL Tree\n2)RB Tree\n\nEnter response: ")
        if(user == '1' or user == "one"):#check if the user selected AVL Tree
            try:
                tree = AVLTrees() #create an empty tree
                populateAVLtree("words.txt", tree) #populate AVL Tree
                print("AVL Tree Populated")
                print("--- %s seconds ---" % (time.time() - start_time))
                userWord2 = input("\nEnter the word you want to search: ")
                userWord = (userWord2.lower())
                count = [] #list used in  method (countAnagrams)
                test = countAnagram(userWord, tree, count)
                if  test == 0:
                    print("\n\nNo anagrams were found for '%s'"% (userWord))
                else:
                    print("\n\nThe word '%s' has [%d] anagrams." % (userWord, test))
                    print("\nThe anagrams for the word '%s' are..." % (userWord))
                    print_anagram(userWord, tree) #check if the word has anagrams
                
            except FileNotFoundError:
                print("\n\nFile not found.")
                break
            
        #check if the option is an Red Black Tree
        elif user == '2' or user == "two":
            try:
                tree = RBTrees() #create an empty tree
                populateRBTree("words.txt", tree)
                print("--- %s seconds ---" % (time.time() - start_time))
                print("RB Tree is populated")

                userWord2 = input("\nEnter the word you want to search: ")
                userWord = (userWord2.lower())
                count = [] #list used in  method (countAnagrams)
                test = countAnagram(userWord, tree, count)
                if test == 0:
                    print("\n\nNo anagrams were found for '%s'"% (userWord))
                else:
                    print("\n\nThe word '%s' has [%d] anagrams." % (userWord, test))
                    print("\nThe anagrams for the word '%s' are..." % (userWord))
                    print_anagram(userWord, tree) #check if the word has anagrams
                
            except FileNotFoundError:
                print("\n\nFile not found.")
                break
            
        else:
            print("invalid input")
            
        print("\n\n\nFinding the max number of anagrams in 'words4.txt")
        try:
            findMaxAnagrams("words4.txt", tree)
            break
        except FileNotFoundError:
            print("\n\nFile not found.")
            break
        
    print("--- %s seconds ---" % (time.time() - start_time))
                     
main() 
