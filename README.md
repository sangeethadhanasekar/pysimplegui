# pysimplegui
## to_do_list(pysimplegui)
This is a simple To-Do List application built using Python and the PySimpleGUI library. The application provides a graphical user interface (GUI) that allows users to manage their tasks efficiently. Here's a brief overview of the application's functionalities:

GUI Layout:
The application features a clean and intuitive GUI layout. It includes the following components:

Task Input Field: Users can enter their tasks in the input field provided.
Add, Edit, and Delete Buttons: These buttons allow users to add new tasks, edit existing tasks, and delete tasks, respectively.
List Boxes: Tasks, their priorities, and deadline dates are displayed in separate list boxes.
Loading Previous Tasks:
If a file named "output_pysimplegui.txt" exists, the application reads its contents to load any previously saved tasks. Each line in the file represents a task, with the format "task,priority,date."

##1.Adding New Tasks:
Users can add new tasks by entering the task description in the input field and clicking the "Add" button. The newly added task will appear in the respective list boxes, and users can also select the task's priority and set a deadline date.


##2.Editing Tasks:
To edit an existing task, users can select the task from the list box and click the "Edit" button. The task's name, priority, and date will be automatically populated in the input fields. Users can make changes as needed and save the updated task by clicking the "Save" button.



##3.Deleting Tasks:
Users can easily remove a task by selecting it from the list box and clicking the "Delete" button. The task will be promptly deleted from the list.


##4.Continuous Execution:
The program runs in a loop, continuously processing user events from the GUI, until the user decides to exit the application.


##5.Saving Changes:
When the user exits the program, all changes made to the task list will be saved to the "output_pysimplegui.txt" file, allowing users to resume their task management in subsequent sessions.
