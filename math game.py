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
stage_questions_done = set()  # tracks all previous stage questions
WINNING_SCORE = 10_000_000
infinite_mode = False

# ==============================
# HELPERS
# ==============================
def clear_screen():
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')

def end_game():
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

def calculate_points(stage, elapsed, time_limit):
    base_points = 50 + (stage - 1) * 50
    if elapsed <= time_limit:
        return base_points + int((time_limit - elapsed) * 20 * stage)
    return base_points

def countdown(sec=3):
    for i in range(sec, 0, -1):
        print(f"Next stage in {i}...")
        time.sleep(1)
    clear_screen()

def get_input(question):
    global paused
    while True:
        answer = input(question).strip().lower()
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
                return None
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
# START MENU
# ==============================
print("===== SELECT GAME MODE =====")
print("1. Standard (End at 10M points)")
print("2. Quick (End at 1M points)")
print("3. Infinite Mode")
mode_choice = input("Choose 1, 2, or 3: ").strip()
if mode_choice=="2":
    WINNING_SCORE = 1_000_000
elif mode_choice=="3":
    infinite_mode = True
print(f"Selected mode. WINNING_SCORE = {WINNING_SCORE:,}")
clear_screen()
time.sleep(1)

# ==============================
# HOW TO PLAY
# ==============================
print("===== HOW TO PLAY =====")
print("Complete all mental sums for the first five stages.")
print("Stages 6 and above can be solved with a calculator.")
print("Lose all your lives and you lose the game.")
print("Each level increases in difficulty but awards more points.")
print("Quick answers + streaks award extra lives and points.")
print(f"Reach {WINNING_SCORE:,} points to beat the game — or type 'continue' to play infinitely!")
print("\nRules: No calculator for the first 4 stages.")
print("========================")
print("\nGame starts in 10 seconds... Get ready!\n")
time.sleep(10)
clear_screen()

# ==============================
# STAGE 1
# ==============================
stage1_correct = 0
print("Level 1: Simple addition and subtraction. Answer within 10 seconds for max points!")

while lives > 0 and stage1_correct < 10:
    a, b = random.randint(1, 10), random.randint(1, 10)
    op = random.choice(['+', '-'])
    if op == '+':
        correct_answer = a + b
        question = f"What is {a} + {b}? "
    else:
        if a < b: a, b = b, a
        correct_answer = a - b
        question = f"What is {a} - {b}? "

    if question in stage_questions_done:
        continue

    answered = False
    while not answered:
        print("You have 10 seconds to answer.")
        start_time = time.time()
        ans = get_input(question)
        if ans is None:
            continue

        try:
            ans = int(ans)
        except ValueError:
            print("Invalid answer. Enter a number, or 'pause'/'continue'/'end'.")
            continue

        elapsed = time.time() - start_time
        answered = True

        if ans == correct_answer:
            print("✅ Correct!")
            correct_streak += 1
            stage1_correct += 1
            highest_streak = max(highest_streak, correct_streak)
            points = calculate_points(1, elapsed, 10)
            score += points
            if correct_streak % 3 == 0:
                lives += 1
                score += 500
                print("🔥 Streak! Extra life + 500 points!")
            stage_questions_done.add(question)
            print(f"Points: {points} | Time: {elapsed:.2f}s")
        else:
            print(f"❌ Incorrect. Correct answer: {correct_answer}")
            lives -= 1
            correct_streak = 0

        print(f"Score: {score} | Lives: {lives} | Streak: {correct_streak} | Stage 1 Correct: {stage1_correct}/10")
        clear_screen()

if lives > 0 and stage1_correct == 10:
    stages_cleared += 1
    countdown()

# ==============================
# STAGE 2
# ==============================
if lives > 0 and stages_cleared == 1:
    stage2_correct = 0
    print("Level 2: Multiplication and division (with math errors). Answer within 10 seconds for max points!")

    while lives > 0 and stage2_correct < 10:
        error_chance = random.random()
        if error_chance < 0.2:
            num = random.randint(-12, 12)
            if random.choice([True, False]):
                question, correct_answer = "What is 0 / 0? ", "math error"
            else:
                question, correct_answer = f"What is {num} / 0? ", "math error"
        else:
            a, b = random.randint(-12, 12), random.randint(1, 12)
            if random.choice(['*', '/']) == '*':
                correct_answer = a * b
                question = f"What is {a} * {b}? "
            else:
                dividend = a * b
                correct_answer = a
                question = f"What is {dividend} / {b}? "

        if question in stage_questions_done:
            continue

        answered = False
        while not answered:
            print("You have 10 seconds to answer.")
            start_time = time.time()
            ans = get_input(question)
            if ans is None:
                continue

            elapsed = time.time() - start_time
            answered = True

            if correct_answer == "math error":
                if ans in ["math error", "error", "undefined", "cannot divide by zero"]:
                    print("✅ Correct!")
                    correct_streak += 1
                    highest_streak = max(highest_streak, correct_streak)
                    stage2_correct += 1
                    points = calculate_points(2, elapsed, 10)
                    score += points
                    if correct_streak % 3 == 0:
                        lives += 2
                        score += 1000
                        print("🔥 Streak! +2 lives +1000 points!")
                    stage_questions_done.add(question)
                else:
                    print("❌ Incorrect. Correct answer: Math Error")
                    lives -= 1
                    correct_streak = 0
            else:
                try:
                    ans_int = int(ans)
                except ValueError:
                    ans_int = None

                if ans_int == correct_answer:
                    print("✅ Correct!")
                    correct_streak += 1
                    highest_streak = max(highest_streak, correct_streak)
                    stage2_correct += 1
                    points = calculate_points(2, elapsed, 10)
                    score += points
                    if correct_streak % 3 == 0:
                        lives += 2
                        score += 1000
                        print("🔥 Streak! +2 lives +1000 points!")
                    stage_questions_done.add(question)
                else:
                    print(f"❌ Incorrect. Correct answer: {correct_answer}")
                    lives -= 1
                    correct_streak = 0

            print(f"Score: {score} | Lives: {lives} | Streak: {correct_streak} | Stage 2 Correct: {stage2_correct}/10")
            clear_screen()

    if lives > 0 and stage2_correct == 10:
        stages_cleared += 1
        countdown()

# ==============================
# STAGE 3
# ==============================
if lives > 0 and stages_cleared == 2:
    print("Level 3: Exponents and square roots. Answer within 10 seconds for max points!")
    exponent_questions = [(f"What is {b}^{e}? ", b**e) for b in range(2, 10) for e in range(2, 4) if b**e <= 500]
    sqrt_questions = [(f"What is the square root of {r**2}? ", r) for r in range(2, 13)]
    stage3_questions = exponent_questions + sqrt_questions
    random.shuffle(stage3_questions)

    idx = 0
    while idx < len(stage3_questions) and lives > 0:
        question, correct_answer = stage3_questions[idx]
        if question in stage_questions_done:
            idx += 1
            continue
        answered = False
        while not answered:
            print("You have 10 seconds to answer.")
            start_time = time.time()
            ans = get_input(question)
            if ans is None:
                continue
            elapsed = time.time() - start_time
            answered = True
            try:
                ans_int = int(ans)
            except ValueError:
                ans_int = None
            if ans_int == correct_answer:
                print("✅ Correct!")
                correct_streak += 1
                highest_streak = max(highest_streak, correct_streak)
                points = calculate_points(3, elapsed, 10)
                score += points
                if correct_streak % 3 == 0:
                    lives += 3
                    score += 1500
                    print("🔥 Streak! +3 lives +1500 points!")
                stage_questions_done.add(question)
                idx += 1
            else:
                print(f"❌ Incorrect. Correct answer: {correct_answer}")
                lives -= 1
                correct_streak = 0
                print("❌ This question will appear again later.")
                stage3_questions.append((question, correct_answer))
                idx += 1
            print(f"Score: {score} | Lives: {lives} | Streak: {correct_streak} | Stage 3 Progress: {idx}/{len(stage3_questions)}")
            clear_screen()

    if lives > 0:
        stages_cleared += 1
        countdown()

# ==============================
# STAGE 4
# ==============================
if lives>0 and stages_cleared==3:
    print("Level 4: Advanced exponents & sqrt. 15s per question. Must answer all correctly.")
    stage4_questions=[]
    while len(stage4_questions)<10:
        op=random.choice(['^','sqrt'])
        if op=='^':
            base=random.randint(2,15)
            exp=random.randint(2,4)
            ans=base**exp
            if ans>1000: continue
            question=f"{base}^{exp} = ?"
        else:
            root=random.randint(2,31)
            ans=root
            question=f"sqrt({root**2}) = ?"
        if question not in stage_questions_done and question not in [q for q,_ in stage4_questions]:
            stage4_questions.append((question,ans))

    idx=0
    while idx<len(stage4_questions) and lives>0:
        question, correct_answer = stage4_questions[idx]
        print("You have 15 seconds to answer.")
        start_time=time.time()
        ans=get_input(question)
        if ans is None:
            continue
        elapsed=time.time()-start_time
        try: ans_int=int(ans)
        except: ans_int=None
        if ans_int==correct_answer:
            print("✅ Correct!")
            correct_streak+=1
            highest_streak=max(highest_streak,correct_streak)
            points=calculate_points(4,elapsed,15)
            score+=points
            if correct_streak%3==0:
                lives+=4
                score+=2000
                print("🔥 Streak! +4 lives +2000 points!")
            stage_questions_done.add(question)
            idx+=1
        else:
            print(f"❌ Incorrect. Correct answer: {correct_answer}")
            lives-=1
            correct_streak=0
            print("❌ This question will appear again later.")
            stage4_questions.append((question,correct_answer))
            idx+=1
        print(f"Score: {score} | Lives: {lives} | Streak: {correct_streak} | Stage 4 Progress: {idx}/{len(stage4_questions)}")
        clear_screen()
    if lives>0:
        stages_cleared+=1
        countdown()

# ==============================
# STAGE 5 (Skippable, answers <=20)
# ==============================
if lives>0 and stages_cleared==4:
    print("Stage 5: Logarithms and exponents. 20s per question. 1250 points per correct answer, streak bonus +2250, 1 life per streak.")
    choice=input("Do you want to attempt Stage 5? (y/n): ").strip().lower()
    if choice=='y':
        stage5_questions=[]
        while len(stage5_questions)<10:
            op=random.choice(['log','exp'])
            if op=='log':
                b=random.choice([2,3,5])
                ans=random.randint(1,4)  # answer <=20
                val=b**ans
                question=f"log base {b} of {val} = ?"
            else:
                base=random.randint(2,5)
                exp=random.randint(1,4)
                ans=base**exp
                if ans>20:
                    continue
                question=f"{base}^{exp} = ?"
            if question not in stage_questions_done and question not in [q for q,_ in stage5_questions]:
                stage5_questions.append((question,ans))
                stage_questions_done.add(question)
        idx=0
        while idx<len(stage5_questions) and lives>0:
            question, correct_answer = stage5_questions[idx]
            print("You have 20 seconds to answer.")
            start_time=time.time()
            ans=get_input(question)
            if ans is None: continue
            elapsed=time.time()-start_time
            try: ans_int=int(ans)
            except: ans_int=None
            if ans_int==correct_answer:
                print("✅ Correct!")
                correct_streak+=1
                highest_streak=max(highest_streak,correct_streak)
                score+=1250
                if correct_streak%3==0:
                    lives+=1
                    score+=2250
                    print("🔥 Streak bonus! +1 life +2250 points!")
                idx+=1
            else:
                print(f"❌ Incorrect. Correct answer: {correct_answer}")
                lives-=1
                correct_streak=0
                idx+=1
            print(f"Score: {score} | Lives: {lives} | Streak: {correct_streak} | Stage 5 Progress: {idx}/{len(stage5_questions)}")
            clear_screen()

# ==============================
# END GAME
# ==============================
if score>=WINNING_SCORE and not infinite_mode:
    print(f"\n🎉 Congratulations! You reached {WINNING_SCORE:,} points and beat the game!")
end_game()


