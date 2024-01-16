'''
Fabian Campos 
CSC 110
Programming Project 2
This program determines students' final grades.
'''

def letter_grade(grade):

    '''
    This function returns the letter grade corresponding 
    to the student's grade.
    Args:
        grade: student's grade
    Returns:
        Letter grade
    '''

    # grade thresholds

    if grade <= 100 and grade >= 90:
        return "A"
    elif grade < 90 and grade >= 80:
        return "B"
    elif grade < 80 and grade >= 70:
        return "C"
    elif grade < 70 and grade >= 60:
        return "D"
    elif grade < 60 and grade >= 0:
        return "E"
    elif grade < 0 or grade > 100: 
        return "X"
    else:
        return "Error"

def pass_or_fail(grade):

    '''
    This function determines whether the student passes or fails 
    according to their grade.
    Args:
        grade: student's grade
    Returns:
        Declares whether student passes or fails, or returns error
    '''

    # grade thresholds

    if grade == "A":
        return "Pass"
    elif grade == "B":
        return "Pass"
    elif grade == "C": 
        return "Pass"
    elif grade == "D":
        return "Pass"
    elif grade == "E": 
        return "Fail"
    else: 
        return "Error"
    
def point_grade(score, total_points):
    
    '''
    This function gets the students point grade. 
    Args: 
        score: student's score on test
        total_points: total points of test
    Returns:
        Student's point grade
    '''

    return round((score / total_points) * 100, 2)

def get_grade_results(score, total_points): 

    '''
    This function declares the student's final grade standing. 
    Args: 
        score: student's score on test
        total_points: total points of test
    Returns: 
        student's final grade standings
    '''

    calculation = (
    "Your grade is " + str(point_grade(score, total_points)) + " (" + 
    str(letter_grade(point_grade(score, total_points))) + 
    " - " + 
    str(pass_or_fail(letter_grade(point_grade(score, total_points)))) + ")"
    )

    return calculation




















    






    
