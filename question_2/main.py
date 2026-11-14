"""
Okay, i understood that we need to design a orchestrator, which actually monitor that whcih task is done
whcih is high priority task or either that task is dependent on other task or not,
and then we need to schedule the task based on that.
So i have in mind that we first need to look into the all the workers,
and then we need to check that which task is dependent on other task,
so, in this case, task 1 and 2 is not dependent on any other task
so we will start working on it, now t will be 0
so at that time, our workers array have the 0,0
it means that both workers are free, so we will assign task 1 to worker 0 and task 2 to worker 1
so after assigning, we will update the workers array as well, so now first 0 of workers will become 3,
but other worker is also 0, so instead of updating the t, we will assign next task to next worker,
the schudule list of tuple needs three thing, first is task id, second is start time and third is worker id, so for worker id, we can take index of the work, and we will take minimum of worker array, so this way, we identify that whcih worker is free
and which is not, we need some check here

i was stuck on the part like how workers updated properly, plus later on i thought that i should use while loop,
instead of for loop, as for loop works on the sequintal, and while loop, we can only run a task whcih is free,
and while loop will break, when all the tasks are done,

task was to not use AI, so i didn't,
so i struggled alot and spent so much time,
so i could not done it in time, then i shifted to next SQL question.
So, let's hope for the best.
"""


def schedule_tasks(W, tasks):
    t = 0
    makespan = 0
    workers = [0] * W
    schedule = list()

    for task_id, duration, priority, dependencies in tasks:

        if all(dep in [t[0] for t in schedule] for dep in dependencies):
            start_time = t
            end_time = start_time + duration
            schedule.append((task_id, start_time, workers.index(min(workers))))
            t = end_time
            workers[schedule[-1][2]] += duration
            makespan = max(makespan, end_time)

    return makespan, schedule


if __name__ == "__main__":
    W = 2
    tasks = [
        (1, 3, 5, []),
        (2, 2, 1, []),
        (3, 4, 9, [1]),
        (4, 1, 1, [1, 2]),
    ]
    print(schedule_tasks(W, tasks))
