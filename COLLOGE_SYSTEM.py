class Program:
    def _init_(self, name, intake):
        self.name = name
        self.intake = intake

    def _str_(self):
        return f"{self.name} (Intake: {self.intake})"


class Faculty:
    def _init_(self, name):
        self.name = name

    def _str_(self):
        return f"{self.name}"


class Hostel:
    def _init_(self, name, gender, year):
        self.name = name
        self.gender = gender
        self.year = year

    def _str_(self):
        return f"{self.name} Hostel ({self.gender}, {self.year})"


class GateQualified:
    def _init_(self, name, rank):
        self.name = name
        self.rank = rank

    def _str_(self):
        return f"{self.name} (Rank: {self.rank})"


class Placement:
    def _init_(self, company, count):
        self.company = company
        self.count = count

    def _str_(self):
        return f"{self.company} ({self.count} students)"


class College:
    def _init_(self, name):
        self.name = name
        self.programs = []
        self.faculty = []
        self.hostels = []
        self.gate_qualified = []
        self.startups = []
        self.placements = []

    def add_program(self, program):
        self.programs.append(program)

    def add_faculty(self, faculty):
        self.faculty.append(faculty)

    def add_hostel(self, hostel):
        self.hostels.append(hostel)

    def add_gate_student(self, student):
        self.gate_qualified.append(student)

    def add_startup(self, name):
        self.startups.append(name)

    def add_placement(self, placement):
        self.placements.append(placement)

    def show_summary(self):
        print(f"\n--- {self.name} ---")
        print("\nAcademic Programs:")
        for p in self.programs:
            print(f" - {p}")

        print("\nFaculty Members:")
        for f in self.faculty:
            print(f" - {f}")

        print("\nHostels:")
        for h in self.hostels:
            print(f" - {h}")

        print("\nGATE Qualified Students:")
        for g in self.gate_qualified:
            print(f" - {g}")

        print("\nStartups by Students:")
        for s in self.startups:
            print(f" - {s}")

        print("\nPlacements:")
        for p in self.placements:
            print(f" - {p}")


# ========== Initialize College System ==========

college = College("Institute of Engineering and Technology, Lucknow")

# Add academic programs
program_list = [
    "BTech CSE (SF)", "BTech CSE (AI)", "BTech CSE (R)",
    "BTech ECE", "BTech Mechanical Engineering",
    "BTech Civil Engineering", "BTech Chemical Engineering",
    "MBA", "MCA", "PhD", "M.Tech"
]
for name in program_list:
    college.add_program(Program(name, 75))

# Add faculty members
faculty_list = [
    "Dr. Arpit Katiyar", "Dr. Aditi Singh", "Dr. Ayan Verma", "Dr. Pankaj Joshi",
    "Dr. Manoj Singh", "Dr. Shivam Chauhan", "Dr. Sushant Pandey", "Dr. Kartik Nair",
    "Dr. Rahul Gupta", "Dr. Aisha Khan"
]
for name in faculty_list:
    college.add_faculty(Faculty(name))

# Add hostels
boys_hostels = [
    ("Ramanujan", "1st Year"),
    ("Aryabhatt", "2nd Year"),
    ("Visheswaraya A", "3rd Year"),
    ("Visheswaraya B", "3rd Year"),
    ("Visheswaraya C", "3rd Year"),
    ("KN", "3rd Year")
]
girls_hostels = [
    ("Gargi", "1st Year"),
    ("Maitreyi", "2nd Year"),
    ("Apala", "3rd Year"),
    ("Anusuya", "4th Year")
]
for name, year in boys_hostels:
    college.add_hostel(Hostel(name, "Boys", year))
for name, year in girls_hostels:
    college.add_hostel(Hostel(name, "Girls", year))

# Add GATE qualified students
gate_students = [
    ("Abhishek Shrivastav", 27),
    ("Ayush", 736), ("Mangesh", 907), ("Vishal", 271),
    ("Anaya", 569), ("Nidhi", 356), ("Shristi", 620),
    ("Manan", 589), ("Sakshi", 169), ("Ark", 960),
    ("Astha", 965), ("Kartikey", 706), ("Khushi", 129),
    ("Aryan", 155), ("Samar", 772), ("Ritika", 574)
]
for name, rank in gate_students:
    college.add_gate_student(GateQualified(name, rank))

# Add startups
for s in ["Varks", "Sath Phere", "While"]:
    college.add_startup(s)

# Add placements
placement_data = {
    "Atlassian": 5, "Adobe": 12, "Google": 3,
    "Microsoft": 3, "Amazon": 2
}
for company, count in placement_data.items():
    college.add_placement(Placement(company, count))

# Show all info
college.show_summary()