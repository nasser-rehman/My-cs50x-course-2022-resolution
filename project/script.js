// Get all todos data from localStorage
let todos = localStorage.getItem("todos");
// Converts the json string into a object
todos = JSON.parse(todos);

// When document is ready fire functions
$(document).ready(function () {
    // Check if has data into localStorage
    if (todos === null) {
        // Initialize empty todo
        todos = [];
        // Show message to user that not have nothing to show
        showHelperInfo();
    } else {
        // Hide message to user that show that not have nothing to show
        hideHelperInfo();
        // Call function to list all the tasks
        listTodos();
    }

    // When input field of description of task change, fire funcion
    $('#input').change(function () {
        // Get the date and create a new datetime
        var today = new Date();
        var date = today.getMonth() + 1 + '/' + today.getDate() + '/' + today.getFullYear();
        var time = today.getHours() + ':' + today.getMinutes() + ':' + today.getSeconds();
        var dateTime = date + ' ' + time;
        // Handle the input val
        var input = $(this).val();
        // Create a json with data provided by user and dateTime generated
        var todo = JSON.stringify({
            content: input,
            date: dateTime,
        });

        // Add new task to todos array
        todos.push(todo);
        // Set the localStorage value with the new todo array
        localStorage.setItem("todos", JSON.stringify(todos));
        // Set value from input to empty
        $(this).val('');
        // Hide Helper if it is showing
        hideHelperInfo();
        // List tasks again to update values
        listTodos();
        // Update textarea height
        updateTextareaHeight();
    });


    // When icon trash is clicked fire function
    $('ul').on('click', '.fa-trash', function () {
        // Get entire li and fadeOut
        $(this).parent('div').parent('li').fadeOut('slow');
        // Get the attribute alt from fa-trash tag into html that corresponds to index from array
        selected_index = parseInt($(this).attr("alt"));
        // Remove the element from array
        todos.splice(selected_index, 1);
        // Set the localStorage value with the new array
        localStorage.setItem("todos", JSON.stringify(todos));
        // Check if todos length is empty to show user the info
        if (todos.length == 0) {
            // Call function to show info
            showHelperInfo();
        }
    });

    // When icon check is pressed fire function
    $('ul').on('click', '.fa-check', function () {
        // Get all text from span tag on HTML
        var datetime = $(this).parent('.icons-handler').parents('li').children('.input-handler').children('.datetime-span').children('span').text();
        // Format text and gets only the datetime, removing the string Added
        var datetime_formatted = datetime.replace('Added ', '');
        // Get the description from textarea
        var content = $(this).parent('.icons-handler').parent('li').children('.input-handler').children('textarea').val();
        // Handle the index from object that is located into attribute data-content into icon
        var index = $(this).parent('.icons-handler').parent('li').children('.input-handler').children('textarea').attr('data-content');
        // Update values from object from index selected
        todos[index] = JSON.stringify({
            content: content,
            date: datetime_formatted,
        });
        // Update localStorage values with new array
        localStorage.setItem("todos", JSON.stringify(todos));
        // List all tasks
        listTodos();
    });

    // Handle event when window is resized to update textarea height value
    $(window).resize(function () {
        updateTextareaHeight();
    })
});

// Add events to all textarea, help to add to DOM elements
function updateTextareaEvents() {
    // When change, key up or paste inside any text area, fire function
    $('textarea').on('keyup change paste', function () {
        // Make check icon visible
        $(this).parent('.input-handler').parent('li').children('.icons-handler').children('.fa-check').css('display', 'block');
        // Update the textarea height to not show scroll bar
        updateTextareaHeight();
    });
}

// Update the textarea height to not show scroll bar
function updateTextareaHeight() {
    // bind function to each textarea
    $('textarea').each(function () {
        // Call function autosize that i got from https://github.com/jackmoore/autosize
        autosize($(this));
    })
}

// Make message fade in to screen
function showHelperInfo() {
    $('#helper-info').fadeIn('slow');
}

// Make message fade out from scrren
function hideHelperInfo() {
    $('#helper-info').fadeOut('slow');
}

// List all tasks into todos variable
function listTodos() {
    // Remove all li tag from html that are inside ul
    $('ul > li').remove();
    // Get JSON todos string from localStorage parsing to javascript object
    todos = JSON.parse(localStorage.getItem('todos'));
    // Check if it's empty
    if (todos != null) {
        // Iterate through all elements
        for (var i in todos) {
            // Parse position to object
            var todo = JSON.parse(todos[i]);
            // Append a li to ul with the todo content
            $('.wrap-container-list ul').append(`
            <li>
                <div class="input-handler">
                    <textarea type="text" data-content="${i}">${todo.content}</textarea>
                    <div class="datetime-span">
                        <span>Added ${todo.date}</span>
                    </div>
                </div>
                <div class="icons-handler">
                    <i class="fa fa-check" alt="${i}"></i>
                    <i class="fa fa-trash" alt="${i}"></i>
                </div>
            </li>`);
        }
    } else {
        // initialize todo with empty list
        todos = [];
        // Show message to usuer
        showHelperInfo();
    }
    // Update events into all textareas
    updateTextareaEvents();
    // Bind event to resize all textarea
    updateTextareaHeight();
}

// Empty todo tasklist from localStorage
function emptyTaskList() {
    // Remove any localStorage
    localStorage.clear();
    // Shows message to user
    showHelperInfo();
    // Set variable to empty array
    todos = [];
    // Get all li from ul
    var list = $('ul li');
    // Iterate to each li inside ul and fade out content
    list.each(function (idx, li) {
        $(li).fadeOut('fast');
    })
}