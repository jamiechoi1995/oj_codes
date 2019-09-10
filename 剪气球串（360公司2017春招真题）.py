'''
https://exercise.acmcoder.com/online/online_judge_ques?ques_id=3862&konwledgeId=42
https://discuss.acmcoder.com/topic/58cd31e475bf559a0653f98f
'''
n = int(raw_input())
balls = raw_input().split()
balls = map(int, balls)
pros_list = [0]*n
pros_list[0] = 1
individual_add = [0]*n
individual_add[0] = 1

def check_prev(i, pros_list):
	count = 0
	sub_fix = [balls[i]]
	for i_ in range(i-1,-1,-1):
		if balls[i_] not in sub_fix:
			sub_fix.append(balls[i_])
			# print(sub_fix)
			count += (individual_add[i_])
			# print(i_, individual_add[i_])
		else:
			break
	return count

for i in range(1,n):
	pros_list[i] += (pros_list[i-1] + check_prev(i, pros_list))
	individual_add[i] = pros_list[i-1]
	# print(pros_list)
	# print(individual_add)

'''
input: 1 2 3 3 2
individual_add: 1 1 2 4 4
pros_list: 1 2 4 4 8
'''

print(pros_list[n-1]%1000000007)
