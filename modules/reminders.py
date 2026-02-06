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

def delete_reminders(reminder_id):
    df = load_reminders()
    
    if reminder_id == "all":
        df = df.iloc[0:0]  # empty the DataFrame
        df.to_csv(REMINDER_FILE, index=False)
        return "All reminders deleted successfully."
    
    # Drop by 'id' column, not DataFrame index
    if reminder_id in df['id'].values:
        df = df[df['id'] != reminder_id]
        df.to_csv(REMINDER_FILE, index=False)
        return f"Reminder {reminder_id} deleted successfully."
    else:
        return f"Reminder {reminder_id} not found."

