---

# Introduction

This script connects to a live YouTube chat and automatically sends messages to a Character.ai chat based on the messages received in the live chat. It filters out messages containing certain blacklisted words to ensure only appropriate messages are sent. The script uses the Playwright library for browser automation and Pytchat for retrieving live chat messages.

<img width="452" alt="image" src="https://github.com/user-attachments/assets/29128c9d-6fd6-4368-b631-d050e922ebd7">


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

# IF YOU WANT TO SUPPORT ME
Ko-fi : https://ko-fi.com/xzeest

<img width="112" alt="image" src="https://github.com/user-attachments/assets/e9767543-a0cd-4a95-b89c-a38acd5c2d2d">

Trakteer : https://trakteer.id/xzeeest/tip?open=true

<img width="113" alt="image" src="https://github.com/user-attachments/assets/cb2618f6-a5d3-41cb-866f-e9d5faeeaf8b">

Streamlabs : https://streamlabs.com/xzeeest

<img width="110" alt="image" src="https://github.com/user-attachments/assets/27f5f15f-462e-49fe-b774-ccf3efb5cfc0">


---

- EVM ADDRESS: 0x491d7397212c55da8352d7733d2513393a362ae9
- SOLANA: 5MNBgtrsasfqenxb75ZLjd4epjB2TUKf9fbxfw143kq6
- BTC: bc1pts2fvykemcdyk2rg37al8chdc4uxptwg82w3nf0j02smzrtm9a6sp5dldc
- TON: UQCnGIFDBtrvJC9LtkcVa3SrkS3ifb2qZxZX3r-abZ-4GG1D

---

