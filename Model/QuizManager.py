class Question:
    def __init__(self, text, options):
        self.text = text
        self.options = options

    def display_question(self):
        formatted_options = "\n".join(f"{index + 1}. {option}" for index, option in enumerate(self.options))
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
        # return options in raw format, maybe display this with the prediction result as summary of chosen options
        return self._chosen_options
    
    def convert_to_model_options(self, reference_options):
        converted_options = []
        for i, chosen_option in enumerate(self._chosen_options):
            current_question = self._questions[i]
            try:
                option_index = current_question.options.index(chosen_option)
                converted_options.append(reference_options[i][option_index])
            except ValueError:
                converted_options.append(None) 
        return converted_options


# Maganda siguro na mabanggit sa questions yung pinagbasihan ng Low, Normal, etc
questions_data = [
    Question("Drug used by the patient:", ["d-penicillamine", "placebo", "Not Applicable"]),
    Question("Age group of the patient:", ["Young Adult", "Middle Aged", "Old Aged"]),
    Question("Sex of the patient:", ["Male", "Female"]),
    Question("Does the patient have Ascites?", ["Yes", "No", "Not Applicable"]),
    Question("Does the patient have Hepatomegaly?", ["Yes", "No", "Not Applicable"]),
    Question("Does the patient have Spiders?", ["Yes", "No", "Not Applicable"]),
    Question("Does the patient have Edema?", ["No Edema and no diuretic therapy for Edema", "With Edema without diuretics or Edema resolved with diuretics", "Edema despite diuretic theraphy"]),
    Question("Bilirubin level of the patient:", ["Normal", "Abnormal"]),
    Question("Cholesterol level of the patient:", ["Normal", "Borderline High", "High", "Not Applicable"]),
    Question("Albumin level of the patient:", ["Low", "Normal", "High", "Not Applicable"]),
    Question("Copper level of the patient's urine:", ["Low", "Normal", "High", "Not Applicable"]),
    Question("Alkaline Phosphatase level of the patient:", ["Low", "Normal", "High", "Not Applicable"]),
    Question("SGOT (Serum glutamic oxaloacetic transaminase) level of the patient's urine:", ["Low", "Normal", "High", "Not Applicable"]),
    Question("Tryglicerides level of the patient:", ["Mild", "Moderate", "Severe", "Not Applicable"]),
    Question("Platelets level of the patient:", ["Low", "Normal", "High", "Not Applicable"]),
    Question("Prothrombin time level of the patient:", ["Low", "Normal", "High", "Not Applicable"]),
    Question("Histologic stage of disease of the patient:", ["Stage 1", "Stage 2", "Stage 3", "Not Applicable"]),
]


options_for_prediction = [
    ["d-penicillamine", "placebo", "na"],
    ["ya", "ma", "oa"],
    ["m", "f"],
    ["y", "n", "na"],
    ["y", "n", "na"],
    ["y", "n", "na"],
    ["n", "s", "y"],
    ["normal", "abnormal"],
    ["normal", "borderline high", "high", "normal"],
    ["low", "normal", "high", "na"],
    ["low", "normal", "high", "na"],
    ["low", "normal", "high", "na"],
    ["low", "normal", "high", "na"],
    ["mild", "moderate", "severe", "na"],
    ["low", "normal", "high", "na"],
    ["low", "normal", "high", "na"],
    ["stage 1", "stage 2", "stage 3", "na"]
]

quiz = Quiz(questions_data)

quiz.start_quiz()

#print lang muna, connect nalang sa views kapag meron ng UI
print("Raw chosen options:")
print(quiz.get_user_chosen_options_raw())
print("")
print("Model based chosen options:")
print(quiz.convert_to_model_options(options_for_prediction))

