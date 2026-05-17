# 🧠 Day 17: OOP Quiz Game

## 📝 About the Project
The **OOP Quiz Game** is a fully object-oriented console-based "True/False" game written in Python. The application fetches a diverse set of questions from a data store, dynamically instantiates question objects, and manages the entire game flow – from presenting questions and receiving user input to validating answers and tracking the score in real-time.

This project was built from the ground up using the **Object-Oriented Programming (OOP)** paradigm, ensuring clean separation of concerns and adherence to the *Single Responsibility Principle*.

---

## 🛠️ Project Architecture (Modularity)
The codebase is decoupled into 4 main collaborating components, avoiding a monolithic structure and allowing for clean extension:

1. **`main.py`** – The main entry point of the application. It orchestrates the process: retrieves raw question data, maps it to instances of the `Question` class, creates the `QuizBrain` runtime, and kicks off the main game loop.
2. **`question_model.py`** – The `Question` model class. It defines a blueprint for a single question, storing the question text (`text`) and its correct answer (`answer`).
3. **`quiz_brain.py`** – The core game engine (session controller). It tracks the current question number, the user's score, prompts the user via console inputs, checks their answers, and determines if there are remaining questions.
4. **`data.py`** – The data module containing a static list of questions structured similarly to the Open Trivia Database API format.

---

## 🎓 What I Learned

By building the **Day 17** project, I deeply explored core object-oriented programming and software design concepts:

### 1. Class Construction & Initialization (`OOP`)
* Learned how to define custom classes in Python using the `class` keyword.
* Mastered the role of the `__init__(self)` constructor to initialize attributes (properties) of a new object instance.

### 2. Attributes vs. Methods
* **Attributes** (`self.score`, `self.question_number`): Used to encapsulate and store the internal state of an object.
* **Methods** (`next_question()`, `still_has_questions()`): Represent the behaviors of an object. Understood how methods can safely mutate an object's internal state.

### 3. Separation of Concerns (SoC)
* Rather than keeping everything inside a single monolithic script, I decoupled the data layer, the presentation model, and the game loop. The `Question` class *only* represents data, and the `QuizBrain` *only* controls the game logic. This keeps the code highly readable, maintainable, and testable.

### 4. Dynamically Managing Lists of Objects
* Learned how to iterate through raw dictionary data (JSON-like arrays) and dynamically map them into a list of strong object instances (`question_bank`) to pass to other runtime components.

---

## 🚀 How to Run the Project

Ensure you have Python 3 installed. Navigate to the project directory and run `main.py`:

```powershell
# Navigate to the Day 17 folder
cd "Day 17 OOP Quiz game"

# Run the game
python main.py
```

## 🎮 Gameplay Showcase
```text
Q.1: Pac-Man was invented by the designer Toru Iwatani while he was eating pizza. (True/False)
True
You got it right! Your score is: 1/1
The correct answer was: True.

Q.2: The iPhone 3G was the second iPhone generation. (True/False)
True
You got it right! Your score is: 2/2
The correct answer was: True.

Q.3: According to Greek Mythology, Atlas was an Olympian God. (True/False)
True
Sorry, that's wrong. 2/3
The correct answer was: False.
...
You've completed the quiz. Your final score is: 8/10
```
