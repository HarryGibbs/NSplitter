nameArray = []
splitArray = []
global finalStand
finalStand = []
num1=0
num2=0
totalLength = 0
sequenceArray = ""
fileChecker = True
global refer
refer = {
    1 : ["GCT", "GCC", "GCA", "GCG", "GCU"],
    2 : ["TGT", "TGC", "UGU", "UGC"],
    3 : ["GAT", "GAC", "GUA"],
    4 : ["GAA", "GAG"],
    5 : ["TTT", "TTC", "UUU", "UUC"],
    6 : ["GGT", "GGC", "GGA", "GGG", "GGU"],
    7 : ["CAT", "CAC", "CAU"],
    8 : ["ATT", "ATC", "ATA", "AUU", "AUC", "AUA"],
    9 : ["AAA", "AAG"],
    10 : ["TTG", "TTA", "CTT", "CTC", "CTA", "CTG", "UUG", "UUA", "CUU", "CUC", "CUA", "CUG"],
    11 : ["ATG", "AUG"],
    12 : ["AAT", "AAC", "AAU"],
    13 : ["CCT", "CCC", "CCA", "CCG", "CCU"],
    14 : ["CAA", "CAG"],
    15 : ["CGT", "CGC", "CGA", "CGG", "AGA", "AGG", "CGU"],
    16 : ["TCT", "TCC", "TCA", "TCG", "AGT", "AGC", "UCU", "UCC", "UCA", "UCG", "AGU"],
    17 : ["ACT", "ACC", "ACA", "ACG", "ACU"],
    18 : ["GTT", "GTC", "GTA", "GTG", "GUU", "GUC", "GUA", "GUG"],
    19 : ["TGG", "UGG"],
    20 : ["---", "~~~"],
    21 : ["TAT", "TAC", "UAU", "UAC"],
    22 : ["TAA", "TAG", "TGA", "UAA", "UAG", "UGA"]
}
import os
arr = os.listdir('./input')
targetFile = arr[0]

inputFile = open("./input/" + str(targetFile), 'r+')
content = inputFile.readlines()

#compares 3 different triplets to see if they are the same number above or not
def compare(comp1, comp2, final):
    for i in refer:
        for x in refer[i]:
            if comp1 == x:
                num1 = i
            if comp2 == x:
                num2 = i
    if num1 == num2:
        final.append(1)
    else:
        final.append(2)

#takes 2 triplets and creates 3 children from it, then sends children to be compared in function above
def oneByThreeCompare(comp1, comp2, num1, num2, compareArray):
    
    proceed1 = False
    proceed2 = False
    for i in range(1, len(refer), 1):
        if comp1 in refer[i]:
            proceed1 = True
        if comp2 in refer[i]:
            proceed2 = True
    if proceed1 and proceed2:
        compare(str(comp1), str(comp2), compareArray)
    elif proceed1 == False:
        print("The neucleotide " + str(comp1) + " is not recognised. Please refer to the required naming as on Github.")
        inp = input("Please fix and try again.")
        print(inp)
    elif proceed2 == False:
        print("The neucleotide " + str(comp2) + " is not recognised. Please refer to the required naming as on Github.")
        inp = input("Please fix and try again.")
        print(inp)

#takes the names and adds them to the "nameArray", then makes another string which has all genetic code minus the names (called sequence array)
def removeNames(nameArray, sequenceArray):
    with open("output/u.txt", "w") as file1:
        file1.truncate(0)
    file1.close()
    with open("output/ns.txt", "w") as file2:
        file2.truncate(0)
    file2.close()
    with open("output/s.txt", "w") as file3:
        file3.truncate(0)
    file3.close()
    with open("output/position-values.txt", "w") as file4:
        file4.truncate(0)
    file4.close()
    for i in content:
        if i[0] == ">":
            nameArray.append(i)
        else:
            sequenceArray += str(i)
    findLength(nameArray, sequenceArray)

# reads the length of the first gene sequence to determine the length of all sequences
def findLength(nameArray, sequenceArray):
    firstString = ""
    first = 0
    for i in content:
        if first <= 1:
            if i[0] == ">":
                first += 1
            else:
                firstString += str(i)
        else:
            breaklessString = firstString.replace("\n", "")
            sequenceLength = int(len(breaklessString)/3)
            break
    splitByThrees(nameArray, sequenceArray, sequenceLength)

#takes the sequencearray from the removenames function, then splits all characters and groupsthem by 3
def splitByThrees(names, sequence, length):
    capitalized = sequence.upper()
    breakless = capitalized.replace("\n", "")
    for i in range(0, len(breakless), 3):
        splitArray.append(breakless[i : i + 3])

    bigCompare(names, sequence, splitArray, length)


# compares 2 codons, and if not unchanged it will send them to function oneByThreeCompare for further comparison
def bigCompare(names, base, split, length):
    for i in range(0, int(length), 1):
        compare = [] 
        for x in range(0, len(names), 1):
            comp1 = split[i]
            comp2 = split[int((length*x)+i)]
            if comp1 == comp2:
                compare.append(0)
            elif comp1 != comp2:
                oneByThreeCompare(comp1, comp2, num1, num2, compare)
        if 2 in compare:
            finalStand.append(2)
        else:
            if 1 in compare:
                finalStand.append(1)
            else:
                finalStand.append(0)
        print(i)
    print(len(finalStand))
    printOut(length, split, names)

#large function to print all the U NS and S changes into their respective files
def printOut(length, split, names):
    
    with open("output/u.txt", "w") as file1:
        with open("output/s.txt", "w") as file2:
            with open("output/ns.txt", "w") as file3:
                tallyCounter = 0
                lengthCounter1 = 0
                lengthCounter2 = 0
                lengthCounter3 = 0
                firstName = True
                for x in range(0, len(names),1):
                    for i in range(0, len(finalStand), 1):
                        if i + int(length)*x == int(tallyCounter)*int(length) :
                            if firstName:
                                file1.write(str(names[tallyCounter]))
                                file2.write(str(names[tallyCounter]))
                                file3.write(str(names[tallyCounter]))
                                firstName = False
                                
                            else:
                                file1.write("\n" + str(names[tallyCounter]))
                                file2.write("\n" + str(names[tallyCounter]))
                                file3.write("\n" + str(names[tallyCounter]))
                                lengthCounter1 = 0
                                lengthCounter2 = 0
                                lengthCounter3 = 0
                            tallyCounter += 1

                        if finalStand[i] == 0:
                            if x != 0:
                                if lengthCounter1 >= 19:
                                    file1.write(str(split[i+length*x]) + "\n")
                                    lengthCounter1 = 0
                                else:
                                    file1.write(str(split[i+length*x]))
                                    lengthCounter1 += 1
                            elif x == 0:
                                if lengthCounter1 >= 19:
                                    file1.write(str(split[i]) + "\n")
                                    lengthCounter1 = 0
                                else:
                                    file1.write(str(split[i]))
                                    lengthCounter1 += 1

                        elif finalStand[i] == 1:
                            if x != 0:
                                if lengthCounter2 >= 19:
                                    file2.write(str(split[i+length*x]) + "\n")
                                    lengthCounter2 = 0
                                else:
                                    file2.write(str(split[i+length*x]))
                                    lengthCounter2 += 1
                            elif x == 0:
                                if lengthCounter2 >= 19:
                                    file2.write(str(split[i]) + "\n")
                                    lengthCounter2 = 0
                                else:
                                    file2.write(str(split[i]))
                                    lengthCounter2 += 1

                        elif finalStand[i] == 2:
                            if x != 0:
                                if lengthCounter3 >= 19:
                                    file3.write(str(split[i+length*x]) + "\n")
                                    lengthCounter3 = 0
                                else:
                                    file3.write(str(split[i+length*x]))
                                    lengthCounter3 += 1
                            elif x == 0:
                                if lengthCounter3 >= 19:
                                    file3.write(str(split[i]) + "\n")
                                    lengthCounter3 = 0
                                else:
                                    file3.write(str(split[i]))
                                    lengthCounter3 += 1

                file3.close()
            file2.close()
        file1.close()
    with open("output/position-values.txt", "w") as file4:
        for i in range(0, len(finalStand), 1):
            file4.write(str(finalStand[i]) + "\n")
    file4.close()
    print("100%")




#first function is called, everything starts here
removeNames(nameArray, sequenceArray)
