# Python Automation GUI for Web Task Simulation (Instagram Use Case)

This project demonstrates a custom-built Python application that automates web interaction (liking Instagram reels) using a graphical user interface (GUI) built with `CustomTkinter`. The automation logic utilizes `PyAutoGUI` for simulating human-like browser activity.

> 💡 This project showcases desktop automation, GUI development, and multithreading—all relevant skills for entry-level roles in data analysis, scripting, and workflow automation.

---

## 📌 Features

- 🔳 **CustomTkinter GUI**: Clean, responsive, dark-themed user interface.
- ⏯️ **Start/Stop Controls**: Easy control of automation via buttons.
- 🔁 **Threaded Execution**: Keeps the GUI responsive while the automation runs in background.
- 🔄 **Scroll & Click Simulation**: Automatically interacts with browser elements.
- 📊 **Progress Feedback**: Displays progress using a real-time progress bar.

---

## 🛠️ Technologies Used

| Tool/Library     | Purpose                              |
|------------------|--------------------------------------|
| `Python`         | Core programming language            |
| `customtkinter`  | UI/UX design                         |
| `pyautogui`      | Mouse and keyboard automation        |
| `threading`      | Background execution                 |
| `time`           | Delay and synchronization            |

---

## 🚀 How It Works

1. User inputs the number of Instagram reels they want to like.
2. On clicking **Start**, the app opens Chrome and navigates to `instagram.com/reels`.
3. The bot simulates likes and scrolls through reels one by one.
4. The user can stop the automation anytime using the **Stop** button.

> ⚠️ Coordinates for click actions (`pg.click(x, y)`) are hard-coded and may need adjustment based on screen resolution.

---

## 📷 Demo Preview

> Coming soon — GIF/video showcasing the automation in action.

---

## 🔧 Setup Instructions

### Prerequisites

- Python 3.8+
- Chrome browser installed
- Instagram account logged in on browser

### Installation

```bash
# Clone the repository
git clone https://github.com/your-username/web-task-simulation-bot.git
cd web-task-simulation-bot

# Install dependencies
pip install customtkinter pyautogui
