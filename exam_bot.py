import os
import urllib.parse
import urllib.request
import feedparser

# Load credentials securely from environment variables
TELEGRAM_BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")

FEED_URL = "https://google.com"

def send_telegram_message(message):
    """Sends a formatted message to your Telegram bot."""
    encoded_message = urllib.parse.quote_plus(message)
    url = f"https://telegram.org{TELEGRAM_BOT_TOKEN}/sendMessage?chat_id={TELEGRAM_CHAT_ID}&text={encoded_message}&parse_mode=Markdown"
    try:
        urllib.request.urlopen(url)
    except Exception as e:
        print(f"❌ Failed to send message: {e}")

def get_exam_updates():
    feed = feedparser.parse(FEED_URL)
    
    if not feed.entries:
        print("No updates found.")
        return

    # Compile the top 5 updates into one single text block
    telegram_text = "🔔 *Latest Government Exam Updates* 🔔\n\n"
    
    for index, entry in enumerate(feed.entries[:5], start=1):
        # Cleans up the title for cleaner reading
        title = entry.title.split(" - ")[0] 
        telegram_text += f"{index}. 📌 *{title}*\n🔗 [Read More]({entry.link})\n\n"
    
    # Send the combined message to Telegram
    send_telegram_message(telegram_text)
    print("✅ Updates sent to Telegram successfully!")

if __name__ == "__main__":
    get_exam_updates()
