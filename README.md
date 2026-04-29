PawPal+ AI Pet Care Planner
Overview
PawPal+ is an AI-assisted system that helps pet owners manage daily care tasks such as feeding, walking, grooming, and vet visits. It generates a schedule and evaluates how reliable that schedule is based on constraints and priorities.
AI Feature: Reliability Self-Check
PawPal+ validates the generated pet care schedule by:


Detecting time conflicts between tasks


Checking whether high-priority tasks are included


Assigning a reliability score


Explaining the reasoning behind the score


This feature is integrated directly into the system and runs automatically after the schedule is generated.
Architecture
The system includes:


Scheduler (manages and sorts tasks)


Conflict Detection (identifies overlapping tasks)


Validator (evaluates schedule reliability)


Explanation Generator (explains decisions and scoring)


See system diagram in /assets/system_diagram.png.
Setup Instructions


Clone the repository


Install dependencies:
pip install -r requirements.txt


Run the program:
python main.py


Sample Output
The program outputs:


Sorted task schedule


Conflict detection results


Reliability score


Explanation of scheduling decisions


Tests


Conflict detection test


Reliability score decreases when conflicts exist


Design Decisions
The system uses a rule-based validator instead of a machine learning model to ensure transparency and easy debugging.
Reflection
This project demonstrates how an AI system can evaluate its own output. Adding a reliability scoring system makes the planner more robust and aligned with real-world AI workflows.
