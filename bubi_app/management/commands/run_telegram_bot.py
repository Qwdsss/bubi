from django.core.management.base import BaseCommand
import telebot
from bubi_app.models import StarWarsCharacter

bot = telebot.TeleBot("6728443148:AAG3vacjD9M2fW8I-7W0sxcpsSTxfgdDHyg")


@bot.message_handler(commands=['help'])
def help_command(message):
    help_message = "Commands:\n" \
                   "/start - Start the bot\n" \
                   "/SW - Get information about Star Wars characters\n" \
                   "/help - Display this help message"

    bot.send_message(message.chat.id, help_message)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет из мира Звездных войн!")


@bot.message_handler(commands=['SW'])
def star_wars_characters(message):
    characters = StarWarsCharacter.objects.all()
    for character in characters:
        affiliation_message = "Affiliation: "
        if character.jedi and not character.sith:
            affiliation_message += "Jedi"
        elif character.sith and not character.jedi:
            affiliation_message += "Sith"
        info_message = (
            f"Name: {character.name}\n"
            f"Species: {character.species}\n"
            f"Homeworld: {character.homeworld}\n"
            f"{affiliation_message}\n"
        )
        bot.send_message(message.chat.id, info_message) 


class Command(BaseCommand):
    def handle(self, *args, **options):
        print("Starting bot...")
        bot.polling()
        print("Bot stopped")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)
