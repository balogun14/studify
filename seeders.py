from database import Database
from datetime import datetime, timedelta


db = Database()

#     db.add_course("Mathematics", "Monday", "09:00", "Room 101")
def addClassesRange():
    classes = [
        {"day": "Monday", "courses": [
            {"name": "PCG 211", "start_time": "08:00", "end_time": "09:00", "room": "Online"},
            {"name": "PHG lab", "start_time": "09:00", "end_time": "12:00", "room": "Physiology lab"},
            {"name": "PHG 231", "start_time": "12:00", "end_time": "13:00", "room": "Research hall"},
            {"name": "PCG 212/PCT 212", "start_time": "14:00", "end_time": "17:00", "room": "PCG lab/PCT lab"}
        ]},
        {"day": "Tuesday", "courses": [
            {"name": "PCH 211", "start_time": "08:00", "end_time": "10:00", "room": "Online"},
            {"name": "PCT 212/PCG 212", "start_time": "10:00", "end_time": "13:00", "room": "PCT lab/PCG lab"},
            {"name": "PCT 211", "start_time": "14:00", "end_time": "15:00", "room": "LT II"},
            {"name": "PCG TUT", "start_time": "15:00", "end_time": "16:00", "room": "Online"}
        ]},
        {"day": "Wednesday", "courses": [
            {"name": "ANA 231", "start_time": "08:00", "end_time": "10:00", "room": "Online"},
            {"name": "PCH 212/PCT 212/PCG 212", "start_time": "10:00", "end_time": "13:00", "room": "PCH lab/PCT lab/PCG lab"},
            {"name": "PCT 213", "start_time": "14:00", "end_time": "16:00", "room": "LT II"}
        ]},
        {"day": "Thursday", "courses": [
            {"name": "PCT 213", "start_time": "12:00", "end_time": "13:00", "room": "LT II"},
            {"name": "PCT 211", "start_time": "14:00", "end_time": "15:00", "room": "LT II"}
        ]},
        {"day": "Friday", "courses": [
            {"name": "PCT 213", "start_time": "08:00", "end_time": "10:00", "room": "Online"},
            {"name": "PCG 211", "start_time": "10:00", "end_time": "12:00", "room": "Online"},
            {"name": "PCH 211", "start_time": "12:00", "end_time": "13:00", "room": "Online"},
            {"name": "PHG 232", "start_time": "15:00", "end_time": "17:00", "room": "Online"}
        ]}
    ]

    for day in classes:
        for course in day["courses"]:
            db.add_course(course["name"], day["day"], course["start_time"], course["end_time"], course["room"])
            print(f"Added course: {course['name']} ({day['day']} {course['start_time']}-{course['end_time']})")
    print("Courses added successfully")



def addBooks():
    # Start date for the study plan (set to Monday of next week)
    today = datetime.now()
    days_ahead = 7 - today.weekday()  # Calculate days until next Monday
    start_date = today + timedelta(days=days_ahead)

    # Create the books list with proper due dates
    books = []

    # Month 1 (first 4 weeks)
    month1_date = start_date
    books.extend([
        {"title": "Atomic structure, Periodic table", "author": "PCH", "course_id": 1, "due_date": (month1_date + timedelta(days=0)).strftime('%Y-%m-%d')},
        {"title": "Definition and terms, Prescriptions", "author": "PCT", "course_id": 2, "due_date": (month1_date + timedelta(days=0)).strftime('%Y-%m-%d')},
        {"title": "General Physiology", "author": "PHG", "course_id": 3, "due_date": (month1_date + timedelta(days=1)).strftime('%Y-%m-%d')},
        {"title": "Historical development, Classification", "author": "MCB", "course_id": 4, "due_date": (month1_date + timedelta(days=1)).strftime('%Y-%m-%d')},
        {"title": "Intro to Pharmacognosy, Plant morphology", "author": "PCG", "course_id": 5, "due_date": (month1_date + timedelta(days=2)).strftime('%Y-%m-%d')},
        {"title": "Introduction to Anatomy, Cell Anatomy", "author": "ANA", "course_id": 6, "due_date": (month1_date + timedelta(days=2)).strftime('%Y-%m-%d')},
        {"title": "Review Monday's topics, Solutions", "author": "PCH", "course_id": 1, "due_date": (month1_date + timedelta(days=3)).strftime('%Y-%m-%d')},
        {"title": "Dosage forms, Weights & Measures", "author": "PCT", "course_id": 2, "due_date": (month1_date + timedelta(days=3)).strftime('%Y-%m-%d')},
    ])

    # Month 2 (next 4 weeks)
    month2_date = start_date + timedelta(weeks=4)
    books.extend([
        {"title": "Analytical methods, concepts of purity", "author": "PCH", "course_id": 1, "due_date": (month2_date + timedelta(days=0)).strftime('%Y-%m-%d')},
        {"title": "Isotonicity, Concentration expressions, Math", "author": "PCT", "course_id": 2, "due_date": (month2_date + timedelta(days=0)).strftime('%Y-%m-%d')},
        {"title": "Cardiovascular System", "author": "PHG", "course_id": 3, "due_date": (month2_date + timedelta(days=1)).strftime('%Y-%m-%d')},
        {"title": "Bacterial growth and nutrition, Reproduction in Bacteria", "author": "MCB", "course_id": 4, "due_date": (month2_date + timedelta(days=1)).strftime('%Y-%m-%d')},
        {"title": "Plant sources, Basic microscopic techniques", "author": "PCG", "course_id": 5, "due_date": (month2_date + timedelta(days=2)).strftime('%Y-%m-%d')},
        {"title": "Integumentary, Nervous systems", "author": "ANA", "course_id": 6, "due_date": (month2_date + timedelta(days=2)).strftime('%Y-%m-%d')},
    ])

    # Month 3 (final 4 weeks)
    month3_date = start_date + timedelta(weeks=8)
    books.extend([
        {"title": "Transition elements and coordination chemistry", "author": "PCH", "course_id": 1, "due_date": (month3_date + timedelta(days=0)).strftime('%Y-%m-%d')},
        {"title": "Past questions on dispensing", "author": "PCT", "course_id": 2, "due_date": (month3_date + timedelta(days=0)).strftime('%Y-%m-%d')},
        {"title": "Past questions review", "author": "PHG", "course_id": 3, "due_date": (month3_date + timedelta(days=1)).strftime('%Y-%m-%d')},
        {"title": "Viruses, Fungi", "author": "MCB", "course_id": 4, "due_date": (month3_date + timedelta(days=1)).strftime('%Y-%m-%d')},
        {"title": "Application of Pharmacognostic procedures", "author": "PCG", "course_id": 5, "due_date": (month3_date + timedelta(days=2)).strftime('%Y-%m-%d')},
        {"title": "Digestive, Urinary, Endocrine system", "author": "ANA", "course_id": 6, "due_date": (month3_date + timedelta(days=2)).strftime('%Y-%m-%d')},
        {"title": "Mock Exam: Complete past exam papers under timed conditions", "author": "Various", "course_id": 7, "due_date": (month3_date + timedelta(days=5)).strftime('%Y-%m-%d')}
    ])

    for book in books:
        db.add_book(book["title"], book["author"], book["course_id"], book["due_date"])
        print(f"Added book: {book['title']} ({book['due_date']})")

    print("Books added successfully")

