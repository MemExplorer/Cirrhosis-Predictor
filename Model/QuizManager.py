from enum import Enum

class Drug(Enum):
    D_PENICILLAMINE = "d-penicillamine"
    PLACEBO = "placebo"
    NOT_APPLICABLE = "na"

class AgeGroup(Enum):
    TEEN_YEARS = "ty"
    YOUNG_ADULT = "ya"
    MIDDLE_AGED = "ma"
    OLD_AGED = "oa"

class Sex(Enum):
    MALE = "m"
    FEMALE = "f"

class YesNo(Enum):
    YES = "y"
    NO = "n"
    NOT_APPLICABLE = "na"

class Edema(Enum):
    NO_EDEMA = "n"
    WITH_EDEMA_NO_DIURETICS = "s"
    EDEMA_WITH_DIURETICS = "y"

class NormalAbnormal(Enum):
    NORMAL = "normal"
    ABNORMAL = "abnormal"
    NOT_APPLICABLE = "na"

class Cholesterol(Enum):
    NORMAL = "normal"
    BORDERLINE_HIGH = "borderline high"
    HIGH = "high"
    NOT_APPLICABLE = "na"

class Level(Enum):
    LOW = "low"
    NORMAL = "normal"
    HIGH = "high"
    NOT_APPLICABLE = "na"

class Tryglicerides(Enum):
    MILD = "mild"
    MODERATE = "moderate"
    SEVERE = "severe"
    NOT_APPLICABLE = "na"

class HistologicStage(Enum):
    STAGE_1 = "stage 1"
    STAGE_2 = "stage 2"
    STAGE_3 = "stage 3"
    NOT_APPLICABLE = "na"


class Question:
    def __init__(self, text, options):
        self.text = text
        self.options = options

    def display_question(self):
        formatted_options = "\n".join(f"{index + 1}. {option.name.replace('_', ' ').title()}" for index, option in enumerate(self.options))
        return f"\n{self.text}\nOptions:\n{formatted_options}"


class Quiz:
    def __init__(self, questions):
        self._questions = questions
        self._current_question_index = 0
        self._chosen_options = []

    def get_current_question(self):
        return self._questions[self._current_question_index]

    def display_current_question(self):
        current_question = self.get_current_question()
        return current_question.display_question()

    def next_question(self):
        if self._current_question_index < len(self._questions) - 1:
            self._current_question_index += 1
            return True
        return False  # Indicates end of quiz

    def start_quiz(self):
        while True:
            print(self.display_current_question())
            user_input = input("Your answer (type 'exit' to quit): ")

            if user_input.lower() == "exit":
                print("Quiz ended.")
                break

            try:
                option_index = int(user_input) - 1
                current_question = self.get_current_question()
                if 0 <= option_index < len(current_question.options):
                    self._chosen_options.append(current_question.options[option_index])
                else:
                    print("Invalid option. Please choose a valid option number.")
                    continue  
            except ValueError:
                print("Invalid input. Please enter a number corresponding to the options.")
                continue  

            if not self.next_question():
                print("End of quiz!")
                print("")
                break

    def get_user_chosen_options_raw(self):
        return [option.value for option in self._chosen_options]
    
    def convert_to_model_options(self):
        return [option.name for option in self._chosen_options]


questions_data = [
    Question("Drug used by the patient:", list(Drug)),
    Question("Age group of the patient:\nTeenager - Greater than or equal to 12 years but less than or equal to 18 years\nYoung Adult - Greater than or equal to 19 years but less than or equal to 40 years\nMiddle Aged - Greater than or equal to 41 years but less than or equal to 65 years\nOld Aged - Greater than 65 years", list(AgeGroup)),
    Question("Sex of the patient:", list(Sex)),
    Question("Does the patient have Ascites?", list(YesNo)),
    Question("Does the patient have Hepatomegaly?", list(YesNo)),
    Question("Does the patient have Spiders?", list(YesNo)),
    Question("Does the patient have Edema?", list(Edema)),
    Question("Bilirubin level of the patient:\nNormal - Less than 0.3 mg/dl\nAbnormal - Greater than or equal to 0.3 mg/dl", list(NormalAbnormal)),
    Question("Cholesterol level of the patient:\nNormal -  Less than 200 mg/dl\nAbnormal - Greater than 240 mg/dl\nBorderline - In between those values", list(Cholesterol)),
    Question("Albumin level of the patient:\nLow - Less than 3.4 gm/dl\nHigh - Greater than 5.4 gm/dl\nNormal: In between those values", list(Level)),
    Question("Copper level of the patient's urine:\nLow - Less than 20 ug/day\nHigh - Greater than 50 ug/day\nNormal - In between those values", list(Level)),
    Question("Alkaline Phosphatase level of the patient:\nLow - Less than 44 U/liter\nnHigh - Greater than 147 U/liter\nNormal - In between those values", list(Level)),
    Question("SGOT (Serum glutamic oxaloacetic transaminase) level of the patient's urine:\nLow - Less than 8000 U/ml\nnHigh - Greater than 45000 U/ml\nNormal - In between those values", list(Level)),
    Question("Tryglicerides level of the patient:\nMild - Less than 200 mg/dl\nSevere - Greater than 500 mg/dl\nModerate - In Between those values", list(Tryglicerides)),
    Question("Platelets level of the patient:\nLow - Less than 150 ml/1000\nHigh - Greater than 450 ml/1000\nNormal: In between those values", list(Level)),
    Question("Prothrombin time level of the patient:\nNormal - Greater than or equal to 11 s but Less than or equal to 13.5 s\nAbnormal - Outside the range of those values", list(NormalAbnormal)),
    Question("Histologic stage of disease of the patient:", list(HistologicStage)),
]

quiz = Quiz(questions_data)

quiz.start_quiz()

print("Raw chosen options:")
print(quiz.get_user_chosen_options_raw())
print("")
print("Model based chosen options:")
print(quiz.convert_to_model_options())
