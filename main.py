from modules import speech, reminders, news, weather
import string
from datetime import datetime
from word2number import w2n

# States: True = active, False = sleep
state = True

def greet():
    speech.speak("Hello, my name is Nova. How may I help you?")


def parse_reminder_command(command):
    patterns = [
        "set a reminder to",
        "set reminder to",
        "set a reminder for",
        "set reminder for"
    ]

    for p in patterns:
        if p in command:
            data = command.replace(p, "").strip()
            break
    else:
        return None, None, None

    if " at " not in data:
        return None, None, None

    task, time_text = data.split(" at ", 1)

    date = datetime.now().strftime("%Y-%m-%d")

    return task.strip(), date, time_text.strip()


def convert_time(time_text):
    time_text = time_text.lower().strip()

    parts = time_text.split()

    if len(parts) == 2:
        num, meridian = parts

        # Case: 100 pm, 630 am, 1015 pm etc.
        if num.isdigit() and len(num) >= 3:
            hour = int(num[:-2])
            minute = int(num[-2:])

            if 0 <= hour <= 12 and 0 <= minute <= 59:
                time_text = f"{hour}:{minute:02d} {meridian}"
                global t
                t = time_text
                

    formats = ["%I %p", "%I:%M %p"]

    for fmt in formats:
        try:
            return datetime.strptime(time_text, fmt).strftime("%H:%M")
        except:
            pass

    return None


def process_command(command):

    if "what can you do" in command:
        speech.speak("Try speaking:\n Set reminder to...\n"
        " show reminders.\n" \
        " show weather.\n" \
        " show news.\n" \
        " delete reminder {id}.")

    elif "set reminder" in command or "set a reminder" in command:
        task, date, time_text = parse_reminder_command(command)

        if not task:
            speech.speak("Please say the reminder properly. Example: set reminder to eat at 12 pm")
            return

        time_24 = convert_time(time_text)

        if not time_24:
            speech.speak("I could not understand the time.")
            return

        reminders.add_reminder(task, date, time_24)
        speech.speak(f"Reminder added for {task} at {t}")

    elif "show reminders" in command:
        result = reminders.show_reminders()
        speech.speak(result)

    elif "delete " in command:
    # Handle "all"
        if "all" in command:
            reminders.delete_reminders("all")
            speech.speak("All reminders deleted successfully.")
            return

        # Extract a number from command (digit or word)
        reminder_id = None
        for word in command.split():
            if word.isdigit():
                reminder_id = int(word)
                break
            else:
                try:
                    reminder_id = w2n.word_to_num(word)
                    break
                except:
                    continue

        # Delete the reminder if a valid number was found
        if reminder_id is not None:
            reminders.delete_reminders(reminder_id - 1) 
            speech.speak(f"Reminder number {reminder_id} deleted successfully.")
        else:
            speech.speak("I could not find which reminder to delete.")

    elif "weather" in command:
        result = weather.get_weather()

        if result is None:
            speech.speak(f"Sorry! Failed to retrieve data.")
        else:
            speech.speak(result)
        

    elif "news" in command:
        result = news.get_news()
        if result is None:
            speech.speak(f"Sorry! Failed to retrieve data.")
            return
        
        elif not result:
            speech.speak("No News Found")
            return
        speech.speak("The News are as follows:")
        for sl,headline in enumerate(result,start = 1):
            speech.speak(f"Headline {sl}: {headline}")

    else:
        speech.speak("Command not recognized.")


# ----- MAIN LOOP -----
greet()

while True:
    user_input = speech.listen()
    if user_input == "":
        continue

    user_input = user_input.lower().strip()
    user_input = user_input.translate(str.maketrans('', '', string.punctuation))


    if state:
        if "stop" in user_input or "sleep" in user_input:
            state = False
            speech.speak("Going to sleep. Say 'hey nova' to wake me up.")
        elif "exit" in user_input:
            speech.speak("Command Recognised.Exiting Program.")
            exit()
        else:
            process_command(user_input)

    else:
        if "nova" in user_input:
            state = True
            speech.speak("I am awake!")
