def solution(log):
    total_study_time = 0 # 총 공부시간을 저장하는 변수입니다. 
    
    for i in range(0, len(log), 2): # 2개씩 쌍으로 읽어서 두 시각의 차이를 구합니다.
        
        # "00:00"형식을 분 단위로 숫자 형식으로 바꿉니다.
        start_time = int(log[i][0:2]) * 60 + int(log[i][3:5])
        end_time = int(log[i+1][0:2]) * 60 + int(log[i+1][3:5])
        study_time = end_time - start_time
        
        # 공부 시간에 대한 2가지 조건을 적용하여 공부 시간을 구합니다.
        if study_time < 5:
            study_time = 0
        elif study_time > 105:
            study_time = 105
        
        # total_study_time에 더합니다.
        total_study_time += study_time
        
    # total_study_time을 이제 다시 "00:00" 형식으로 바꿉니다
    total_hour = total_study_time // 60
    total_min = total_study_time % 60
    
    total_study_time_str = str(total_hour).zfill(2)+':'+str(total_min).zfill(2) # 문자열 함수를 사용하여 "00:00" 형식을 맞춥니다. 

    return total_study_time_str 
############################## 입력 data ###############################
# case 1
# log = ["08:30", "09:00", "14:00", "16:00", "16:01", "16:06", "16:07", "16:11"]

# case 2
log = ["01:00", "08:00", "15:00", "15:04", "23:00", "23:59"]

print(solution(log))