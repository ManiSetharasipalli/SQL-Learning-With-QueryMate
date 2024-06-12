// Declare editor variable in the global scope
var editor;

// Function to initialize CodeMirror editor
function initializeCodeMirror() {
    // Initialize CodeMirror on the textarea
    editor = CodeMirror(document.getElementById("editor-container"), {
        mode: "text/x-sql", // Set mode to SQL
        theme: "default", // Choose a theme
        lineNumbers: true, // Show line numbers
        indentUnit: 4 // Set indentation unit
    });

    // Check if query parameter is present in URL
    const urlParams = new URLSearchParams(window.location.search);
    const query = urlParams.get('query');
    if (query) {
        // Set the value of the editor to the query parameter value
        editor.setValue(query);
    }
}

// Function to execute SQL query
function executeQuery() {
    // Get query from CodeMirror editor
    var query = editor.getValue();

    // Create XMLHttpRequest object
    var xhr = new XMLHttpRequest();

    // Setup request
    xhr.open("POST", "/query_editor", true);
    xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");

    // Define what happens on successful data submission
    xhr.onload = function () {
        if (xhr.status === 200) {
            // Update HTML content with response
            var resultContainer = document.getElementById("result-container");
            resultContainer.innerHTML = xhr.responseText;
        } else {
            console.error('Request failed. Returned status of ' + xhr.status);
        }
    };

    // Send request with query data
    xhr.send("sql_query=" + encodeURIComponent(query));

    // Prevent default form submission
    return false;
}

// Call initializeCodeMirror function when the page is loaded
window.onload = initializeCodeMirror;
