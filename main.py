import time
import schedule
from database import Database
from notification_system import NotificationSystem
from seeders import addBooks, addClassesRange


def main():
    # Initialize database and notification system
    db = Database()
    notifier = NotificationSystem('awwal', db)

    # Example of adding data (uncomment and modify as needed)
    """
    # Add courses
    db.add_course("Mathematics", "Monday", "09:00", "Room 101")
    db.add_course("Physics", "Monday", "11:00", "Room 102")

    # Add books
    db.add_book("Calculus I", "John Smith", 1, "2025-02-21")

    # Add exams
    db.add_exam(1, "2025-03-15", "Differential Equations")
    """
    addBooks()
    addClassesRange()

    # Schedule notifications
    schedule.every().day.at("07:00").do(notifier.send_daily_schedule)  # Morning summary

    # Check for class reminders every 20 minutes
    schedule.every(20).minutes.do(notifier.send_class_reminder)

    # Send initial test notification
    notifier.send_notification(
        "System Start",
        "🚀 Student reminder system is now active!",
        tags="system"
    )

    # Keep the script running
    while True:
        schedule.run_pending()
        time.sleep(60)


if __name__ == "__main__":
    main()