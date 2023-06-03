token = '5911425335:AAGPzUr8bJSIsxjn5ld8OCzEGT7gxwgbsc8'

from typing import Final
from telegram import Bot
import imagen
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
from telegram.ext import CallbackContext



# pip install python-telegram-bot
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes


print('Arrancando bot...')

TOKEN: Final = '5911425335:AAGPzUr8bJSIsxjn5ld8OCzEGT7gxwgbsc8'
BOT_USERNAME: Final = '@mrbytesadminbot'




# Lets us use the /start command
async def start_command(update: Update, context: CallbackContext):
    message = 'Bienvenido, MrBytesbot a la Orden! 😄\n\nHaz clic en un botón:'

    button_info = InlineKeyboardButton('Información', callback_data='info')
    button_info2 = InlineKeyboardButton('Quienes somos', callback_data='info2')
    keyboard = InlineKeyboardMarkup([[button_info], [button_info2]])

    await update.message.reply_text(text=message, reply_markup=keyboard)


async def button_info_callback2(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    if query.data == 'info':
        message = 'Aquí tienes la información que buscas.' \
                  ' \nPara ver todos los catalogos del menu ingrese el comando /producto ' \
                  ' \nPara ver todos los catalogos del segundo menu ingrese el comando /producto2 ' \
                  ' \nPara ver todos los catalogos del tercer menu ingrese el comando /producto3 ' \
                  ' \nPara ver todos los catalogos del cuarto menu ingrese el comando /producto4 ' \
                  ' \nPara ver todos los catalogos del quinto menu ingrese el comando /producto5 ' \
                  '\n Por si tiene alguna inconveniencia ingrese /help para ayudarlo'

        await query.message.reply_text(text=message)
    elif query.data == 'info2':
        image_url = 'https://img.freepik.com/vector-premium/diseno-logotipo-panaderia-retro-hornear-pasteleria_434503-542.jpg?w=740'
        message = 'The Bread es una empresa dedicada a la venta de pastelitos y panes.'
        await query.message.reply_photo(photo=image_url)
        await query.message.reply_text(text=message)



# Lets us use the /help command
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hola te saluda MrBytesbot, Como te ayudamos?,'
                                   'Por el momento solo reconozco los siguientes comandos : '
                                   ' /start ------------ Visualizar el menu de catalogos '
                                   ' /need  -------------Necesitas informacion ¿? '
                                   ' /custom  ------------- Comando podemos agregar cualquier texto  '
                                   ' /producto  -------------Ver el catalogo de la empresa y sus precios del menu'
                                   ' /producto2  -------------Ver el segundo catalogo de la empresa y sus precios del menu'
                                   ' /producto3  -------------Ver el tercer catalogo de la empresa y sus precios del menu'
                                   ' /producto4  -------------Ver el cuarto catalogo de la empresa y sus precios del menu'
                                   ' /producto5  -------------Ver el quinto catalogo de la empresa y sus precios del menu'
                                    '\nPara contactarse con el proveedor llame al 46905447')

# Comando need
async def need_command(update, context):
    await update.message.reply_text('Me han creado para ayudarte con tus dudas, ☺ '
                                   'por ahora no puedo entender emojis, stickers, imagenes '
                                   'selecciona el comando /start para regresar al inicio Gracias !!')

# Lets us use the /custom command
async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Este es un comando personalizado, puede agregar el texto que desee aquí.')



def handle_response(text: str) -> str:
    # Create your own response logic
    processed: str = text.lower()

    if 'hola' in processed:
        return 'Que onda!'

    if 'Hola' in processed:
        return 'Que onda!'

    if 'buenos dias' in processed:
        return 'Buenos dias ☺!'


    if 'buenas tardes' in processed:
        return 'Buenas tardes ☺!'

    if 'buenas noches' in processed:
        return 'Buenas noches ☺!'

    if 'que tal estas' in processed:
        return 'Estoy bien!'

    if 'que tal' in processed:
        return 'bien y tu? ☺!'

    if 'te amo' in processed:
        return 'Yo tambien ♥!'

    if 'necesito ayuda' in processed:
        return 'Para consultar informacion, ingrese el comando /help, le aparecerá informacion que necesite!'

    if 'jajaja' in processed:
        return 'Por que te ries???'

    if 'ayuda' in processed:
        return 'Si necesitas ayuda, ingresa el comando /help, tendrás mucha información'

    if 'quiero informacion de los precios' in processed:
        return 'Ingresa a los catalogos de los productos iniciando con: /producto, /producto 2, /producto3, para ver los menus'

    if 'muestra el menu' in processed:
        return 'Aquí tienes la información que buscas.' \
                  ' \nPara ver todos los catalogos del menu ingrese el comando /producto ' \
                  ' \nPara ver todos los catalogos del segundo menu ingrese el comando /producto2 ' \
                  ' \nPara ver todos los catalogos del tercer menu ingrese el comando /producto3 ' \
                  ' \nPara ver todos los catalogos del cuarto menu ingrese el comando /producto4 ' \
                  ' \nPara ver todos los catalogos del quinto menu ingrese el comando /producto5 ' \
                  '\n Por si tiene alguna inconveniencia ingrese /help para ayudarlo'

    if 'muestra un video' in processed:
        return 'Aquí tienes: https://www.youtube.com/watch?v=rdBfwUjxO_E&ab_channel=AleHervi.'

    if 'quiero hacer un pastel' in processed:
        return 'Esto te puede gustar ☺: https://www.youtube.com/watch?v=yhLXmwEBZnU&ab_channel=PostresBeatrizFigueroa.'

    if 'dame recetas' in processed:
        return 'Esto te puede llamar la atención ☺: https://www.recetasgratis.net/receta-de-pastel-sencillo-de-vainilla-43470.html.'

    if 'adios' in processed:
        return 'Adios, cuídate, espero que te haya gustado mi servicio ☺.'

    return 'No entiendo'


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Get basic info of the incoming message
    message_type: str = update.message.chat.type
    text: str = update.message.text

    # Print a log for debugging
    print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')

    # React to group messages only if users mention the bot directly
    if message_type == 'group':
        # Replace with your bot username
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            response: str = handle_response(new_text)
        else:
            return  # We don't want the bot respond if it's not mentioned in the group
    else:
        response: str = handle_response(text)

    # Reply normal if the message is in private
    print('Bot:', response)
    await update.message.reply_text(response)


# Función para el comando /producto
async def producto_command(update, context):
    await update.message.reply_text('Aquí tiene un vistazo al catalogo de que lo ofrece todo el menú:')
    products = [
        {"name": "Criollos Panecitos", "price": "Q25", "image_url": "https://img-global.cpcdn.com/recipes/09ed2d0c0b52fd84/640x640sq70/photo.webp"},
        {"name": "Combo de pastelitos de crema", "price": "Q40", "image_url": "http://blog.cosasderegalo.com/wp-content/uploads/2013/05/pastelitos-merengue-menu-recetas.jpg"},
        {"name": "Tazon de empanadas", "price": "Q35", "image_url": "https://quierocakes.com/wp-content/uploads/2019/02/pastelitos.jpg"},
        {"name": "Pastelitos Venezolanos", "price": "Q20", "image_url": "https://comidasvenezolanas.org/wp-content/uploads/2021/02/pastelitos-venezolanos_700x466.jpg"},
        {"name": "Empanadas de pollo", "price": "Q20", "image_url": "https://d1kxxrc2vqy8oa.cloudfront.net/wp-content/uploads/2019/11/02125135/RFB-3110-3-masadepastelitos.jpg"},
        {"name": "Calzones de jamon y queso", "price": "Q15", "image_url": "https://comidahonduras.com/wp-content/uploads/2022/07/pastelitos-jamon-queso-Comidahonduras-800x530.jpg"},
        {"name": "Pastelito de chocolate", "price": "Q10", "image_url": "https://4.bp.blogspot.com/-MbyGZ4b22B0/VMB_NHUM66I/AAAAAAAACFY/qIzy5YGJCP8/s1600/Chocolate%2BCupcakes%2BSyS2.jpg"},
        {"name": "Pastelitos Andinos", "price": "Q40", "image_url": "https://comidasvenezolanas.org/wp-content/uploads/2021/01/pastelitos-andinos_700x466.jpg"},
        {"name": "Pan con pollo", "price": "Q25", "image_url": "https://www.recetassalvador.com/base/stock/Recipe/38-image/38-image_web.jpg"},
        {"name": "Pan con chile", "price": "Q28", "image_url": "https://media-cdn.tripadvisor.com/media/photo-s/0f/91/da/a5/pan-con-chile-relleno.jpg"}
    ]
    bot = Bot(token=context.bot.token)

    for product in products:
        image_url = product["image_url"]
        caption = f"{product['name']} - {product['price']}"

        # Crear el botón para agregar a la lista de compra
        keyboard = InlineKeyboardMarkup(
            [[InlineKeyboardButton("Agregar a la lista de compra", callback_data=f"add_to_cart_{product['name']}")]])

        # Enviar la foto con el botón y la leyenda
        await bot.send_photo(chat_id=update.effective_chat.id, photo=image_url, caption=caption, reply_markup=keyboard)

    # Manejar los callbacks de los botones
    app.add_handler(CallbackQueryHandler(add_to_cart_callback))


# Función para manejar los callbacks de los botones
def add_to_cart_callback(update, context):
    query = update.callback_query
    product_name = query.data.split("_", 2)[2]  # Obtener el nombre del producto desde el callback_data
    user_id = query.from_user.id

    # Aquí puedes implementar la lógica para agregar el producto a la lista de compra del usuario

    # Enviar una respuesta al callback
    query.answer(text="Producto agregado a la lista de compra")

# Función para el comando /producto2
async def producto2_command(update, context):
    await update.message.reply_text('Aquí tiene un vistazo al segundo catalogo de que lo ofrece todo el menú:')
    products = [
        {"name": "Pastel de fresas con crema", "price": "Q100", "image_url": "https://storage.googleapis.com/patsy-ecommerce.appspot.com/small_FRESAS_CON_CREMA_6bb4f36558"},
        {"name": "Pastel selva negra", "price": "Q130", "image_url": "https://storage.googleapis.com/patsy-ecommerce.appspot.com/small_SELVA_NEGRA_1964333182"},
        {"name": "Pie de queso y piña colada", "price": "Q135", "image_url": "https://storage.googleapis.com/patsy-ecommerce.appspot.com/small_3_ab13793c36"},
        {"name": "Pie de queso mango y piña", "price": "Q120", "image_url": "https://storage.googleapis.com/patsy-ecommerce.appspot.com/small_1_330dc2313f"},
        {"name": "Pie de queso, frambuesa y chocolate blanco", "price": "Q120", "image_url": "https://storage.googleapis.com/patsy-ecommerce.appspot.com/small_4_14cec30bc0"},
        {"name": "Pie de queso y mermelada berries", "price": "Q150", "image_url": "https://storage.googleapis.com/patsy-ecommerce.appspot.com/small_2_027b972668"},
        {"name": "Pastel fresa melocotón", "price": "Q140", "image_url": "https://storage.googleapis.com/patsy-ecommerce.appspot.com/small_FRESA_MELO_2a4a35bccc"},
        {"name": "Pastel chocolate con frutas", "price": "Q240", "image_url": "https://storage.googleapis.com/patsy-ecommerce.appspot.com/small_PASTEL_CHOCOLATE_CON_FRUTAS_7a7aa83fc0"},
        {"name": "Pastel brownie y cajeta", "price": "Q250", "image_url": "https://storage.googleapis.com/patsy-ecommerce.appspot.com/small_BROWNIE_CAJETA_6214f268a4"},
        {"name": "Pastel chocoflan", "price": "Q200", "image_url": "https://storage.googleapis.com/patsy-ecommerce.appspot.com/PASTEL_CHOCOFLAN_copia_f2b4acfd3b"}
    ]

    bot = Bot(token=context.bot.token)

    for product in products:
        image_url = product["image_url"]
        caption = f"{product['name']} - {product['price']}"

        # Crear el botón para agregar a la lista de compra
        keyboard = InlineKeyboardMarkup(
            [[InlineKeyboardButton("Agregar a la lista de compra", callback_data=f"add_to_cart_{product['name']}")]])

        # Enviar la foto con el botón y la leyenda
        await bot.send_photo(chat_id=update.effective_chat.id, photo=image_url, caption=caption, reply_markup=keyboard)

    # Manejar los callbacks de los botones
    app.add_handler(CallbackQueryHandler(add_to_cart_callback))


# Función para manejar los callbacks de los botones
def add_to_cart_callback(update, context):
    query = update.callback_query
    product_name = query.data.split("_", 2)[2]  # Obtener el nombre del producto desde el callback_data
    user_id = query.from_user.id

    # Aquí puedes implementar la lógica para agregar el producto a la lista de compra del usuario

    # Enviar una respuesta al callback
    query.answer(text="Producto agregado a la lista de compra")

# Función para el comando /producto3
async def producto3_command(update, context):
    await update.message.reply_text('Aquí tiene un vistazo al tercer catalogo de que lo ofrece todo el menú:')
    products = [
        {"name": "Sablé de chocolate chips", "price": "Q7", "image_url": "https://www.lecafeguatemala.com/_uploads/menus/imgs/full/336.jpg"},
        {"name": "Espumillas", "price": "Q16", "image_url": "https://www.lecafeguatemala.com/_uploads/menus/imgs/full/491-20230202143638.jpg"},
        {"name": "Chocolate negro", "price": "Q21", "image_url": "https://www.lecafeguatemala.com/_uploads/menus/imgs/full/407.jpg"},
        {"name": "Toscano", "price": "Q72", "image_url": "https://www.lecafeguatemala.com/_uploads/menus/imgs/full/79.png"},
        {"name": "Sandwich simple", "price": "Q15", "image_url": "https://static.wixstatic.com/media/6b5508_5293130da7294cf3b30da0da4bcfe267.jpg/v1/fill/w_267,h_400,al_c,q_80,enc_auto/6b5508_5293130da7294cf3b30da0da4bcfe267.jpg"},
        {"name": "Limonada", "price": "Q12", "image_url": "https://static.wixstatic.com/media/6b5508_09162d61db89464196aed53af6173989.jpg/v1/fill/w_704,h_528,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/6b5508_09162d61db89464196aed53af6173989.jpg"},
        {"name": "Tostaditas con chile", "price": "Q10", "image_url": "https://static.wixstatic.com/media/6b5508_c3f04ad1ae80426d892e942219c9c96a~mv2.jpg/v1/fill/w_470,h_490,al_c,q_80,usm_0.66_1.00_0.01,enc_auto/6b5508_c3f04ad1ae80426d892e942219c9c96a~mv2.jpg"},
        {"name": "Panitos locos", "price": "Q15", "image_url": "https://static.wixstatic.com/media/6b5508_2add2fd4a6df4311b493ad6fe0980b6b~mv2.jpg/v1/fill/w_871,h_490,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/6b5508_2add2fd4a6df4311b493ad6fe0980b6b~mv2.jpg"},
        {"name": "Hamburguesa de queso", "price": "Q35", "image_url": "https://ds1e83w8pn0gs.cloudfront.net/fotosmultisite/51734-1.jpg"},
        {"name": "Galleta Polvorones", "price": "Q22", "image_url": "https://ds1e83w8pn0gs.cloudfront.net/fotosmultisite/1121-1.jpg"}
    ]

    for product in products:
        image_url = product["image_url"]
        caption = f"{product['name']} - {product['price']}"
        button = InlineKeyboardButton(
            text="Agregar a la lista de compra",
            callback_data=f"add_to_cart_{product['name']}"
        )
        reply_markup = InlineKeyboardMarkup([[button]])
        await context.bot.send_photo(chat_id=update.effective_chat.id, photo=image_url, caption=caption,
                                     reply_markup=reply_markup)


async def button_callback(update, context):
    query = update.callback_query
    query.answer()

    if query.data.startswith("add_to_cart_"):
        product_name = query.data.split("_", 2)[2]
        # Aquí puedes realizar la lógica para agregar el producto a la lista de compra
        await query.message.reply_text(f"Producto '{product_name}' agregado a la lista de compra.")
    else:
        await query.message.reply_text("Opción inválida.")

# Función para el comando /producto4
async def producto4_command(update, context):
    await update.message.reply_text('Aquí tiene un vistazo al cuarto catalogo de que lo ofrece todo el menú:')
    products = [
        {"name": "Galleta Alfajores", "price": "Q30", "image_url": "https://ds1e83w8pn0gs.cloudfront.net/fotosmultisite/1438-1.jpg"},
        {"name": "Cinnamon Roll 5 Unidades", "price": "Q40", "image_url": "https://ds1e83w8pn0gs.cloudfront.net/fotosmultisite/4494-1.jpg"},
        {"name": "Pastelito de Nutella y Banano", "price": "Q14", "image_url": "https://ds1e83w8pn0gs.cloudfront.net/fotosmultisite/3997-1.jpg"},
        {"name": "Sourdough de Centeno", "price": "Q20", "image_url": "https://ds1e83w8pn0gs.cloudfront.net/fotosmultisite/5208-1.jpg"},
        {"name": "Coffee Snaps con Chocolate", "price": "Q36", "image_url": "https://ds1e83w8pn0gs.cloudfront.net/fotosmultisite/8263-1.jpg"}
    ]
    bot = Bot(token=context.bot.token)

    for product in products:
        image_url = product["image_url"]
        caption = f"{product['name']} - {product['price']}"

        # Crear el botón para agregar a la lista de compra
        keyboard = InlineKeyboardMarkup(
            [[InlineKeyboardButton("Agregar a la lista de compra", callback_data=f"add_to_cart_{product['name']}")]])

        # Enviar la foto con el botón y la leyenda
        await bot.send_photo(chat_id=update.effective_chat.id, photo=image_url, caption=caption, reply_markup=keyboard)

    # Manejar los callbacks de los botones
    app.add_handler(CallbackQueryHandler(add_to_cart_callback))

async def producto5_command(update, context):
    await update.message.reply_text('Aquí tiene un vistazo al quinto catalogo de que lo ofrece todo el menú:')
    products = [
        {"name": "Cold Brew Latte", "price": "Q15", "image_url": "https://dea154aeb528bee620f5-799733fd03b9298a9f65fee6178f3d08.ssl.cf1.rackcdn.com/pix_16_100263_2000_5f91926354436.jpg"},
        {"name": "Capuchino", "price": "Q20", "image_url": "https://upload.wikimedia.org/wikipedia/commons/0/00/Cappuccino_PeB.jpg"},
        {"name": "Capuchino con chocolate", "price": "Q25", "image_url": "https://cdn0.recetasgratis.net/es/posts/2/4/2/capuchino_16242_600.webp"},
        {"name": "Capuccino frappé", "price": "Q19", "image_url": "https://cdn0.recetasgratis.net/es/posts/2/9/8/capuccino_frappe_56892_600.webp"},
        {"name": "Café frappe con Thermomix", "price": "Q28", "image_url": "https://cdn0.recetasgratis.net/es/posts/0/0/5/cafe_frappe_con_thermomix_30500_600.webp"}
    ]
    bot = Bot(token=context.bot.token)

    for product in products:
        image_url = product["image_url"]
        caption = f"{product['name']} - {product['price']}"

        # Crear el botón para agregar a la lista de compra
        keyboard = InlineKeyboardMarkup(
            [[InlineKeyboardButton("Agregar a la lista de compra", callback_data=f"add_to_cart_{product['name']}")]])

        # Enviar la foto con el botón y la leyenda
        await bot.send_photo(chat_id=update.effective_chat.id, photo=image_url, caption=caption, reply_markup=keyboard)

    # Manejar los callbacks de los botones
    app.add_handler(CallbackQueryHandler(add_to_cart_callback))

# Log errors
async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')


# Run the program
if _name_ == '_main_':
    app = Application.builder().token(TOKEN).build()

    # Commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('custom', custom_command))
    app.add_handler(CommandHandler('producto', producto_command))
    app.add_handler(CommandHandler('producto2', producto2_command))
    app.add_handler(CommandHandler('producto3', producto3_command))
    app.add_handler(CommandHandler('producto4', producto4_command))
    app.add_handler(CommandHandler('producto5', producto5_command))
    app.add_handler(CommandHandler('need', need_command))
    app.add_handler(CallbackQueryHandler(button_callback))

    # Registrar el manejador de comandos y el manejador de la acción del botón
    app.add_handler(CallbackQueryHandler(button_info_callback2, pattern='info'))
    #
    app.add_handler(CallbackQueryHandler(button_info_callback2, pattern='info2'))

    # Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Log all errors
    app.add_error_handler(error)


    print('Polling...')
    # Run the bot
    app.run_polling(poll_interval=5)