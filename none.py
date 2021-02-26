

# 사각형 면적 구하기
def solution1(hegith, weight):
    return hegith*weight

hegith,weight = map(int,input().split())
print(solution1(hegith,weight))


subject_socre_list = [90, 30, 20, 50, 3, 30, 50]

# 점수 평균 구하기
def solution2(*subject_scores):
    total = 0
    for i in subject_scores:
        total += i
    return total/len(subject_scores)
        

print(solution2(*subject_socre_list))



subject_score_list_by_season = {
    '1학기': {
        '영어': 90,
        '국어': 40,
        '수학': 3,
    },
    '2학기': {
        '영어': 40,
        '국어': 20,
        '수학': 10,
    },
}
# subject_score_list_by_season['1학기']['국어']

# 과목별 점수 평균 (1, 2학기 합쳑서) 구하기
def solution3(**subject_scores):
    ttotal = 0
    a = 0
    b = 0
    c = 0
    for i in subject_scores.keys():
        
        for j in subject_scores[i]:
            if j == '국어':
                a += subject_scores[i][j]
            
            elif j == '영어':
                b += subject_scores[i][j]

            elif j == '수학':
                c += subject_scores[i][j]
                
    return {'국어': a/2,'영어':b/2,'수학':c/2}
        

print(solution3(**subject_score_list_by_season))

# {'국어': 100, '영어': 100, '수학': 100}


subject_score_list_by_season = {
    '1학기': {
        '영어': 90,
        '국어': 40,
        '수학': 3,
    },
    '2학기': {
        '영어': 40,
        '국어': 20,
        '수학': 10,
    },
}

# 과목별 점수 평균 (1, 2학기 합쳑서) 구하기
def solution4(**subject_scores):
    score_average_data = {}

    for subject_score_data in subject_scores.values():
        for subject, score in zip(subject_score_data.keys(), subject_score_data.values()):
            if score_average_data.get(subject):
                score_average_data[subject] += score
            else:
                score_average_data[subject] = score
    
    print(score_average_data)

    return list(map(lambda x: x/len(subject_scores), score_average_data.values()))
            
    
    

    # for i in subject_scores.keys():
        
    #     for j in subject_scores[i]:
    #         if j == '국어':
    #             a += subject_scores[i][j]
            
    #         elif j == '영어':
    #             b += subject_scores[i][j]

    #         elif j == '수학':
    #             c += subject_scores[i][j]
                
    # return {'국어': a/2,'영어':b/2,'수학':c/2}

print(solution4(**subject_score_list_by_season))