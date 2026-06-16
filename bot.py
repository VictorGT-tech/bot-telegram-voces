import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from gtts import gTTS

TOKEN = os.environ.get("TOKEN")

def start(update: Update, context: CallbackContext):
    update.message.reply_text("👋 Hola! Soy tu bot de voces.\n\nMándame cualquier texto y te lo devuelvo en nota de voz.")

def texto_a_voz(update: Update, context: CallbackContext):
    texto = update.message.text
    update.message.reply_text("Generando audio... 🎙️")
    
    try:
        tts = gTTS(text=texto, lang='es')
        tts.save("audio.mp3")
        
        with open("audio.mp3", "rb") as audio:
            update.message.reply_audio(audio=audio)
        
        os.remove("audio.mp3")
    except Exception as e:
        update.message.reply_text(f"Error: {e}")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, texto_a_voz))
    
    print("Bot encendido...")
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
