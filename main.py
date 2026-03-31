from datetime import datetime
from pawpal_system import Pet, Task, User

# Create user
owner = User("Alex")

# Create pets
pet1 = Pet("Buddy", "Dog", 3)
pet2 = Pet("Whiskers", "Cat", 2)

# Add pets
owner.add_pet(pet1)
owner.add_pet(pet2)

# Create tasks
task1 = Task("Morning Walk", pet1, datetime.now().replace(hour=9, minute=0), 1)
task2 = Task("Feed Cat", pet2, datetime.now().replace(hour=8, minute=30), 2)
task3 = Task("Vet Appointment", pet1, datetime.now().replace(hour=14, minute=0), 1)

# Add tasks
owner.add_task(task1)
owner.add_task(task2)
owner.add_task(task3)

# Get today's tasks
tasks_today = owner.view_tasks(datetime.now())

# Sort tasks by time
tasks_today.sort(key=lambda t: t.time)

# Print schedule
print("Today's Schedule:\n")

for task in tasks_today:
    time_str = task.time.strftime("%I:%M %p")
    print(f"{time_str} - {task.title} for {task.pet.name} (Priority {task.priority})")
