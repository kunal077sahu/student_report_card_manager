#==========================================
#     📖REPORT CARD MANAGER
#==========================================

students = {
    "kunal" : 100,
    "meow" : 23,
    "faa" : 67
}

#titel
def titel(titel_name):
    print("="*60)
    print(titel_name.center(60))
    print("="*60,"\n","\n")

#show all student
def show_all_students():
    print(students.keys())

#add students
def add_students():
    name = input("enter student's name: ")
    marks = int(input("enter student's marks: "))
    students[name] = marks
    print(f"{name} was added.....✔")

#average marks
def average():
    marks = []
    marks_in_students = students.values()
    marks.append(marks_in_students)
    print(f"average marks: {sum(marks_in_students)/len(marks)}")

#topper of class
def toppers():
    topper = max(students,key=students.get)
    print(f"🏆topper of the class: {topper}")

#save to file
def save_to_file():
    with open("report.txt","w") as f :
        f.write(f"topper of class is {toppers}\n")
        f.write(f"average marks is {sum(students.values())/len(students.values())}")
    print("🏆topper of class and average marks is add to the file.")

#read file
def read_file():
    with open("report.txt","r") as f :
        text = f.read()
        print(text)

print(titel("REPORT CARD MANAGER"))

while True:
    print("______MENU______")
    print("1. show all students name         5.save to file")
    print("2. add students                   6.load/read file")
    print("3. average marks                  7.exit")
    print("4. topper of class\n")

    

    choice = int(input("enter your choice: "))

    if choice == 1 :
        show_all_students()
    elif choice == 2 :
        add_students()
    elif choice == 3 :
        average()
    elif choice == 4 :
        toppers()
    elif choice == 5 :
        save_to_file()
    elif choice == 6 :
        read_file()
    elif choice == 7 :
        print("Thamk you for using our program......good bye")
        break
    else:
        print("invalid choice")
        
    
