import random

class ClassSeatingArrangement:
    def __init__(self, rows, seats_per_row):
        self.rows = rows
        self.seats_per_row = seats_per_row
        self.arrangement = self.generate_empty_arrangement()

    def generate_empty_arrangement(self):
        return [['Empty' for _ in range(self.seats_per_row)] for _ in range(self.rows)]

    def assign_student(self, row, seat, student_name):
        if 0 <= row < self.rows and 0 <= seat < self.seats_per_row:
            if self.arrangement[row][seat] == 'Empty':
                self.arrangement[row][seat] = student_name
                return True
            else:
                print(f"Seat {row}-{seat} is already occupied.")
        else:
            print("Invalid row or seat number.")

    def display_arrangement(self):
        for row in range(self.rows):
            for seat in range(self.seats_per_row):
                print(f"Row {row + 1} - Seat {seat + 1}: {self.arrangement[row][seat]}")
            print()

if __name__ == "__main__":
    rows = 5
    seats_per_row = 6
    classroom = ClassSeatingArrangement(rows, seats_per_row)

    # Simulate assigning students randomly
    students = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Hank", "Ivy"]
    random.shuffle(students)

    for row in range(rows):
        for seat in range(seats_per_row):
            student = students.pop() if students else "Empty"
            classroom.assign_student(row, seat, student)

    # Display the seating arrangement
    classroom.display_arrangement()
