---

# Introduction

This script connects to a live YouTube chat and automatically sends messages to a Character.ai chat based on the messages received in the live chat. It filters out messages containing certain blacklisted words to ensure only appropriate messages are sent. The script uses the Playwright library for browser automation and Pytchat for retrieving live chat messages.

---

# Features

- **Real-Time Chat Monitoring**: Monitors live chat messages from a specified YouTube video in real-time.
- **Blacklist Filtering**: Ignores messages containing any blacklisted words, ensuring only suitable messages are sent to Character.ai.
- **Automated Interaction**: Automatically fills in and sends messages to the Character.ai chat interface.
- **Customizable Input**: Allows users to specify the YouTube video ID and the textarea placeholder for sending messages.

---

# Getting Started

1. **Install Required Libraries**: You need to install the following libraries if you haven't already:
   - `playwright`
   - `pytchat`

   You can install these using pip:

   ```bash
   pip install playwright pytchat
   ```

   **Note**: After installing Playwright, you may need to run the following command to install the required browsers:

   ```bash
   playwright install
   ```

2. **Prepare the Blacklist**: Create a text file named `word-blacklist.txt` and list any words you want to filter out, one per line.

3. **Run the Script**:
   - Save the provided Python script to a file, for example, `live_chat_bot.py`.
   - Open your terminal or command prompt and navigate to the directory where your script is located.
   - Run the script with the command:

     ```bash
     python live_chat_bot.py
     ```

   - Follow the prompts to enter the YouTube video ID and the textarea placeholder for Character.ai.

4. **Interact with the Bot**: The script will start monitoring the live chat. Messages will be sent to the Character.ai chat as long as the script is running.

---
