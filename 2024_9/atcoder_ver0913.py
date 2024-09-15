# class SolutionFor0913:
#     def MergeTwoList():
        
list1 = list(map(int,input().split()))
list2 = list(map(int,input().split()))

ForMergingList = []

for i in list1:
    ForMergingList.append(i)
    print(ForMergingList)
    
for i in list2:
    ForMergingList.append(i)
    print(ForMergingList)
    
ForMergingList.sort()
print(ForMergingList)
