const questions = [
  { question: "What is the capital of France?", choices: ["Paris", "London", "Berlin", "Madrid"], correct: "Paris" },
  { question: "What is 2 + 2?", choices: ["3", "4", "5", "6"], correct: "4" },
  { question: "What is the largest planet in our solar system?", choices: ["Earth", "Mars", "Jupiter", "Saturn"], correct: "Jupiter" },
  { question: "What is the chemical symbol for water?", choices: ["H2O", "O2", "H2", "CO2"], correct: "H2O" },
  { question: "Who wrote 'Hamlet'?", choices: ["Charles Dickens", "William Shakespeare", "Mark Twain", "Jane Austen"], correct: "William Shakespeare" },
  // Add more questions here...
  // Ensure you have a total of 15 questions
];


let currentQuestionIndex = 0;
let score = 0;

function showQuestion() {
  if (currentQuestionIndex >= questions.length) {
      showResult();
      return;
  }

  const questionElement = document.getElementById('question');
  const choicesElement = document.getElementById('choices');

  questionElement.textContent = questions[currentQuestionIndex].question;
  choicesElement.innerHTML = '';

  questions[currentQuestionIndex].choices.forEach(choice => {
      const button = document.createElement('button');
      button.textContent = choice;
      button.onclick = () => selectAnswer(choice);
      choicesElement.appendChild(button);
  });
}

function selectAnswer(choice) {
  const correctAnswer = questions[currentQuestionIndex].correct;
  if (choice === correctAnswer) {
      score++;
  }

  currentQuestionIndex++;
  showQuestion();
}

function nextQuestion() {
  currentQuestionIndex++;
  showQuestion();
}

function showResult() {
  const quizElement = document.getElementById('quiz');
  const resultElement = document.getElementById('result');

  quizElement.style.display = 'none';
  resultElement.style.display = 'block';
  resultElement.textContent = `You scored ${score} out of ${questions.length}`;
}

document.addEventListener('DOMContentLoaded', () => {
  showQuestion();
});
