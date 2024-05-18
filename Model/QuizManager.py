from AttributesInfo import QResponseEnum as QRE, response_to_text


class Question:
    def __init__(self, text, options, description=""):
        self.text = text
        self.desc = description
        self.options = options

    def display_question(self):
        disp_txt = self.text + "\n"
        if len(self.desc) > 0:
            disp_txt += self.desc + "\n"

        disp_txt += "\n"

        # print options
        for i, j in enumerate(self.options):
            option_str = response_to_text(j)
            disp_txt += chr(65 + i)  # Ascii capital 'A'
            disp_txt += ". "
            disp_txt += option_str
            disp_txt += "\n"
        return disp_txt


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
                option_index = ord(user_input.upper()) - 65
                current_question = self.get_current_question()
                if 0 <= option_index < len(current_question.options):
                    self._chosen_options.append(current_question.options[option_index])
                else:
                    print("Invalid option. Please choose a valid option number.")
                    continue
            except ValueError:
                print(
                    "Invalid input. Please enter a number corresponding to the options."
                )
                continue

            if not self.next_question():
                print("End of quiz!")
                print("")
                break


questions_data = [
    Question(
        "Drug used by the patient:",
        [QRE.D_PENICILLAMINE, QRE.PLACEBO, QRE.NOT_AVAILABLE],
    ),
    Question(
        "Age group of the patient:",
        [QRE.TY, QRE.YA, QRE.MA, QRE.OA],
        "Teenager - Greater than or equal to 12 years but less than or equal to 18 years\nYoung Adult - Greater than or equal to 19 years but less than or equal to 40 years\nMiddle Aged - Greater than or equal to 41 years but less than or equal to 65 years\nOld Aged - Greater than 65 years",
    ),
    Question("Sex of the patient:", [QRE.MALE, QRE.FEMALE]),
    Question("Does the patient have Ascites?", [QRE.YES, QRE.NO, QRE.NOT_AVAILABLE]),
    Question(
        "Does the patient have Hepatomegaly?", [QRE.YES, QRE.NO, QRE.NOT_AVAILABLE]
    ),
    Question("Does the patient have Spiders?", [QRE.YES, QRE.NO, QRE.NOT_AVAILABLE]),
    Question(
        "Does the patient have Edema?", [QRE.ENDEMA_Y, QRE.ENDEMA_N, QRE.ENDEMA_S]
    ),
    Question(
        "Bilirubin level of the patient:",
        [QRE.NORMAL, QRE.ABNORMAL],
        "Normal - Less than 0.3 mg/dl\nAbnormal - Greater than or equal to 0.3 mg/dl",
    ),
    Question(
        "Cholesterol level of the patient:",
        [QRE.NORMAL, QRE.BORDERLINE_HIGH, QRE.HIGH, QRE.NOT_AVAILABLE],
        "Normal -  Less than 200 mg/dl\nAbnormal - Greater than 240 mg/dl\nBorderline - In between those values",
    ),
    Question(
        "Albumin level of the patient:",
        [QRE.LOW, QRE.NORMAL, QRE.HIGH],
        "Low - Less than 3.4 gm/dl\nHigh - Greater than 5.4 gm/dl\nNormal: In between those values",
    ),
    Question(
        "Copper level of the patient's urine:",
        [QRE.LOW, QRE.NORMAL, QRE.HIGH, QRE.NOT_AVAILABLE],
        "Low - Less than 20 ug/day\nHigh - Greater than 50 ug/day\nNormal - In between those values",
    ),
    Question(
        "Alkaline Phosphatase level of the patient:",
        [QRE.LOW, QRE.NORMAL, QRE.HIGH, QRE.NOT_AVAILABLE],
        "Low - Less than 44 U/liter\nnHigh - Greater than 147 U/liter\nNormal - In between those values",
    ),
    Question(
        "SGOT (Serum glutamic oxaloacetic transaminase) level of the patient's urine:",
        [QRE.LOW, QRE.NORMAL, QRE.HIGH, QRE.NOT_AVAILABLE],
        "Low - Less than 8000 U/ml\nnHigh - Greater than 45000 U/ml\nNormal - In between those values",
    ),
    Question(
        "Tryglicerides level of the patient:",
        [QRE.MILD, QRE.MODERATE, QRE.SEVERE, QRE.NOT_AVAILABLE],
        "Mild - Less than 200 mg/dl\nSevere - Greater than 500 mg/dl\nModerate - In Between those values",
    ),
    Question(
        "Platelets level of the patient:",
        [QRE.LOW, QRE.NORMAL, QRE.HIGH, QRE.NOT_AVAILABLE],
        "Low - Less than 150 ml/1000\nHigh - Greater than 450 ml/1000\nNormal: In between those values",
    ),
    Question(
        "Prothrombin time level of the patient:",
        [QRE.NORMAL, QRE.ABNORMAL, QRE.NOT_AVAILABLE],
        "Normal - Greater than or equal to 11 s but Less than or equal to 13.5 s\nAbnormal - Outside the range of those values",
    ),
    Question(
        "Histologic stage of disease of the patient:",
        [QRE.STAGE_1, QRE.STAGE_2, QRE.STAGE_3, QRE.STAGE_4, QRE.NOT_AVAILABLE],
    ),
]

quiz = Quiz(questions_data)

quiz.start_quiz()

print("Raw chosen options:")
print(quiz._chosen_options)
