__author__ = 'leo'

# f = open('2.txt', 'r')
# a = {}
#
# for line in f:
#     for char in line:
#         if char and char != '\n':
#             if char in a:
#                 a[char] += 1
#             else:
#                 a[char] = 1
# for i in a:
#     print '%s: %d' % (i, a[i])

data=open('2.txt',"r").read()
# tab=[]
# for car in data:
#     if tab.count(car)==0:
#         tab.append(car)
# print tab

print "".join([char for char in data if char.isalpha()])
