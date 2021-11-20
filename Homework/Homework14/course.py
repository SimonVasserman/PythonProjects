class Course:
    def __init__(self, name, description, students, teacher, star_date, end_date, quantity_lesson):
        self.name = name
        self.description = description
        self.students = []
        self.teacher = []
        self.start_date = star_date
        self.end_date = end_date
        self.quantity_lesson = quantity_lesson

    def __repr__(self):
            return f"{self.name} | {self.}"