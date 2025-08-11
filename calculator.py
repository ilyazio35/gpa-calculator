# gpacalculator.py

GRADE_POINTS = {
    'A+': 4.0,
    'A': 4.0,
    'A-': 3.7,
    'B+': 3.3,
    'B': 3.0,
    'B-': 2.7,
    'C+': 2.3,
    'C': 2.0,
    'C-': 1.7,
    'D+': 1.3,
    'D': 1.0,
    'D-': 0.7,
    'F': 0.0,
}

def calculate_gpa(grades, credits):
    """
    grades: list of strings e.g. ['A', 'B+', 'C']
    credits: list of strings or numbers e.g. ['3', '4', '3']
    returns: GPA rounded to 2 decimals or error string
    """
    try:
        total_points = 0
        total_credits = 0
        for grade, credit in zip(grades, credits):
            grade = grade.upper()
            if grade not in GRADE_POINTS:
                return f"Invalid grade: {grade}"
            credit = float(credit)
            if credit < 0:
                return "Credit hours cannot be negative"
            total_points += GRADE_POINTS[grade] * credit
            total_credits += credit

        if total_credits == 0:
            return "Total credits cannot be zero"

        gpa = total_points / total_credits
        return round(gpa, 2)
    except Exception as e:
        return f"Error: {str(e)}"