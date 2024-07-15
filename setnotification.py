from plyer import notification
from datetime import datetime
import time

def show_notification(title, message):
    # Notification Displayer
    notification.notify(
        title = title,
        message = message,
        timeout=10  # time in seconds to disappear automatically
    )

def main():
    ###
    try:
        # (format HH:MM)
        notification_time = "12:00"
        while True:
            # Get the current system time
            now = datetime.now().strftime("%H:%M")
            
            # Check if the current time is the notification time
            if now == notification_time:
                show_notification("Notification!")
                time.sleep(60)  
            else:
                time.sleep(30) 

    except KeyboardInterrupt:
        print("\n\nQuitting...")

if __name__ == "__main__":
    main()
