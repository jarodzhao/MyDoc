import printList

txtFile = open('aabb.txt')

for line in txtFile:
    data = line.split(" ")
    printList.print_movie(data)

print()

txtFile.close()

''' 单行注释怎么写'''

nikeName = ['zhao','haitao','jarod',['a',['afaf','dfdf','efef'],'b','c','d']]

#printList.print_movie(nikeName,0)