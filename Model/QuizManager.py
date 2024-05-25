import json
from typing import List, Tuple


class Question:
    def __init__(self, id: int, question_text: str, options: List[Tuple[str, str]], desc: str = ""):
        """
        Initialize a question.

        Args:
            id: The question ID
            question_text: The question text content
            options: List of options as tuples (option_id, option_text)
            desc: Optional description for the question.
        """
        self.id = id
        self.question_text = question_text
        self.desc = desc
        self.options = options

    def display_question(self) -> str:
        """
        Returns the formatted string of the question and its options.

        Returns:
            str: Formatted question
        """
        display_text = f"{self.question_text}\n"
        if self.desc:
            display_text += f"{self.desc}\n"
        display_text += "\n"

        for i, (option_id, option_text) in enumerate(self.options):
            display_text += f"{chr(65 + i)}. {option_text}\n"

        return display_text


class Quiz:
    def __init__(self, json_path: str):
        """
        Initialize the quiz with questions from a JSON file.

        Args:
            json_path: Path to the JSON file containing the questions.
        """
        self._questions: List[Question] = self._load_questions(json_path)
        self._current_question_index: int = 0
        self._chosen_options: List[Tuple[str, str]] = []

    def _load_questions(self, json_path: str) -> List[Question]:
        """
        Load questions from a JSON file.

        Args:
            json_path: Path to the JSON file containing the questions.
        
        Returns:
            List: List of Question objects.
        """
        with open(json_path, 'r') as file:
            loaded_json = json.load(file)
        
        return [Question(**question) for question in loaded_json]

    def get_current_question(self) -> Question:
        """
        Get the current question.

        Returns:
            Question: The current Question object.
        """
        return self._questions[self._current_question_index]

    def display_current_question(self) -> str:
        """
        Get the formatted string of the current question.

        Returns:
            str: Formatted question string.
        """
        return self.get_current_question().display_question()

    def next_question(self) -> bool:
        """
        Move to the next question if available.

        Returns:
            bool: True if there is a next question, False otherwise.
        """
        if self._current_question_index < len(self._questions) - 1:
            self._current_question_index += 1
            return True
        return False

    def start_quiz(self):
        """
        Start the quiz, displaying questions and collecting user answers.
        """
        while True:
            print(self.display_current_question())
            user_input = input("Your answer (type 'exit' to quit): ").strip().lower()

            if user_input == 'exit':
                print("Quiz ended.")
                break

            if self._process_answer(user_input):
                if not self.next_question():
                    print("End of quiz!")
                    break

        self._show_chosen_options()

    def _process_answer(self, answer: str) -> bool:
        """
        Process the user's answer.

        Args:
            answer: The user's answer input.

        Returns:
            bool: True if the answer is valid, False otherwise.
        """
        if len(answer) != 1 or not answer.isalpha():
            print("Invalid input. Please enter a valid letter corresponding to the options.")
            return False

        option_index = ord(answer.upper()) - 65
        current_question = self.get_current_question()

        if 0 <= option_index < len(current_question.options):
            self._chosen_options.append(current_question.options[option_index])
            return True
        else:
            print("Invalid option. Please choose a valid option letter.")
            return False

    def _show_chosen_options(self):
        """
        Displays the options chosen by the user.
        """
        print("Raw chosen options:")
        print(self._chosen_options)


if __name__ == "__main__":
    quiz = Quiz(r".\Resources\raw\questions.json")
    quiz.start_quiz()
