# PawPal+ Model Card

## Overview
PawPal+ is an AI-assisted pet care planner that generates daily schedules and evaluates their reliability using a self-check system.

## AI Feature
The system includes a reliability and validation component that:
- Detects scheduling conflicts
- Evaluates inclusion of high-priority tasks
- Assigns a reliability score
- Explains reasoning behind decisions

## Limitations
- Does not account for travel time between tasks
- Assumes all tasks have equal effort beyond priority
- Conflict detection only checks exact time overlap

## Biases
- Prioritization is based solely on numeric priority
- User-defined priorities may not reflect real-world urgency

## Testing
The system was tested using:
- Conflict detection tests
- Reliability scoring validation tests

Results:
- System correctly identifies conflicts
- Reliability score decreases when conflicts are present
