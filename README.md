# **Introduction**
This Python script integrates Playwright and pytchat to facilitate the interaction between a YouTube live chat and the Character.ai chat interface. It allows users to manually input a YouTube video ID and a specific placeholder phrase for a textarea on Character.ai. The script is designed to monitor the live chat in real time, filter out messages based on a blacklist, and relay acceptable messages to the Character.ai chat.

# Features:
1. Real-Time Interaction: Using Playwright, it launches a browser session, navigates to the Character.ai chat interface, and listens for new messages from the specified YouTube live chat.
2.  The code is structured to provide a seamless user experience, facilitating the integration of chat features and enhancing engagement with viewers during live streams.
3. Blacklist Filtering: The script reads a list of prohibited words from a file and ignores any live chat messages that contain these words.
4. Error Handling: Comprehensive logging and error handling mechanisms ensure the script runs smoothly, reporting any issues encountered during execution.

# How it Works:
This script connects YouTube live chat with the Character.ai chat interface. Here’s how it works:

1. Importing Libraries:
The script uses Playwright to automate the browser and pytchat to access YouTube live chat. The time and logging libraries are used for time management and logging activities.
2. Logging Configuration:
The script sets up logging to display messages in the console, helping to monitor the script's execution and capture any errors.
3. Loading the Blacklist:
The load_blacklist function reads prohibited words from a file (word-blacklist.txt) and stores them in a list. If the file is not found, an error message is logged.
4. User Input:
The script prompts the user to enter the YouTube video ID and a placeholder phrase for the textarea in Character.ai, allowing flexible configuration.
5. Connecting to YouTube Live Chat:
The script establishes a connection to the YouTube live chat using the provided video ID.
6. Launching the Browser:
Using Playwright, the script launches a Chromium browser, which can run in headless mode (without UI) or with a visible UI, depending on the user's preference.
7. Navigating to Character.ai:
The script opens the Character.ai URL and waits for the page to load completely. It then searches for the textarea element based on the user-defined placeholder.
8. Listening for Live Chat Messages:
The script checks for new messages from the YouTube live chat. Each message is checked for prohibited words:
9. If the message contains any blacklisted words, it is ignored and logged.
If not, the message is printed to the console and filled into the Character.ai textarea to be sent.
10. Error Handling:
Any errors that occur during setup or message processing are captured and logged, ensuring the script continues running smoothly even if issues arise.
11. Sleep Interval:
After sending a message, the script pauses for 2 seconds before processing the next message to make interactions feel more natural.

Through these steps, the script facilitates communication between YouTube live chat and the Character.ai platform, enhancing viewer interaction during live streams.

# Getting Started
To use this script, follow these steps to set up your environment and run the program:

1. **Install Required Libraries**:  
   Make sure you have Python installed on your computer. Then, install the necessary libraries using pip. Open your terminal or command prompt and run:
   ```bash
   pip install playwright pytchat
   ```
   After that, install the browser binaries for Playwright:
   ```bash
   playwright install
   ```

2. **Create the Blacklist File**:  
   Create a text file named `word-blacklist.txt` in the same directory as your script. Add any words you want to block (one word per line). For example:
   ```
   badword1
   badword2
   forbidden
   ```

3. **Prepare Your Script**:  
   Copy the provided code into a Python script file (e.g., `chat_integration.py`). Make sure the script is in the same directory as the `word-blacklist.txt` file.

4. **Run the Script**:  
   Open your terminal or command prompt, navigate to the directory where your script is located, and run:
   ```bash
   python chat_integration.py
   ```
   The script will prompt you to enter the YouTube **video ID** and the **textarea placeholder**. For example:
   - YouTube video ID: `DZ0hf7sKP4g`
   - Textarea placeholder: `Message Kaela Assistant`

5. **Interact with YouTube Live Chat**:  
   Once you enter the required information, the script will launch a browser window. It will connect to the specified YouTube live chat and the Character.ai chat interface. You will see messages from the YouTube live chat relayed to Character.ai, with any blacklisted messages ignored.

6. **Stop the Script**:  
   To stop the script, you can close the browser window or interrupt the script in the terminal using `Ctrl + C`.

### Important Notes
- Ensure that you have a stable internet connection while running the script.
- The script is designed for live chats; it may not work properly with regular video comments.
- Adjust the blacklist words in the `word-blacklist.txt` file as needed to suit your preferences.

By following these steps, you should be able to set up and run the script successfully, enabling interaction between YouTube live chat and Character.ai!

Remember to use the bot responsibly and respect the YouTube community guidelines when using it during live streams. Enjoy engaging with your audience in a more interactive and accessible way!
