let editor1, editor2;
const dmp = new diff_match_patch();

window.onload = function() {
  editor1 = CodeMirror.fromTextArea(document.getElementById('text1'), {
    lineNumbers: true,
    mode: 'text/plain'
  });
  editor2 = CodeMirror.fromTextArea(document.getElementById('text2'), {
    lineNumbers: true,
    mode: 'text/plain'
  });

  fetchTextsFromServer();
};

function compareText() {
  const text1 = editor1.getValue();
  const text2 = editor2.getValue();

  const diffs = dmp.diff_main(text1, text2);
  dmp.diff_cleanupSemantic(diffs);

  const minimapContent = diffs.map(diff => {
    const [type, text] = diff;
    if (type === diff_match_patch.DIFF_INSERT) {
      return `<span class="diff-insert">${text}</span>`;
    } else if (type === diff_match_patch.DIFF_DELETE) {
      return `<span class="diff-delete">${text}</span>`;
    } else {
      return text;
    }
  }).join('');

  document.getElementById('minimap-content').innerHTML = minimapContent;
}

function fetchTextsFromServer() {
  fetch('/textcompare/get_texts/')
    .then(response => response.json())
    .then(data => {
      editor1.setValue(data.text1);
      editor2.setValue(data.text2);
    });
}

function saveTextToServer() {
  const text1 = editor1.getValue();
  const text2 = editor2.getValue();
  fetch('/textcompare/save_text/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': getCookie('csrftoken')
    },
    body: JSON.stringify({ text1, text2 })
  });
}

function clearAll() {
  editor1.setValue('');
  editor2.setValue('');
  saveTextToServer();
  document.getElementById('minimap-content').innerHTML = '';
}

function clearBox(box) {
  if (box === 1) {
    editor1.setValue('');
  } else {
    editor2.setValue('');
  }
  saveTextToServer();
  document.getElementById('minimap-content').innerHTML = '';
}

function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
    const cookies = document.cookie.split(';');
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      if (cookie.substring(0, name.length + 1) === (name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

function processText() {
  saveTextToServer(); // Save current text before processing
  compareText();
}
