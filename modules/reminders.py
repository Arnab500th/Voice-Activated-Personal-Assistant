import pandas as pd
import os


REMINDER_FILE = "data/reminders.csv"

def load_reminders():
    if os.path.exists(REMINDER_FILE):
        return pd.read_csv(REMINDER_FILE)
        
    else:
        return pd.DataFrame(columns=["id", "reminder_text", "date","time"])

def add_reminder(reminder_text, date,time):
    df = load_reminders()
    new_id = df['id'].max() + 1 if not df.empty else 1
    df = pd.concat([df, pd.DataFrame([[new_id, reminder_text, date,time]], columns=df.columns)], ignore_index=True)
    df.to_csv(REMINDER_FILE, index=False)

def show_reminders():
    df = load_reminders()
    if df.empty:
        return "No reminders found. "
    
    speech_text = f"you have {len(df)} reminders."

    for _,row in df.iterrows():
        speech_text+=f"\nreminder {row["id"]}: {row["reminder_text"]} on {row["date"]} at {row["time"]}"

    return speech_text

def delete_reminders(id):
    df = load_reminders()
    if id == "all":
        df = df.drop(index=list(range(len(df))))
        df.to_csv(REMINDER_FILE, index=False)
    else:
        df = df.drop(index=id)
        df.to_csv(REMINDER_FILE, index=False)
    
    return "Reminders deleted successfully."
