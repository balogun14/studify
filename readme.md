# Student Schedule Manager

A Python application to manage academic schedules, reading assignments, and exam notifications for university students.

## Features

- **Class Schedule Management**
  - Track daily classes with time and location
  - Automated daily schedule notifications
  - Support for multiple courses per day

- **Reading List Management**
  - Organize reading assignments by course
  - Track due dates for readings
  - Associate readings with specific courses

- **Exam Tracking**
  - Record upcoming exams
  - Get notifications for exam dates
  - Track exam topics by course

- **Notification System**
  - Daily schedule summaries
  - Class reminders
  - Upcoming exam alerts

## Setup

1. Clone the repository:
```bash
git clone <repository-url>

cd student-schedule-manager
```

2. Create a virtual environment and install dependencies:
```bash

python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# or
.venv\Scripts\activate  # Windowspip install -r requirements.txtpython main.py
```

3. Run the application:
```bash
python main.py
```

## Usage
The system automatically seeds the database with:  
Course schedule
Reading assignments (3-month study plan)
Exam dates
Notifications are sent:  
Daily schedule summary at 7:00 AM
Class reminders every 20 minutes
Upcoming exam notifications

## Contributing
Contributions are welcome! Please refer to the [contribution guidelines](CONTRIBUTING.md) for detailed instructions.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) for more information.
```

# Output
```bash
$ python main.py
2021-09-01 07:00:00
Good morning! Here's your schedule for today:
1. Course: Math 101
   Time: 9:00 AM - 10:30 AM
   Location: Room 101
2. Course: History 101
    Time: 11:00 AM - 12:30 PM
    Location: Room 201
3. Course: English 101
    Time: 2:00 PM - 3:30 PM
    Location: Room 301
````


