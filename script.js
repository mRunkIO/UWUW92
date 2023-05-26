const form = document.getElementById('question-form');
const answerContainer = document.getElementById('answer-container');

form.addEventListener('submit', function(e) {
  e.preventDefault();

  const question = document.getElementById('question').value;
  const schoolMarks = document.getElementById('school-marks').value;

  // Make an HTTP POST request to the backend
  fetch('/ask', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      question: question,
      school_marks: schoolMarks
    })
  })
  .then(response => response.json())
  .then(data => {
    // Display the generated answer in the answer container
    answerContainer.innerHTML = `<p>${data.answer}</p>`;
  })
  .catch(error => {
    console.error('Error:', error);
  });
});
