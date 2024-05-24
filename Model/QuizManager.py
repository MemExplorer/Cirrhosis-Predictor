import json


class Question:
    def __init__(self, id, question_text, options, desc=""):
        self.id = id
        self.question_text = question_text
        self.desc = desc
        self.options = options

    def display_question(self):
        disp_txt = self.question_text + "\n"
        if len(self.desc) > 0:
            disp_txt += self.desc + "\n"

        disp_txt += "\n"

        # print options
        for i, j in enumerate(self.options):
            option_str = j[1]
            disp_txt += chr(65 + i)  # Ascii capital 'A'
            disp_txt += ". "
            disp_txt += option_str
            disp_txt += "\n"
        return disp_txt


class Quiz:
    def __init__(self, json_path):
        questions = []
        loaded_json = None
        with open(json_path, "r") as tr:
            json_content = tr.read()
            loaded_json = json.loads(json_content)

        for i in loaded_json:
            questions.append(Question(**i))
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
                    "Invalid input. Please enter a valid letter corresponding to the options."
                )
                continue

            if not self.next_question():
                print("End of quiz!")
                print("")
                break


quiz = Quiz(r".\Resources\raw\questions.json")

quiz.start_quiz()

print("Raw chosen options:")
print(quiz._chosen_options)
