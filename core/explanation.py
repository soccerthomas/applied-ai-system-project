def explain_plan(tasks, conflicts, score, checks):
    explanation = "\nPawPal+ AI Self-Check:\n\n"

    explanation += f"Reliability Score: {score}%\n\n"

    explanation += "Scheduled Tasks:\n"
    for task in sorted(tasks, key=lambda t: t.time):
        explanation += (
            f"- {task.time.strftime('%m/%d %I:%M %p')} - "
            f"{task.title} for {task.pet.name} "
            f"(Priority: {task.priority})\n"
        )

    explanation += "\nConflict Review:\n"
    if conflicts:
        for conflict in conflicts:
            explanation += f"- {conflict}\n"
    else:
        explanation += "- No conflicts found.\n"

    explanation += "\nReasoning:\n"
    for check in checks:
        explanation += f"- {check}\n"

    return explanation