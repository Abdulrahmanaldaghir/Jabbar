import os
import tempfile
import PyPDF2
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext


TOKEN = 'your token'

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Send me a PDF file, and I will convert it to text for you!')

def pdf_to_text(file_path):
    with open(file_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        text = ''
        for page_num in range(len(pdf_reader.pages)):
            text += pdf_reader.pages[page_num].extract_text()
    return text


def process_pdf(update: Update, context: CallbackContext) -> None:
    file = context.bot.getFile(update.message.document.file_id)
    file_name = os.path.join(tempfile.gettempdir(), update.message.document.file_name)
    file.download(file_name)
    
    text = pdf_to_text(file_name)
    
    with tempfile.NamedTemporaryFile(mode='wb', delete=False) as temp_file:
        temp_file.write(text.encode('utf-8'))
    
    update.message.reply_document(document=open(temp_file.name, 'rb'))
    os.unlink(temp_file.name)



def main() -> None:
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.document & ~Filters.command, process_pdf))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
