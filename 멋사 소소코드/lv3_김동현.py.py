import random
def answer_num(): # 3개의 랜덤 숫자를 정해주는 함수
    num1 = [1,2,3,4,5,6,7,8,9]
    answer = random.sample(num1,3)
    return answer


def guess_num(): # 3개의 추측된 숫자를 받아주는 함수
    guess = [] 
    while(1):
        three_num = input('0부터 9 사이의 서로 다른 3개의 숫자를 고르시오:')
        guess = three_num.split()
        error_count = 0
        for item in guess: # 3개의 서로 다른 숫자를 받기 위해 조건을 만듭니다.
            if int(item) < 0 or int(item) > 9: # 첫번째 조건
                error_count += 1
            elif guess.count(item) >= 2: # 두번째 조건
                error_count += 1
        if error_count == 0:
            break
    return guess
           
        
    
def score_num(guess, answer): # 점수를 매기는 함수
    strike = 0
    ball = 0
    i = 0
    while i < len(guess):
        if int(guess[i]) == int(answer[i]): # 스트라이크 조건
            strike += 1
            i += 1
        elif int(guess[i]) in answer: # 볼 조건
            ball += 1
            i += 1
        else:
            i += 1
    return strike, ball

game_answer = answer_num()

while(1): # 조건을 만족시킬때 게임을 종료시킵니다.
    game_guess = guess_num()
    s, b = score_num(game_guess, game_answer)
    print('{}S{}B입니다.'.format(s,b))
    if s == 3:
        print('3S입니다. 프로그램을 종료합니다.')
        break





    
    
