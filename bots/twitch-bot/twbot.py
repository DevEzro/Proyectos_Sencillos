import os
import asyncio
import random
from dotenv import load_dotenv # get .env values
from twitchio.ext import commands

load_dotenv()

class MiBot(commands.Bot):

    # INICIALIZACIÓN
    def __init__(self):
        super().__init__(
            token=os.environ['TWITCH_TOKEN'],
            client_id=os.environ['TWITCH_CLIENT_ID'],
            nick='My Twitch Bot',
            prefix='!',
            initial_channels=['ChannelName']
        )

    # DIAGNÓSTICO
    async def event_ready(self):
        print(f'✅ Conectado a Twitch como {self.nick}!')

    # OBTIENE MENSAJE DEL CHAT Y USUARIO
    async def event_message(self, message):
        if message.echo:
            return

        print(f"📩 [{message.channel.name}] {message.author.name}: {message.content}")
        
        #region Ejemplo: DETECTA UNA PALABRA
        if "palabra" in message.content.lower():
            await message.channel.send(f'@{message.author.name} ha dicho la palabra')
        #endregion
        
        await self.handle_commands(message)

    # COMANDOS CON !
    # Si escribe !test en el chat, aparece el memsaje del await mencionando al usuario que lo escribió
    @commands.command(name='test')
    async def test_command(self, ctx: commands.Context):
        print("🤖 Comando !test detectado")
        await ctx.send(f'¡Hola @{ctx.author.name}! El bot funciona perfectamente. 🚀')   

# ARRANCA EL BOT
async def main():
    bot = MiBot()
    await bot.start()

if __name__ == '__main__':
    asyncio.run(main())