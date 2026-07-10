
import json
import random
import sys

QUESTIONS = [
	{
		"question": "What is the capital of France?",
		"choices": ["A) Berlin", "B) Madrid", "C) Paris", "D) Rome"],
		"answer": "C"
	},
	{
		"question": "Which language is primarily used for data science?",
		"choices": ["A) Java", "B) Python", "C) C++", "D) Ruby"],
		"answer": "B"
	},
	{
		"question": "Who wrote '1984'?",
		"choices": ["A) Aldous Huxley", "B) George Orwell", "C) Ray Bradbury", "D) J.K. Rowling"],
		"answer": "B"
	},
	{
		"question": "What is 7 * 8?",
		"choices": ["A) 54", "B) 56", "C) 58", "D) 48"],
		"answer": "B"
	}
]

HIGH_SCORE_FILE = "quiz_highscore.json"


def load_highscore():
	try:
		with open(HIGH_SCORE_FILE, "r") as f:
			return json.load(f)
	except Exception:
		return {"name": None, "score": 0}


def save_highscore(name, score):
	data = {"name": name, "score": score}
	with open(HIGH_SCORE_FILE, "w") as f:
		json.dump(data, f)


def ask_question(q):
	print("\n" + q["question"])
	for choice in q["choices"]:
		print(choice)
	while True:
		ans = input("Your answer (A/B/C/D): ").strip().upper()
		if ans in ("A", "B", "C", "D"):
			return ans == q["answer"]
		print("Please enter A, B, C or D.")


def run_quiz():
	print("Simple Quiz Game")
	name = input("Enter your name: ").strip() or "Player"
	qs = QUESTIONS.copy()
	random.shuffle(qs)
	score = 0
	for q in qs:
		if ask_question(q):
			print("Correct!")
			score += 1
		else:
			print(f"Wrong. Correct answer: {q['answer']}")
	print(f"\n{name}, your score: {score}/{len(qs)}")
	hs = load_highscore()
	if score > hs.get("score", 0):
		print("New high score!")
		save_highscore(name, score)
	else:
		if hs.get("name"):
			print(f"High score: {hs['score']} by {hs['name']}")


if __name__ == "__main__":
	try:
		run_quiz()
	except KeyboardInterrupt:
		print("\nGoodbye")
		sys.exit(0)
