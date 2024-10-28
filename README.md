# Keysight_AI-ML-intern_EDA_domain
The repository contains the solution to Keysight Design question for AI/ML intern position for EDA Domain

Submitted by: Shreyas Gupta

## Problem Statement : 
Build a simple command-line interface (CLI) tool for managing tasks. The tool should allow users to add, view, complete, and delete tasks. Tasks should be stored in a text file (e.g., tasks.txt) so that they persist between sessions.


### Proposed Solution 1:
Developed a Python script which can allow user to perform different operations using command line interace(CLI). All the task operations are stored in text file which can be accessed even from a different session. The various possilbe operations inclued: add, view, complete, and delete tasks.

### CLI Outputs for Solution 1:

adding new task 1:

![Agent Playing](assets/add_task_1.png)


adding new task 2:

![Agent Playing](assets/add_task_2.png)


view task list:

![Agent Playing](assets/view_task.png)


mark task 2 as done:

![Agent Playing](assets/mark_done_2.png)


view updated task list:

![Agent Playing](assets/view_updated_task.png)


adding new task 3:

![Agent Playing](assets/add_task_3.png)


view updated task list:

![Agent Playing](assets/view_updated_task_1.png)


delete task 1:

![Agent Playing](assets/del_task_1.png)


view updated task list:

![Agent Playing](assets/view_updated_task_2.png)


exit task manager:

![Agent Playing](assets/exit_task.png)


view task list from new session:

![Agent Playing](assets/view_task_after_exit.png)


### Proposed Solution 2:
The above solution is not user friendly, as the user needs to adhere to specific instructions in order to use the task manager.

So tried developing a BERT based model which can be used for task intent classification based on input prompt given by user. Then using the intent prediction perform the required operation on task list 

classes for intent classification: [add_task, list_task, complete_task, delete_task].

example 1) input given by user can be 'Add "New book"', then the bert model should classify this intent as 'add_task' and then the add 'New book' to task list.

example 2) input given by user can be ' remove "cars"' then bert model should classify this as 'delete_task' and subsequently delete 'cars' from the task list.

In order to Fine tune BERT model, I created a synthetic data set of 1600 entries which will equally represent all class labels. The dataset looked like following:

### Outputs for Solution 2:
