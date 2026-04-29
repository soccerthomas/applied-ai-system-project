import sys
import os
from datetime import datetime

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from pawpal_system import Pet, Task, Scheduler
from core.validator import validate_plan

def test_conflict_detection():
    scheduler = Scheduler()
    pet = Pet("Buddy", "Dog", 3)

    t1 = Task("Walk", pet, datetime(2026, 4, 29, 9, 0), 7)
    t2 = Task("Grooming", pet, datetime(2026, 4, 29, 9, 0), 4)

    scheduler.add_task(t1)
    scheduler.add_task(t2)

    conflicts = scheduler.detect_conflicts()

    assert len(conflicts) == 1

def test_reliability_score_drops_when_conflict_exists():
    scheduler = Scheduler()
    pet = Pet("Buddy", "Dog", 3)

    t1 = Task("Walk", pet, datetime(2026, 4, 29, 9, 0), 7)
    t2 = Task("Grooming", pet, datetime(2026, 4, 29, 9, 0), 4)

    scheduler.add_task(t1)
    scheduler.add_task(t2)

    conflicts = scheduler.detect_conflicts()
    score, checks = validate_plan(scheduler.tasks, conflicts)

    assert score < 100
