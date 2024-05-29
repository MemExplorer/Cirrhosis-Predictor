const totalQuestionsElement = document.getElementById('total-num-questions');
const questionElement = document.getElementById('question');
const choicesElement = document.getElementById('choices');
const quizElement = document.getElementById('quiz');
const progressBarElement = document.getElementById('progress-bar');
const progressDiv = document.getElementById('progressDiv');
const resultDiv = document.getElementById('resultDiv');
const backBtn = document.getElementById('backButton');
const percentageResultLbl = document.getElementById('percentageResult');
const labelResultLbl = document.getElementById('labelResult');

let currentQuestionIndex = 0;
let userAnswers = {};
backBtn.style.visibility = 'hidden';
resultDiv.style.visibility = 'hidden';
// Check User Answers
const userAnswerElement = document.getElementById('choices');

function httpGetAsync(theUrl, callback) {
  var xmlHttp = new XMLHttpRequest();
  xmlHttp.onreadystatechange = function () {
    if (xmlHttp.readyState == 4 && xmlHttp.status == 200)
      callback(xmlHttp.responseText);
  }
  xmlHttp.open("GET", theUrl, true); // true for asynchronous 
  xmlHttp.send(null);
}

function showQuestion() {

  // Reset state before showing a new question
  resetState();

  httpGetAsync("http://localhost/ViewModel/API.py?type=fetch&index=" + currentQuestionIndex, (resp) => {
    let jsonResp = JSON.parse(resp);
    if (jsonResp.success) {
      let questionResp = jsonResp.data;

      totalQuestionsElement.textContent = "Question " + (currentQuestionIndex + 1) + "/" + questionResp.quiz_length;
      questionElement.textContent = questionResp.question_text;
      if (questionResp.desc) {
        questionElement.innerHTML += "<br><p>" + questionResp.desc.replaceAll("\n","<br>") + "</p>";
      }

      // Add choices
      questionResp.options.forEach(choice => {
        const button = document.createElement('button');
        button.innerHTML = choice[1];
        button.classList.add("btn", "button-question", "col-5", "mx-auto", "mb-3", "me-3");
        button.onclick = () => selectAnswer(questionResp.id, choice[0], questionResp.quiz_length);
        choicesElement.appendChild(button);

      });
      const progress = ((Object.keys(userAnswers).length) / questionResp.quiz_length) * 100;
      progressBarElement.style.width = progress + "%";
    }
  });

}


// Clear all child elements from the choicesElement
function resetState() {
  while (choicesElement.firstChild) {
    choicesElement.removeChild(choicesElement.firstChild);
  }
}

// Append the answer into an array and go to the next question
function selectAnswer(qId, choice, qLen) {
  userAnswers[qId] = choice;
  if (currentQuestionIndex == 0) {
    backBtn.style.visibility = 'visible';
  }
  else if (currentQuestionIndex == qLen - 1) {
    // quiz end
    let payload = JSON.stringify(userAnswers);
    console.log(payload);
    let encodedPayload = btoa(payload).replaceAll("+", "-").replaceAll("/", "_");
    httpGetAsync("http://localhost/ViewModel/API.py?type=result&response_data=" + encodedPayload, (resp) => {
      let jsonResp = JSON.parse(resp);
      if (jsonResp.success) {
        let prediction = jsonResp.data;
        percentageResultLbl.textContent = prediction.percentage + "%";
        labelResultLbl.textContent = prediction.result;
      }
    });
    quizElement.remove();
    progressDiv.style.visibility = 'hidden';
    resultDiv.style.visibility = 'visible';
    backBtn.style.visibility = 'hidden';
    console.log("end");
  }
  else if (currentQuestionIndex >= qLen) {
    return
  }
  currentQuestionIndex++;
  showQuestion();
  console.log(currentQuestionIndex);

}


// Go back to the previous question
function previousQuestion() {

  // Remove the answer to the current question
  if (currentQuestionIndex > 0) {
    currentQuestionIndex--;
  }

  showQuestion();
}


document.addEventListener('DOMContentLoaded', () => {
  showQuestion();
});

function startTest() {
  location.replace("Questionnaire1.html")
}

function showSlide(slideIndex) {
  // Remove 'active' class from all carousel items
  var carouselItems = document.querySelectorAll('.carousel-item');
  carouselItems.forEach(function(item) {
      item.classList.remove('active');
  });
  
  // Add 'active' class to the selected carousel item
  var selectedSlide = document.getElementById('slide' + (slideIndex + 1));
  selectedSlide.classList.add('active');
}