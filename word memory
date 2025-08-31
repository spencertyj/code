import random
import time
import math
import os
import msvcrt

LEADERBOARD_FILE = "leaderboard.txt"

def get_character_set():
    print("Choose sequence type:")
    print("1. Numbers only")
    print("2. Letters only")
    print("3. Both numbers and letters")
    choice = input("Enter 1, 2, or 3: ")
    if choice == "1":
        return "0123456789"
    elif choice == "2":
        return "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    else:
        return "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

def generate_sequence(length, chars):
    return [random.choice(chars) for _ in range(length)]

def show_sequence(sequence):
    print("Remember this sequence:")
    print(" ".join(sequence))
    time.sleep(3)
    print("\n" * 50)
    print("\033c", end="")

def flush_input():
    while msvcrt.kbhit():
        msvcrt.getch()

def get_player_input():
    flush_input()  # Clear any pre-typed input before prompting
    start_time = time.time()
    player_input = list(input("Enter the sequence: "))
    end_time = time.time()
    elapsed = end_time - start_time
    print(f"Time taken: {elapsed:.2f} seconds")
    return player_input, elapsed

def check_answer(player_input, correct_sequence):
    return player_input == correct_sequence

def get_time_limit(sequence_length):
    if sequence_length <= 4:
        return 5
    elif sequence_length <= 6:
        return 7
    elif sequence_length <= 8:
        return 10
    else:
        return 15

def calculate_score(elapsed, time_limit, correct):
    if not correct or elapsed > time_limit:
        return 0
    if elapsed <= 2:
        return 1000
    # Exponential decay, k=1
    score = int(1000 * math.exp(-1 * (elapsed - 1)))
    return score

def save_score(name, score):
    with open(LEADERBOARD_FILE, "a") as f:
        f.write(f"{name},{score}\n")

def load_leaderboard():
    scores = []
    if os.path.exists(LEADERBOARD_FILE):
        with open(LEADERBOARD_FILE, "r") as f:
            for line in f:
                parts = line.strip().split(",")
                if len(parts) == 2 and parts[1].isdigit():
                    scores.append((parts[0], int(parts[1])))
    # Sort by score descending, take top 10
    return sorted(scores, key=lambda x: x[1], reverse=True)[:10]

def display_leaderboard():
    leaderboard = load_leaderboard()
    print("\n=== Leaderboard ===")
    print("Rank | Name        | Score")
    print("-----------------------------")
    for i, (name, score) in enumerate(leaderboard, 1):
        print(f"{i:>4} | {name:<10} | {score}")
    print("-----------------------------\n")

def show_round_stats(lives, round_score, score, elapsed):
    print("\n--- Round Stats ---")
    print(f"Lives left: {lives}")
    print(f"Points scored this round: {round_score}")
    print(f"Total points: {score}")
    print(f"Time taken: {elapsed:.2f} seconds")
    print("-------------------\n")
    time.sleep(3)
    print("\n" * 50)
    print("\033c", end="")
    time.sleep(1)

def play_game():
    name = input("Enter your name for the leaderboard: ")
    chars = get_character_set()
    sequence_length = 3
    score = 0
    lives = 2
    while lives > 0:
        sequence = generate_sequence(sequence_length, chars)
        show_sequence(sequence)
        time_limit = get_time_limit(sequence_length)
        print(f"You have {time_limit} seconds to answer.")
        print(f"Lives: {lives}")
        player_input, elapsed = get_player_input()
        correct = check_answer(player_input, sequence)
        round_score = calculate_score(elapsed, time_limit, correct)
        if elapsed > time_limit:
            print(f"Time limit exceeded! You took {elapsed:.2f} seconds (limit was {time_limit} seconds).")
            lives -= 1
            round_score = 0
            show_round_stats(lives, round_score, score, elapsed)
        elif correct:
            print("Correct!")
            print(f"You answered in {elapsed:.2f} seconds")
            score += round_score
            sequence_length += 1
            if (sequence_length-3) % 3 == 0:
                lives += 1
                print("Congratulations! You gained an extra life.")
            show_round_stats(lives, round_score, score, elapsed)
        else:
            print("Wrong, you lost a life.")
            print(f"You answered in {elapsed:.2f} seconds")
            lives -= 1
            round_score = 0
            show_round_stats(lives, round_score, score, elapsed)
    print("Game over!")
    print("Your final score:", score)
    save_score(name, score)
    display_leaderboard()

# Start the game
play_game()
