import random
import time
import math
import os
import sys

# ==============================
# GLOBALS
# ==============================
score = 0
lives = 3
correct_streak = 0
highest_streak = 0
stages_cleared = 0
paused = False

# ==============================
# HELPERS
# ==============================
def clear_screen():
    time.sleep(1.5)
    os.system('cls' if os.name == 'nt' else 'clear')

def end_game():
    """Show final stats and quit"""
    print("\n===== GAME OVER =====")
    print(f"Final Score   : {score}")
    print(f"Highest Streak: {highest_streak}")
    print(f"Lives Left    : {lives}")
    print(f"Stages Cleared: {stages_cleared}")
    print("=====================\n")
    sys.exit()

def show_stats():
    print("\n--- Current Stats ---")
    print(f"Score: {score}")
    print(f"Highest Streak: {highest_streak}")
    print(f"Lives Left: {lives}")
    print(f"Stages Cleared: {stages_cleared}")
    print("--------------------\n")

def get_input(current_question, current_answer):
    """Input handler that keeps question and answer fixed during pause"""
    global paused
    while True:
        answer = input(current_question).strip().lower()

        if answer == "pause":
            paused = True
            print("⏸ Game paused.")
            show_stats()
            print("Type 'continue' to resume or 'end' to quit.")
            continue
        elif answer == "continue":
            if paused:
                paused = False
                print("▶ Game resumed!\n")
                return None  # re-ask same question
            else:
                print("Game is not paused.")
                continue
        elif answer == "end":
            end_game()

        if paused:
            print("Game is paused. Type 'continue' to resume or 'end' to quit.")
            continue

        return answer

# ==============================
# STAGE 1
# ==============================
stage1_correct = 0
print("Level 1: Simple addition and subtraction. Answer within 10 seconds for max points!")

while lives > 0 and stage1_correct < 10:
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    operation = random.choice(['+', '-'])
    if operation == '+':
        correct_answer = a + b
        question = f"What is {a} + {b}? "
    else:
        if a < b: a, b = b, a
        correct_answer = a - b
        question = f"What is {a} - {b}? "

    answered = False
    while not answered:
        print("You have 10 seconds to answer.")
        start_time = time.time()
        ans = get_input(question, correct_answer)
        if ans is None:
            continue  # resumed from pause

        try:
            ans = int(ans)
        except ValueError:
            print("Invalid answer. Enter a number, or 'pause'/'continue'/'end'.")
            continue

        elapsed = time.time() - start_time
        answered = True

        if ans == correct_answer:
            print("Correct!")
            correct_streak += 1
            stage1_correct += 1
            highest_streak = max(highest_streak, correct_streak)
            points = 100 if elapsed <= 10 else int(100 * math.exp(-1 * (elapsed - 10)))
            score += points
            if correct_streak % 3 == 0:
                lives += 1
                score += 500
                print("🔥 Streak! Extra life + 500 points!")
            print(f"Points: {points} | Time: {elapsed:.2f}s")
        else:
            print(f"Incorrect. Correct answer was {correct_answer}.")
            lives -= 1
            correct_streak = 0

        print(f"Score: {score} | Lives: {lives} | Streak: {correct_streak} | Stage 1 Correct: {stage1_correct}/10")
        clear_screen()

if lives > 0 and stage1_correct == 10:
    stages_cleared += 1

# ==============================
# STAGE 2
# ==============================
if lives > 0 and stage1_correct == 10:
    stage2_correct = 0
    print("Level 2: Multiplication and division (with math errors). Answer within 10 seconds for max points!")

    while lives > 0 and stage2_correct < 10:
        error_chance = random.random()
        if error_chance < 0.2:
            error_type = random.choice(['zero_div_zero', 'div_by_zero'])
            if error_type == 'zero_div_zero':
                question = "What is 0 / 0? "
                correct_answer = "math error"
            else:
                num = random.randint(-12, 12)
                question = f"What is {num} / 0? "
                correct_answer = "math error"
        else:
            a = random.randint(-12, 12)
            b = random.randint(1, 12)
            op = random.choice(['*', '/'])
            if op == '*':
                correct_answer = a * b
                question = f"What is {a} * {b}? "
            else:
                correct_answer = a
                dividend = a * b
                question = f"What is {dividend} / {b}? "

        answered = False
        while not answered:
            print("You have 10 seconds to answer.")
            start_time = time.time()
            ans = get_input(question, correct_answer)
            if ans is None:
                continue

            elapsed = time.time() - start_time
            answered = True

            if correct_answer == "math error":
                if ans in ["math error", "error", "undefined", "cannot divide by zero"]:
                    print("Correct!")
                    correct_streak += 1
                    highest_streak = max(highest_streak, correct_streak)
                    stage2_correct += 1
                    points = 250
                    score += points
                    if correct_streak % 3 == 0:
                        lives += 2
                        score += 1000
                        print("🔥 Streak! +2 lives +1000 points!")
                    print(f"Points: {points} | Time: {elapsed:.2f}s")
                else:
                    print("Incorrect. Correct answer: Math Error")
                    lives -= 1
                    correct_streak = 0
            else:
                try:
                    ans_int = int(ans)
                except ValueError:
                    ans_int = None

                if ans_int == correct_answer:
                    print("Correct!")
                    correct_streak += 1
                    highest_streak = max(highest_streak, correct_streak)
                    stage2_correct += 1
                    points = 250
                    score += points
                    if correct_streak % 3 == 0:
                        lives += 2
                        score += 1000
                        print("🔥 Streak! +2 lives +1000 points!")
                    print(f"Points: {points} | Time: {elapsed:.2f}s")
                else:
                    print(f"Incorrect. Correct answer: {correct_answer}")
                    lives -= 1
                    correct_streak = 0

            print(f"Score: {score} | Lives: {lives} | Streak: {correct_streak} | Stage 2 Correct: {stage2_correct}/10")
            clear_screen()

    if lives > 0 and stage2_correct == 10:
        stages_cleared += 1

# ==============================
# STAGE 3
# ==============================
if lives > 0 and stage2_correct == 10:
    print("Level 3: Exponents and square roots. Answer within 10 seconds for max points!")
    exponent_questions = [(f"What is {b}^{e}? ", b**e) for b in range(2, 10) for e in range(2, 4) if b**e <= 500]
    sqrt_questions = [(f"What is the square root of {r**2}? ", r) for r in range(2, 13)]
    stage3_questions = exponent_questions + sqrt_questions
    random.shuffle(stage3_questions)

    idx = 0
    while idx < len(stage3_questions) and lives > 0:
        question, correct_answer = stage3_questions[idx]
        answered = False
        while not answered:
            print("You have 10 seconds to answer.")
            start_time = time.time()
            ans = get_input(question, correct_answer)
            if ans is None:
                continue
            elapsed = time.time() - start_time
            answered = True

            try:
                ans_int = int(ans)
            except ValueError:
                ans_int = None

            if ans_int == correct_answer:
                print("Correct!")
                correct_streak += 1
                highest_streak = max(highest_streak, correct_streak)
                points = 500
                score += points
                if correct_streak % 3 == 0:
                    lives += 3
                    score += 1500
                    print("🔥 Streak! +3 lives +1500 points!")
                print(f"Points: {points} | Time: {elapsed:.2f}s")
                idx += 1  # Move to next question
            else:
                print(f"Incorrect. Correct answer: {correct_answer}")
                lives -= 1
                correct_streak = 0
                print("❌ This question will appear again later.")
                stage3_questions.append((question, correct_answer))
                idx += 1  # Move to next, incorrect question appended to end

            print(f"Score: {score} | Lives: {lives} | Streak: {correct_streak} | Stage 3 Progress: {idx}/{len(stage3_questions)}")
            clear_screen()

    if lives > 0:
        stages_cleared += 1

# ==============================
# STAGE 4
# ==============================
if lives > 0 and stages_cleared >= 3:
    print("Level 4: Advanced exponents and roots. Answer within 15 seconds for max points!")
    while lives > 0:
        op = random.choice(['^', 'sqrt'])
        if op == '^':
            while True:
                base = random.randint(2, 15)
                exp = random.randint(2, 4)
                correct_answer = base ** exp
                if correct_answer <= 1000:
                    break
            question = f"What is {base}^{exp}? "
        else:
            root = random.randint(2, 31)
            num = root ** 2
            correct_answer = root
            question = f"What is the square root of {num}? "

        answered = False
        while not answered:
            print("You have 15 seconds to answer.")
            start_time = time.time()
            ans = get_input(question, correct_answer)
            if ans is None:
                continue
            elapsed = time.time() - start_time
            answered = True

            try:
                ans_int = int(ans)
            except ValueError:
                ans_int = None

            if ans_int == correct_answer:
                print("Correct!")
                correct_streak += 1
                highest_streak = max(highest_streak, correct_streak)
                points = 750
                score += points
                if correct_streak % 3 == 0:
                    lives += 4
                    score += 2000
                    print("🔥 Streak! +4 lives +2000 points!")
                print(f"Points: {points} | Time: {elapsed:.2f}s")
            else:
                print(f"Incorrect. Correct answer: {correct_answer}")
                lives -= 1
                correct_streak = 0

            print(f"Score: {score} | Lives: {lives} | Streak: {correct_streak}")
            clear_screen()

    stages_cleared += 1

# ==============================
# END GAME
# ==============================
end_game()

