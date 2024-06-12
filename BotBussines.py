from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Tu token de API de BotFather
TOKEN = '7356540491:AAHILvk8Aq6ENmjeX2cDlc2taHbpUH19Onk'

# Función para iniciar el bot y mostrar el teclado
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        ["Ventas Mensuales", "Clientes Activos"],
        ["Inventario Actual", "Desempeño por Región"],
        ["Proyecciones de Ventas", "Soporte al Cliente"]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True, resize_keyboard=True)
    await update.message.reply_text('Elige una opción para obtener información:', reply_markup=reply_markup)

# Función para manejar la respuesta del usuario
async def handle_response(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_response = update.message.text
    if user_response == "Ventas Mensuales":
        await update.message.reply_text("Las ventas mensuales actuales son de $100,000.")
        await update.message.reply_text("Te puedo ayudar en algo más? Elige una opcion")
    elif user_response == "Clientes Activos":
        await update.message.reply_text("Actualmente tenemos 1,200 clientes activos.")
        await update.message.reply_text("Te puedo ayudar en algo más? Elige una opcion")
    elif user_response == "Inventario Actual":
        await update.message.reply_text("El inventario actual es de 5,000 unidades.")
        await update.message.reply_text("Te puedo ayudar en algo más? Elige una opcion")
    elif user_response == "Desempeño por Región":
        await update.message.reply_text("El mejor desempeño es en la región Norte con un 25% de aumento en ventas.")
        await update.message.reply_text("Te puedo ayudar en algo más? Elige una opcion")
    elif user_response == "Proyecciones de Ventas":
        await update.message.reply_text("Se proyecta un crecimiento del 10% en ventas para el próximo trimestre.")
        await update.message.reply_text("Te puedo ayudar en algo más? Elige una opcion")
    elif user_response == "Soporte al Cliente":
        await update.message.reply_text("El tiempo de respuesta promedio en soporte al cliente es de 2 horas.")
        await update.message.reply_text("Te puedo ayudar en algo más? Elige una opcion")
    else: 
        await update.message.reply_text("L o siento, no entiendo tu respuesta. Por favor, elige una opción del menú.")

def main():
    # Crear la aplicación
    application = Application.builder().token(TOKEN).build()

    # Añadir manejadores para los comandos
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_response))

    # Iniciar el bot
    application.run_polling()

if __name__ == '__main__':
    main()
