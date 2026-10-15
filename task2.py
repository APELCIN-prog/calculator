def check_winners(scores, student_score):
    scores.sort(reverse=True)
    if student_score in scores[:3]:
        print('Вы в тройке победителей!')
    else:
        print('Вы не попали в тройку победителей')


test_list = [20, 48, 52, 38, 36, 13, 7, 41, 34, 24, 5, 51, 9, 14, 28]
stas_estimation = int(input())
check_winners(test_list, stas_estimation)
