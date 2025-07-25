# 1.Write a Python program to check if a number is positive, negative, or zero.
def check_number_positive_negative_zero(number: int) -> str:
    if number > 0:
        return f"Number is Positive"
    elif number < 0:
        return f"Number is negative"
    else:
        return f"Number is zero "


number = check_number_positive_negative_zero(0)
print(number)


# 2.Given a student’s score, write a program to print “Pass” if score ≥ 40, otherwise print “Fail”.
def print_student_result(score: int) -> str:

    # if score >= 40:
    #     return "Pass"
    # else:
    #     return "Fail"

    return "Pass" if score >= 40 else "Fail"


result = print_student_result(12)
print(result)


# 3.Write a program that checks if a given year is a leap year.
def check_leap_year(year: int) -> str:
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        return f"{year} is a Leap Year"
    return f"{year} is not a Leap Year"


year = check_leap_year(1900)  # check cases for 1900, 2000, 2024
print(year)


# 4.Given 3 integers, write a program to find the largest number using if-elif-else.
def find_largest_number(number1: int, number2: int, number3: int) -> str:
    if number1 > number2 and number1 > number3:
        return f"{number1} is > both {(number2)} and {(number3)}"
    elif number2 > number1 and number2 > number3:
        return f"{number2} is > both {(number1)} and {(number3)}"
    else:
        return f"{number3} is > both {(number1)} and {(number2)}"


largest_number = find_largest_number(67, 56, 1099809389809)
print(f"Largest Number: {largest_number}")

# 5.Evaluate if a candidate passes technical round using:
#      	coding_skill ≥ 4
#      	problem_solving ≥ 4
#      	cs_fundamentals ≥ 4
#       (Use and operator)


def check_candidate_skills(coding: int, problem: int, cs: int) -> bool:
    return coding >= 4 and problem >= 4 and cs >= 4


Candidate = check_candidate_skills(5, 6, 7)
print(Candidate)


# 6.Check if a candidate meets communication and CGPA criteria:
#    	CGPA ≥ 7.0
#    	communication ≥ 3
def check_candidate_criteria(cgpa: float, communication: int) -> bool:
    return cgpa >= 7 and communication >= 3


candidate = check_candidate_criteria(8.9, 2)
print(candidate)


# 7.Based on inputs, decide hiring decision using nested if:
#   	Check technical first, then CGPA & communication
def hiring_decision(
    coding_skill: int,
    problem_solving: int,
    cs_fundamentals: int,
    cgpa: float,
    communication: float,
) -> str:
    if check_candidate_skills(coding_skill, problem_solving, cs_fundamentals):
        if check_candidate_criteria(cgpa, communication):
            return "Candidate is hired!"
        else:
            return "Rejected: Did not meet CGPA/Communication criteria."
    else:
        return "Rejected: Did not pass the technical round."


hire_or_not = hiring_decision(9, 4, 7, 8.9, 1)
print(hire_or_not)


# 8.Write a program to check if a number is divisible by both 3 and 5 using and.
def number_is_divisible_by_3_5(number: int) -> str:
    if (number % 3 == 0) and (number % 5 == 0):
        return f"{number} is divisible by both 3 and 5"
    return f"{number} is not divisible by both 3 and 5"


print(number_is_divisible_by_3_5(15))


# 9.Given a list of candidates with CGPAs, print “Fast-Track” if CGPA > 9 or communication ≥ 4
def get_candidates_track(cgpa: float, communication: int) -> str:
    if (cgpa >= 9) or (communication >= 4):
        return "Fast-Track"


print(get_candidates_track(2, 5))


# 10.Write a program using not to check if a person is not eligible for a scholarship (i.e., CGPA < 6).
def person_is_eligible_for_scholarship(cgpa: int) -> str:
    if not (cgpa >= 6):
        return "person is not eligible for a scholarship"
    else:
        return "Person is eligible for scholarship"


print(person_is_eligible_for_scholarship(3))
