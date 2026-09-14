import discord
import os
from dotenv import load_dotenv

# Se caargan las variables de entorno
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

# Los intents se instancian y son necesarios para ciertas acciones
intents = discord.Intents.default()
intents.message_content = True

# Se instancia el cliente para interactuar con el bot
client = discord.Client(intents=intents)

# Evento de conexión iniciada
@client.event
async def on_ready():
    print(f'Conectado como {client.user}')

# Evento de mensajes recibidos
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    # Log que comprueba que el mensaje enviado por el cliente ha sido recibido
    print(f"Mensaje recibido: {message.content}")

    # Comandos y respuestas
    if message.content.startswith("/saludar"):
        await message.channel.send("¡Hola!")

    if message.content.startswith("/redes"):
        await message.channel.send("Sígueme en mis redes como @DevEzro")
        
# Inicializa el TOKEN del bot del fichero .env
client.run(TOKEN)