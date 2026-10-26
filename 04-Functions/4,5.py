def points_to_grade(points):
    grade = ''
    if points >= 18:
        grade = 'excellent'

    if points >= 14:
        grade = 'good'

    if points >= 10:
        grade = 'satisfactory'

    else:
        grade = 'failed'
    


        return grade


    test_result = 15
    final_grade = points_to_grade(test_result)
    print('u scored  points on the test. your final grade is')