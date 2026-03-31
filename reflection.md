# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

- Briefly describe your initial UML design.
My initial UML design had classes such as Pet, Task, Scheduler, and User. The Pet class was responsible for storing information about each pet like name, type, and age. The Task class handled activities such as walks, feeding, or vet visits. The Scheduler class was responsible for organizing tasks and making sure they were assigned at appropriate times. The User class represented the person using the app and connected all the pets and tasks together.
- What classes did you include, and what responsibilities did you assign to each?
Yes, my design changed during implementation. At first, I had the Scheduler directly manage all task details, but I realized it was better to let the Task class handle more of its own data. This made the code more organized and easier to manage. I made this change to improve clarity and keep responsibilities separated.
  

**b. Design changes**

- Did your design change during implementation?
Yes, my design changed during implementation. This made the code more organized and easier to manage. I made this change to improve clarity and keep responsibilities separated
- If yes, describe at least one change and why you made it.
At first, I had the Scheduler directly manage all task details, but I realized it was better to let the Task class handle more of its own data.
---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?
The scheduler looks at a few main things: the time a task is supposed to happen, the priority of the task, which pet it is for, and whether it repeats. I decided that time and priority were the most important because things like feeding or medication need to happen on schedule. Other tasks, like walks or playtime, are less strict, so they can be moved around if needed.
**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?
One tradeoff the scheduler makes is that it always puts higher-priority tasks before lower-priority tasks, even if the lower-priority tasks were scheduled earlier. This makes sense because it makes sure the most important pet care things get done on time, even if some other tasks are delayed.
---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?
I used AI to help come up with the class structure, write the basic code for tasks, pets, and the scheduler, and suggest ways to sort tasks, filter them, handle recurring tasks, and detect conflicts. The prompts that worked best were ones that asked for very specific code or logic, like how to sort a list of tasks by time or how to check if two tasks happen at the same time.
**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?
There was a time when AI suggested a very complicated way to check for conflicts between tasks. I didn’t use it because it was too messy and slow. I looked at the logic and realized I could do the same thing with a simpler approach. Then I tested it by creating tasks that happened at the same time and checked that the warning message appeared correctly.
---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?
I tested that tasks could be sorted by time, filtered by pet and whether they were complete, that daily tasks would automatically create the next day’s task when marked complete, and that the scheduler could detect conflicts. These tests were important to make sure the app actually planned pet care correctly and didn’t miss or double-book tasks.

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?
I am pretty confident that the scheduler works for normal situations. If I had more time, I would test edge cases like tasks that happen at midnight, overlapping multi-day tasks, tasks with zero duration, and multiple recurring tasks at the same time for the same pet.

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?
I am happy with how the scheduler handles recurring tasks and conflict warnings. It makes the system feel like it could really help a pet owner plan their day.
**b. What you would improve**

- If you had another iteration, what would you improve or redesign?
If I had another chance, I would make the scheduler smarter about more complicated situations, like pets’ preferences or tasks that happen in different locations. I would also make the app interface talk directly to the backend so adding and editing tasks updates everything immediately.
**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
The main thing I learned is that AI can be really helpful for writing code and coming up with ideas, but you still need to think carefully and test everything yourself to make sure it works and makes sense.
