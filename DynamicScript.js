const questions = [
  { question: "What is 2 + 2?", choices: ["3", "4", "5", "6"]},
  { question: "Age group of the patient:", choices: ["Teenager (12-18 years old)", "Young Adult (19-40 years old)", "Middle Aged (41-65 years old)", "Old Aged (65 above)"]},
  { question: "Sex of the patient:", choices: ["MALE", "FEMALE"]},
  { question: "Drug used by the patient:", choices: ["D_PENICILLAMINE", "PLACEBO", "NOT_AVAILABLE"]},
  { question: "What is the largest planet in our solar system?", choices: ["Earth", "Mars", "Jupiter", "Saturn"]},
  { question: "What is the chemical symbol for water?", choices: ["H2O", "O2", "H2", "CO2"]},
  { question: "Who wrote 'Hamlet'?", choices: ["Charles Dickens", "William Shakespeare", "Mark Twain", "Jane Austen"]},
  // Add more questions here...
  // Ensure you have a total of 15 questions
];


const totalQuestionsElement = document.getElementById('total-num-questions');
const questionElement = document.getElementById('question');
const choicesElement = document.getElementById('choices');



let currentQuestionIndex = 0;
let userAnswers = [];

// Check User Answers
const userAnswerElement = document.getElementById('choices');

function showQuestion() {
  // Return if it reaches the maximum number of questions
  if (currentQuestionIndex >= questions.length) {
    // Put a function that shows the result

    return;
  }


  // Reset state before showing a new question
  resetState();

  const currentQuestion = questions[currentQuestionIndex];

  // This code is only to check the users answers
  //userAnswerElement.textContent = userAnswers;

  totalQuestionsElement.textContent = "Question " + (currentQuestionIndex + 1) + "/" + questions.length;
  questionElement.textContent = currentQuestion.question;

  // Add choices
  questions[currentQuestionIndex].choices.forEach(choice => {
    const button = document.createElement('button');
    button.innerHTML = choice;
    button.classList.add("btn", "button-question", "col-6", "mx-auto", "mb-3");
    button.onclick = () => selectAnswer(choice);
    choicesElement.appendChild(button);
  })


}


// Clear all child elements from the choicesElement
function resetState() {
  while (choicesElement.firstChild) {
    choicesElement.removeChild(choicesElement.firstChild);
  }
}

// Append the answer into an array and go to the next question
function selectAnswer(choice) {
  if (currentQuestionIndex >= questions.length) {
    return
  }
  userAnswers[currentQuestionIndex] = choice;
  currentQuestionIndex++;
  showQuestion();
}

// Go to the next question
function nextQuestion() {
  if (currentQuestionIndex >= questions.length) {
    return
  }
  currentQuestionIndex++;
  showQuestion();
}

// Go back to the previous question
function previousQuestion() {

  // Remove the answer to the current question
  if (currentQuestionIndex > 0) {
    userAnswers.splice(currentQuestionIndex, 1);
    currentQuestionIndex--;
  }

  showQuestion();
}


document.addEventListener('DOMContentLoaded', () => {
  showQuestion();
});