import json
import os
import random

LEADERBOARD_FILE = "leaderboard.json"

# Load leaderboard
def load_leaderboard():
    if os.path.exists(LEADERBOARD_FILE):
        with open(LEADERBOARD_FILE, "r") as f:
            return json.load(f)
    return {}

# Save leaderboard
def save_leaderboard(leaderboard):
    with open(LEADERBOARD_FILE, "w") as f:
        json.dump(leaderboard, f, indent=4)

# Multiple choice questions
questions = {
    "What is the largest planet in our solar system?": {
        "answer": "Jupiter",
        "options": ["Earth", "Mars", "Jupiter", "Saturn"]
    },
    "Who wrote the play Romeo and Juliet?": {
        "answer": "William Shakespear",
        "options": ["Charles Dickens", "William Shakespear", "Jane Austen", "Mark Twain"]
    },
    "How many continents are there in the world?": {
        "answer": "Seven",
        "options": ["Five", "Six", "Seven", "Eight"]
    },
    "Which ocean is the deepest in the world?": {
        "answer": "Pacific Ocean",
        "options": ["Atlantic Ocean", "Pacific Ocean", "Indian Ocean", "Arctic Ocean"]
    },
    "What is the chemical symbol for gold?": {
        "answer": "Au",
        "options": ["Ag", "Au", "Gd", "Pt"]
    },
    "Who painted the Mona Lisa?": {
        "answer": "Leonardo da Vinci",
        "options": ["Vincent van Gogh", "Leonardo da Vinci", "Pablo Picasso", "Claude Monet"]
    },
    "In computing, what does “CPU” stand for?": {
        "answer": "Central Processing Unit",
        "options": ["Central Processing Unit", "Computer Personal Unit", "Central Program Utility", "Control Process Unit"]
    },
    "Which country is known as the Land of the Rising Sun?": {
        "answer": "Japan",
        "options": ["China", "Japan", "Thailand", "South Korea"]
    },
    "What is the smallest prime number?": {
        "answer": "2",
        "options": ["1", "2", "3", "5"]
    },
    "In which year did the Titanic sink?": {
        "answer": "1912",
        "options": ["1910", "1911", "1912", "1913"]
    },
    "Which planet is known as the Red Planet?": {
        "answer": "Mars",
        "options": ["Mars", "Venus", "Mercury", "Jupiter"]
    },
    "Who is the Greek god of the sea?": {
        "answer": "Poseidon",
        "options": ["Zeus", "Poseidon", "Hades", "Ares"]
    },
    "What is the square root of 64?": {
        "answer": "8",
        "options": ["6", "7", "8", "9"]
    },
    "Which animal is known for having black and white stripes?": {
        "answer": "Zebra",
        "options": ["Tiger", "Zebra", "Panda", "Skunk"]
    },
    "In what country would you find the Great Pyramid of Giza?": {
        "answer": "Egypt",
        "options": ["Sudan", "Egypt", "Morocco", "Libya"]
    },
    "What is the main ingredient in guacamole?": {
        "answer": "Avocado",
        "options": ["Avocado", "Cucumber", "Lettuce", "Green Pepper"]
    },
    "Which language has the most native speakers in the world?": {
        "answer": "Mandarin Chinese",
        "options": ["English", "Mandarin Chinese", "Spanish", "Hindi"]
    },
    "In music, how many notes are in a standard major scale?": {
        "answer": "Seven(7)",
        "options": ["Six(6)", "Seven(7)", "Eight(8)", "Nine(9)"]
    },
    "Which scientist proposed the theory of relativity?": {
        "answer": "Albert Einstein",
        "options": ["Isaac Newton", "Albert Einstein", "Niels Bohr", "Galileo Galilei"]
    },
    "How many sides does a hexagon have?": {
        "answer": "Six(6)",
        "options": ["Five(5)", "Six(6)", "Seven(7)", "Eight(8)"]
    },
}

def play_quiz():
    name = input("Enter your name: ")
    score = 0

    print("\nType 'quit' anytime to stop the quiz early.\n")

    for q, data in questions.items():
        options = data["options"][:]
        random.shuffle(options)  # Randomize option order

        print(f"\n{q}")
        letters = ["A", "B", "C", "D"]
        for i, option in enumerate(options):
            print(f"{letters[i]}. {option}")

        ans = input("Your choice: ").strip().upper()

        if ans.lower() == "quit":
            break

        if ans in letters:
            chosen = options[letters.index(ans)]
            if chosen.lower() == data["answer"].lower():
                print("✅ Correct!")
                score += 1
            else:
                print(f"❌ Wrong! The answer is {data['answer']}")
        else:
            print("Invalid choice. Please enter A, B, C, or D.")

    print(f"\nYour score: {score}")

    leaderboard = load_leaderboard()
    leaderboard[name] = max(score, leaderboard.get(name, 0))
    save_leaderboard(leaderboard)

    print("\n🏆 Leaderboard 🏆")
    for player, scr in sorted(leaderboard.items(), key=lambda x: x[1], reverse=True):
        print(f"{player}: {scr}")

if __name__ == "__main__":
    play_quiz()
