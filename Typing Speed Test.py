import time

def calculate_typing_speed(sentence, time_taken):
    words = sentence.split()
    num_words = len(words)
    seconds = time_taken / 60
    wpm = num_words / seconds
    return wpm

def main():
    print("Welcome to the Typing Speed Test!")
    sentence = "The quick brown fox jumps over the lazy dog."
    print("Your task is to type the following sentence:")
    print(sentence)
    input("Press Enter when you're ready to start...")
    
    start_time = time.time()
    user_input = input("Type the sentence here: ")
    end_time = time.time()
    
    time_taken = end_time - start_time
    user_typing_speed = calculate_typing_speed(sentence, time_taken)
    
    print(f"Time taken: {time_taken:.2f} seconds")
    print(f"Your typing speed: {user_typing_speed:.2f} WPM")

if __name__ == "__main__":
    main()
