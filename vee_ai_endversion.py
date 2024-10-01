from playwright.sync_api import sync_playwright
import pytchat
import time
import logging
from rich.console import Console
from rich.text import Text

# Inisialisasi console rich
console = Console()

# Menampilkan watermark di bagian awal
watermark_text = Text("LiveChat Youtube to Character.AI", style="bold blue")
author_text = Text("by: tobeoren", style="bold cyan")

console.print(watermark_text, justify="center")
console.print(author_text, justify="center")

# Konfigurasi logging
logging.basicConfig(level=logging.INFO)

# Fungsi untuk membaca kata blacklist dari file dengan encoding UTF-8
def load_blacklist(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            # Baca semua baris dan hapus spasi
            return [line.strip().lower() for line in file.readlines()]
    except FileNotFoundError:
        logging.error("Blacklist file not found!")
        return []
    except UnicodeDecodeError as e:
        logging.error("Error decoding the file: %s", e)
        return []

# Memasukkan video_id dan kata textarea secara manual
video_id = input("Masukkan YouTube video_id: ")  # Contoh: DZ0hf7sKP4g
textarea_placeholder = input("Masukkan kata dari textarea (contoh: 'Message Kaela Assistant'): ")

# Memuat kata-kata blacklist
blacklist = load_blacklist("word-blacklist.txt")

# Membuat koneksi ke live chat YouTube
chat = pytchat.create(video_id=video_id)

with sync_playwright() as p:
    logging.info("Launching browser...")
    # Pilih browser (Chrome)
    browser = p.chromium.launch(headless=False)  # headless=True untuk tidak menampilkan UI
    context = browser.new_context()  # Membuat konteks baru
    page = context.new_page()
    
    # Buka halaman Character.ai chat
    try:
        logging.info("Navigating to Character.ai...")
        page.goto("https://character.ai/chat/kjStETpL1jUBZL_cbxtHZWVbbJV-HoleFnRMiMlyXgo")
        page.wait_for_timeout(15000)  # Tunggu tambahan 15 detik untuk memastikan halaman dimuat
        
        logging.info("Waiting for the textarea...")
        # Mencari textarea menggunakan selector berdasarkan placeholder yang diinput
        chat_box = page.locator(f'textarea[placeholder="{textarea_placeholder}..."]')
        chat_box.wait_for(state='visible', timeout=60000)  # Tunggu hingga elemen terlihat

        while chat.is_alive():
            try:
                for c in chat.get().sync_items():
                    message = c.message.lower()  # Konversi pesan ke lowercase
                    author = c.author  # Ambil penulis pesan
                    timestamp = c.timestamp  # Ambil timestamp pesan

                    # Cek apakah pesan mengandung kata-kata dari blacklist
                    if any(word in message for word in blacklist):
                        logging.info("[%s] %s: Message ignored due to blacklist", timestamp, author)
                        continue  # Abaikan pesan jika mengandung kata blacklist

                    # Cetak pesan dari live chat ke konsol
                    logging.info("[%s] %s: %s", timestamp, author, message)

                    # Masukkan pesan ke Character.ai chat box menggunakan Playwright
                    chat_box.fill(message)  # Mengisi pesan
                    chat_box.press("Enter")  # Tekan Enter untuk mengirim pesan

                    time.sleep(2)  # Beri jeda sebelum kirim pesan selanjutnya
            except Exception as e:
                logging.error("Error occurred during message processing: %s", e)
                # Lanjutkan loop meski ada error
                continue
    except Exception as e:
        logging.error("Error occurred during setup: %s", e)
