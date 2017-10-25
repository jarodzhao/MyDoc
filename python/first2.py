# coding=utf-8

import printList

try:
    txtFile = open('aabb.txt')

    for line in txtFile:
        try:
            if not line.find(" ") == -1:
                line = line.split(" ")
                printList.print_movie(line)
            else:
                print(line)
        except ValueError:
            print('发布错误,不存在" "')

    #print('jarod zhao',file=txtFile)

    txtFile.close()

except IOError:
    print('文件读写错误!!!')

''' 单行注释怎么写 '''

nikeName = ['zhao','haitao','jarod',['a',['afaf','dfdf','efef'],'b','c','d']]

#printList.print_movie(nikeName,0)