def validate_plan(tasks, conflicts):
    score = 100
    checks = []

    if conflicts:
        score -= 25
        checks.append("Conflicts were detected in the schedule.")
    else:
        checks.append("No time conflicts were found.")

    high_priority_tasks = [t for t in tasks if t.priority >= 8]

    if high_priority_tasks:
        checks.append("High-priority tasks were included in the plan.")
    else:
        score -= 10
        checks.append("No high-priority tasks were found.")

    if len(tasks) == 0:
        score = 0
        checks.append("No tasks were scheduled.")

    score = max(score, 0)
    return score, checks