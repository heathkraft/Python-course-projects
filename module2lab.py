#Create file (just using the file provided), with name, address, city/state, and phone number
#Open and read file
#Print the list, with additional formatting 
#count number of people, and print the count. (this step not covered in the lessons so far)

print("")
print("---- People -------------------------------------------")

personnum = 1
#instructor solution: with open('m02_lab_people') as people:
#for person in people:

for person in open('m02_lab_people'):
    print(personnum, "  name:", person.strip())
    personnum += 1

print("")
print("total: ", personnum - 1)