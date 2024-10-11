# Creating a stack for task management
task_stack = []

# Adding (pushing) tasks to the stack
task_stack.append("Pack Item A")
task_stack.append("Pack Item B")
task_stack.append("Pack Item C")

# Displaying current tasks in the stack
print("Current tasks in the stack:", task_stack)

# Completing (popping) the last task
print("Task to perform:", task_stack.pop())  # Outputs: Pack Item C
print("Remaining tasks in the stack:", task_stack)

# Adding a new task
task_stack.append("Pack Item D")
print("Updated tasks in the stack:", task_stack)
