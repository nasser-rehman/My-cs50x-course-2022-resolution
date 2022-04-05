# TASK LIST 2022
#### Video Demo:  <https://www.youtube.com/watch?v=4YhpLscuOMc>
#### Description:
This project is a webpage where anyone can create a tasklist. The implementation is fairly simple. I wanted to make a project like this to expand my knowledge of Javascript/jQuery and of techniques to manipulate local storage data.

Techonologies user:
- HTML
- CSS3
- JavaScript
- jQuery
- localStorage
- others small libraries

## How the webpage works?

The idea is simple. The user can register tasks to-do. During the registration of a task you just need to enter the field and press enter:

- Describe

Than the task will be listed in the task list section bellow the input. In the task list section, for each task registered by user, a textarea that contains the description of task and two more icons are presented, one of them being hidden, which is the check responsible to update the task list into storage, until the user changes the texarea content, and the other is the trash, which is responsible for deleting the task list. All the text input has a function to change the height so that it does not generate layout breaks and does not show the scroll bar when the text from task is to large. It's only possible to update one task per time. If two or three tasks have their content changed, only the content that the user clicks on the check icon will be saved, the others will shows the same content as before in localStorage.

### Database or not?
In this project i used localStorage. The localStorage isn't a database, it's only a key value pair stored into a variable associated to the window object that allows JavaScript apps and websites to save data in the web browser without an expiration date.

## Possible improvements
Here i can leave a list of possible improvements to my work:

- Have a registration and a database to store data from each user, making the app not just local
- Have the possibility of save all the tasks that have the content changed
- Possible implementation of a calendar for the user to be able to organize himself through it, registering the tasks and dividing them by days.
- A list of task that has already been completed

## How to launch application
Since the app doesn't have a back-end and all the functions is client-side, you just need to:

1. Make sure that you have internet connection as there are library dependencies
2. Clone the code
3. Extract the content of project
4. Once extracted go to the folder and open the index.html with browser
5. You are ready to use!