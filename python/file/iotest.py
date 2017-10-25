"""
Usage:
"""

man = ['ppp','aaa','ddd','eee','fff']
other = ['afefa','efef','frra','aawq']

try:
    data = open('sketch.txt','w')
    for each_line in data:
        try:
            (role, line, ab) = each_line.split(':',2)
#            if ab == 'h':
#                ab.append('hello')  #列表才能添加对象
            print(role)
            print(line)
            print(ab)
        except ValueError:
            print('ValueError')
    print('zht', file=data)
    data.close()
except IOError:
    print('IOError')
        
        
