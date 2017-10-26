#coding=utf-8

def print_list(lines):

    for line in lines:

        if isinstance(line, list):

            print_list(line)

        else:
            if not line.find('http-nio-8999-exec-') == -1:
                print(line, end='')
