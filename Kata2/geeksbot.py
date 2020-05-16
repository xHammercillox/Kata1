from telegram.ext import Updater, CommandHandler

def main():
    # Instanciamos el updater
    updater = Updater(token=open("./bot_token").read(), use_context=True)
    # Añadiendo un manejador al comando /start
    updater.dispatcher.add_handler(CommandHandler("start", start))

    # Añadir manejador para el comando /repite
    updater.dispatcher.add_handler(CommandHandler("repite", repite))

    #Añadir un manejador para el comando /suma
    updater.dispatcher.add_handler(CommandHandler("suma", suma))

    # Empezamos a pedir notificaciones a Telegram
    updater.start_polling()

    # Capturamos señales de parada
    updater.idle()

def start(update, context):
    update.message.reply_text("Hola soy un bot")

def repite(update, context):
    # Repite el mensaje que se ha puesto
    update.message.reply_text(update.message.text)

def suma(update, context):
    # args = [2, 2] Esto es la suma
    resultado = int(context.args[0]) + int(context.args[1])
    resultado = int(resultado)
    update.message.reply_text(int)("El resultado es: " +resultado)

main()