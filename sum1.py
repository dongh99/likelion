import random
def answer_num():
    num1 = [1,2,3,4,5,6,7,8,9]
    answer = [1,3,5]
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
        if int(guess1[j]) == int(answer[j]):
            strike += 1
            j += 1
        elif int(guess1[j]) in answer:
            ball += 1
            j += 1
        else:
            j += 1
    return strike, ball


ANSWER = answer_num()

while 1:
    GUESS = guess_num()
    s, b = score_num(GUESS, ANSWER)
    print('{}S {}B'.format(s,b))

    if s == 3:
        break
        
        






    
    




