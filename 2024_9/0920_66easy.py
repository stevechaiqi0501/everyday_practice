# class SolutionFor66:
#     def For66easy(self,nums:list[int]):

numsList = [1,2,3]
numsInt = int(''.join(map(str,numsList)))

result_numsInt = numsInt + 1
result_numsStr = str(result_numsInt)

result = []
#１を加えたint型のnumsをresultにlistとして入力する
for i in range(len(result_numsStr)):
    temp_int = result_numsInt%10
    result.append(temp_int)
    reversed_result = result[::-1]
    result_numsInt = result_numsInt // 10
    
print(reversed_result)

#絶対もっとスマートな方法あるって