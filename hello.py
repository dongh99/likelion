import random
def answer_num():
    num1 = [1,2,3,4,5,6,7,8,9]
    answer = random.sample(num1,3)
    return answer


def guess_num():
    guess = []
    while(1):
        a = input('0부터 9 사이의 서로 다른 3개의 숫자를 고르시오:')
        guess = a.split()
        error_count = 0
        for item in guess:
            if int(item) < 0 or int(item) > 9:
                error_count += 1
            elif guess.count(item) >= 2:
                error_count += 1
        if error_count == 0:
            break
    return guess
           
        
    
def score_num(guess1, answer):
    strike = 0
    ball = 0
    j = 0
    while j < len(guess1):
        if guess1[j] == answer[j]:
            strike += 1
            j += 1
        elif guess1[j] in answer:
            ball += 1
            j += 1
        else:
            j += 1
    return strike, ball


ANSWER = answer_num()
tries = 0

while 1:
    GUESS = guess_num()
    s, b = score_num(GUESS, ANSWER)
    print('{}S {}B'.format(s,b))

    if s == 3:
        tries += 1
        break
    else:
        tries += 1

print("축하합니다. {}번 만에 숫자 3개의 값과 위치를 모두 맞추셨습니다.".format(tries))





    
    
