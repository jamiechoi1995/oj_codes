'''
https://exercise.acmcoder.com/online/online_judge_ques?ques_id=3863&konwledgeId=42
https://discuss.acmcoder.com/topic/58cd31e475bf559a0653f98f
'''

def process(input_line):
    # dp = [[-1]*len(input_line)]*len(input_line) # wrong, low copy !! modification in one row will change other rows
    dp = [[-1 for i in range(len(input_line))] for j in range(len(input_line))]

    # init table
    for index, item in enumerate(input_line):
        dp[index][index] = item

    y_end = len(input_line)-1
    for shift in range(len(input_line)-1):
        for y in range(y_end):
            x = y+1+shift
            dp[y][x] = sum(input_line[y:x+1]) - min(dp[y+1][x], dp[y][x-1])
        y_end -= 1
    return dp[0][-1]

n = int(raw_input())
for i in range(n):
	l = int(raw_input())
	input_line = raw_input().split()
	input_line = map(int, input_line)
	first = process(input_line)
	print('Case #%d: %d %d' % (i+1, first, sum(input_line)-first))
