import os
import telebot 

bot = telebot.TeleBot("5159478561:AAEvHPhc13F0Bb1yIBESxv4-uecpV52n-U8")

client.forward_messages(
    chat_id=chat_id,
    from_chat_id=message.chat.id,
    message_ids=message.message_id
)

bot.polling()
