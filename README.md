# PawPal+ AI Pet Care Planner

## Overview
PawPal+ is an AI-assisted system that helps pet owners manage daily care tasks such as feeding, walking, grooming, and vet visits. It generates a schedule and evaluates how reliable that schedule is based on constraints and priorities.

## AI Feature: Reliability Self-Check
PawPal+ validates the generated pet care schedule by:
- Detecting time conflicts between tasks
- Checking whether high-priority tasks are included
- Assigning a reliability score
- Explaining the reasoning behind the score

This feature is integrated directly into the system and runs automatically after the schedule is generated.

## Architecture
The system consists of:
- Scheduler: manages and sorts tasks
- Conflict Detection: identifies overlapping tasks
- Validator: evaluates schedule reliability
- Explanation Generator: explains decisions and scoring

See system diagram in `/assets/system_diagram.png`.

## Setup Instructions
1. Clone the repository
2. Install dependencies:
   pip install -r requirements.txt
3. Run the program:
   python main.py

## Sample Output
Example output includes:
- Sorted task schedule
- Conflict detection results
- Reliability score
- Explanation of scheduling decisions

## Tests
- Conflict detection test
- Reliability score decreases when conflicts exist

## Design Decisions
The system prioritizes simplicity and clarity. A rule-based validator was used instead of a machine learning model to ensure transparency and easy debugging.

## Reflection
This project demonstrated how AI systems can go beyond generating outputs by evaluating their own results. Adding a reliability scoring system made the application more robust and aligned with real-world AI workflows.
