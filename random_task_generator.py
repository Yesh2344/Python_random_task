import random
import time

def task_greet():
    greetings = ["Hello, world!", "Hi there!", "Greetings, human!", "Hey, how's it going?"]
    return random.choice(greetings)

def task_calculate():
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    operation = random.choice(['+', '-', '*', '/'])
    if operation == '+':
        result = a + b
    elif operation == '-':
        result = a - b
    elif operation == '*':
        result = a * b
    else:
        result = a / b
    return f"{a} {operation} {b} = {result:.2f}"

def task_quote():
    quotes = [
        "The only way to do great work is to love what you do. - Steve Jobs",
        "Life is what happens when you're busy making other plans. - John Lennon",
        "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
        "Success is not final, failure is not fatal: it is the courage to continue that counts. - Winston Churchill"
    ]
    return random.choice(quotes)

def task_joke():
    jokes = [
        "Why don't scientists trust atoms? Because they make up everything!",
        "Why did the scarecrow win an award? He was outstanding in his field!",
        "Why don't eggs tell jokes? They'd crack each other up!",
        "Why don't skeletons fight each other? They don't have the guts!"
    ]
    return random.choice(jokes)

# List of available tasks
tasks = [task_greet, task_calculate, task_quote, task_joke]

def run_bot():
    print("Random Task Bot is starting...")
    while True:
        # Randomly select a task
        task = random.choice(tasks)
        
        # Execute the task and print the result
        result = task()
        print(f"Performing task: {task.__name__}")
        print(f"Result: {result}")
        print("-" * 40)
        
        # Wait for a random time between 1 and 5 seconds
        delay = random.uniform(1, 5)
        time.sleep(delay)

if __name__ == "__main__":
    try:
        run_bot()
    except KeyboardInterrupt:
        print("\nRandom Task Bot is shutting down...")