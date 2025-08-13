import json
import os

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

# Quiz questions
questions = {
      "What is the largest planet in our solar system?" :"Jupiter",
      "Who wrote the play Romeo and Juliet?" :"William Shakespear",
      "How many continents are there in the world?" :"Seven",
      "Which ocean is the deepest in the world?" :"Pacific Ocean",
      "What is the chemical symbol for gold?" :"Au",
      "Who painted the Mona Lisa?" :"Leonardo da Vinci",
      "In computing, what does “CPU” stand for?" :"Central Processing Unit",
      "Which country is known as the Land of the Rising Sun?" :"Japan",
      "What is the smallest prime number?" :"2",
      "In which year did the Titanic sink?" :"1912",
      "Which planet is known as the Red Planet?" :"Mars",
     " Who is the Greek god of the sea?" :"Poseidon",
      "What is the square root of 64?" :"8",
      "Which animal is known for having black and white stripes?" :"Zebra",
      "In what country would you find the Great Pyramid of Giza?" :"Egypt",
      "What is the main ingredient in guacamole?" :"Avocado",
      "Which language has the most native speakers in the world?" :"Mandarin Chinese",
      "In music, how many notes are in a standard major scale?" :"Seven(7)",
      "Which scientist proposed the theory of relativity?" :"Albert Einstein",
      "How many sides does a hexagon have?" :"Six(6)",
}

def play_quiz():
    name = input("Enter your name: ")
    score = 0

    for q, a in questions.items():
        ans = input(q).strip()
        if ans.lower() == a.lower():
            print("Correct! 🎉")
            score += 1
        else:
            print(f"❌ Wrong! The answer is {a}")

    print(f"\nYour score: {score}")

    leaderboard = load_leaderboard()
    leaderboard[name] = max(score, leaderboard.get(name, 0))
    save_leaderboard(leaderboard)

    print("\n🏆 Leaderboard 🏆")
    for player, scr in sorted(leaderboard.items(), key=lambda x: x[1], reverse=True):
        print(f"{player}: {scr}")

if __name__ == "__main__":
    play_quiz()
