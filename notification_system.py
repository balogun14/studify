from datetime import datetime

import requests

from database import Database


class NotificationSystem:
    def __init__(self, topic: str, db: Database):
        self.topic = topic
        self.ntfy_url = f"https://ntfy.sh/{topic}"
        self.db = db
        self.quotes_api = "https://api.quotable.io/random"

    def send_notification(self, title: str, message: str, priority: str = "default", tags: str = None):
        try:
            headers = {
                "Title": title,
                "Priority": priority
            }
            if tags:
                headers["Tags"] = tags

            response = requests.post(
                self.ntfy_url,
                data=message.encode(encoding='utf-8'),
                headers=headers
            )
            print(f"Notification sent: {title} - {message}")
        except Exception as e:
            print(f"Error sending notification: {e}")

    def send_daily_schedule(self):
        classes = self.db.get_todays_classes()
        readings = self.db.get_todays_readings()
        exams = self.db.get_upcoming_exams()

        # Morning summary message
        summary = "📅 TODAY'S SCHEDULE:\n\n"

        if classes:
            summary += "🎓 CLASSES:\n"
            for cls in classes:
                summary += f"- {cls['name']} at {cls['time']}"
                if cls['room']:
                    summary += f" (Room {cls['room']})"
                summary += "\n"

        if readings:
            summary += "\n📚 READINGS DUE:\n"
            for reading in readings:
                summary += f"- {reading['title']} ({reading['course']})\n"

        if exams:
            summary += "\n📝 UPCOMING EXAMS:\n"
            for exam in exams:
                summary += f"- {exam['course']} on {exam['date']}: {exam['topic']}\n"

        self.send_notification(
            "Daily Schedule",
            summary,
            priority="high",
            tags="calendar,books,exam"
        )

    def send_class_reminder(self):
        """Check and send reminders for upcoming classes"""
        classes = self.db.get_todays_classes()

        for cls in classes:
            class_time = datetime.strptime(cls['time'], "%H:%M").time()
            if (datetime.now().time().hour == class_time.hour - 1 and
                    datetime.now().time().minute == 20):
                message = f"🎓 Upcoming class: {cls['name']} at {cls['time']}"
                if cls['room']:
                    message += f" in Room {cls['room']}"
                self.send_notification(
                    "Class Reminder",
                    message,
                    priority="high",
                    tags="class"
                )