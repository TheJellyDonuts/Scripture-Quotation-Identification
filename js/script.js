const textInput = document.getElementById('text-input');
const uploadButton = document.getElementById('upload-button');
const fileInput = document.getElementById('file-input');
const output = document.getElementById('output');

textInput.addEventListener('input', updateOutput);
uploadButton.addEventListener('click', openFileInput);
fileInput.addEventListener('change', handleFileInput);

function updateOutput() {
  output.innerText = textInput.value;
}

function openFileInput() {
  fileInput.click();
}

function handleFileInput() {
  const file = fileInput.files[0];
  const reader = new FileReader();

  reader.onload = function(event) {
    output.innerText = event.target.result;
  }

  reader.readAsText(file);
  document.getElementById('text-input').value = '';
  document.getElementById('output').style.display = 'block';
}
