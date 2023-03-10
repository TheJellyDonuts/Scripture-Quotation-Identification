// Reads the contents of the selected file and inserts them into the text box.
function loadFile() {
  // Select the file input and text box elements
  const fileInput = document.getElementById("file-input");
  const textBox = document.getElementById("text-input");

  // Get the selected file
  const file = fileInput.files[0];

  // Create a new FileReader object
  const reader = new FileReader();

  // When the file has loaded
  reader.onload = function() {
    // Insert the text into the text box
    textBox.value = reader.result;

    // Clear the file input value
    fileInput.value = "";
  };

  // Read the file as text
  reader.readAsText(file);
}

// Attach the function to the change event of the file input element
const fileInput = document.getElementById("file-input");
fileInput.addEventListener("change", loadFile);


