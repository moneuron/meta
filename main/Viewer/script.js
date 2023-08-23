const fileInput = document.getElementById('fileInput');
const sortOption = document.getElementById('sortOption');
const fileList = document.getElementById('fileList');
const downloadButton = document.getElementById('downloadButton');
let textEntries = {};

fileInput.addEventListener('change', handleFileInputChange);
sortOption.addEventListener('change', updateSort);
downloadButton.addEventListener('click', handleDownloadClick);
fileList.addEventListener('click', handleClearButtonClick);

function updateSort() {
  const files = Array.from(fileList.querySelectorAll('.file-item'));
  const option = sortOption.value;
  files.sort((a, b) => {
    if (option === 'name') {
      return a.querySelector('h2').textContent.localeCompare(b.querySelector('h2').textContent);
    } else if (option === 'number') {
      return parseInt(a.querySelector('h2').textContent) - parseInt(b.querySelector('h2').textContent);
    }
  });
  fileList.innerHTML = '';
  files.forEach(file => fileList.appendChild(file));
}

function handleFileInputChange(event) {
  fileList.innerHTML = '';
  textEntries = {};
  const files = event.target.files;
  for (const file of files) {
    if (file.type === 'text/plain') {
      readTextFile(file);
    }
  }
}

function readTextFile(file) {
  const reader = new FileReader();
  reader.onload = function (e) {
    const fileContent = e.target.result;
    const fileId = Date.now();
    const doi = getDOIFromText(fileContent);
    textEntries[fileId] = '';
    const fileDiv = createFileDiv(file.name, fileContent, fileId, doi);
    fileList.appendChild(fileDiv);
    updateSort();
  };
  reader.readAsText(file);
}

function createFileDiv(fileName, fileContent, fileId, doi) {
  const fileDiv = document.createElement('div');
  fileDiv.classList.add('file-item');
  fileDiv.innerHTML = `
    <h2>${fileName}</h2>
    <pre>${highlightLinks(fileContent)}</pre>
    <div class="textarea-container">
      <textarea data-file-id="${fileId}" rows="1" cols="30" placeholder="Cleared!">${doi}</textarea>
      ${createClearButton(fileId).outerHTML}
    </div>
  `;
  return fileDiv;
}

function getDOIFromText(text) {
  const doiRegex = /\b(10\.\d{4,}(?:\.\d+)*\/\S+)\b/g;
  const matches = text.match(doiRegex);
  return matches ? matches[0] : '';
}

function highlightLinks(text) {
  const doiRegex = /\b(10\.\d{4,}(?:\.\d+)*\/\S+)\b/g;
  return text.replace(doiRegex, '<a href="https://doi.org/$1" target="_blank" class="view-article-button">Full Text</a>');
}

function createClearButton(fileId) {
  const clearButton = document.createElement('button');
  clearButton.textContent = 'X';
  clearButton.classList.add('clear-button');
  return clearButton;
}

function handleClearButtonClick(event) {
  if (event.target && event.target.classList.contains('clear-button')) {
    clearTextarea(event.target.previousElementSibling);
  }
}

function clearTextarea(textarea) {
  textarea.value = '';
}

function handleDownloadClick() {
  const textData = [];
  const textareas = fileList.querySelectorAll('textarea');
  textareas.forEach(textarea => {
    const fileId = textarea.getAttribute('data-file-id');
    const text = textarea.value.trim();
    if (text !== '') {
      textData.push(text);
    }
    textEntries[fileId] = text;
  });

  const textBlob = new Blob([textData.join('\n')], { type: 'text/plain' });
  const downloadLink = document.createElement('a');
  downloadLink.href = URL.createObjectURL(textBlob);
  downloadLink.download = 'text_entries.txt';
  downloadLink.click();
}


window.addEventListener('beforeunload', function (event) {
  event.preventDefault();
  event.returnValue = '';
});

window.addEventListener('unload', function (event) {
  event.returnValue = 'You have unsaved changes. Are you sure you want to leave?';
});
