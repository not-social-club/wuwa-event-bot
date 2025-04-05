import discord
import datetime
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
CANAL_ID = int(os.getenv("CANAL_ID")) 

intents = discord.Intents.default()
client = discord.Client(intents=intents)

# Formato data/hora (Nao coloque nas datas exemplo 03)- AA-MM-DD-HH-MM-SS 
eventos = [
    {
        "nome": "CANTARELLA & CAMELLYA",
        "inicio": datetime.datetime(2025, 3, 26, 22, 40, 0), 
        "fim": datetime.datetime(2025, 4, 17, 11, 59, 0),
    },
    {
        "nome": "Tower of Adversity: Hazard Zone",
        "inicio": datetime.datetime(2025, 3, 31, 5, 59, 0),
        "fim": datetime.datetime(2025, 4, 28, 5, 59, 0),
    },
    {
        "nome": "Whimpering Wastes",
        "inicio": datetime.datetime(2025, 3, 17, 5, 59, 0),
        "fim": datetime.datetime(2025, 4, 14, 5, 59, 0),
    },
    {
        "nome": "Fantasies of the Thousand Gateways",
        "inicio": datetime.datetime(2025, 3, 31, 5, 59, 0),
        "fim": datetime.datetime(2025, 4, 7, 5, 59, 0),
    },
    {
        "nome": "Virtual Crisis: Prototype Trials",
        "inicio": datetime.datetime(2025, 4, 3, 11, 59, 0),
        "fim": datetime.datetime(2025, 4, 28, 5, 59, 0),
    },
]

async def enviar_mensagem(channel):
    """Envia a mensagem com eventos ativos e futuros."""
    agora = datetime.datetime.utcnow()
    proximos_dias = agora + datetime.timedelta(days=7)

    embed = discord.Embed(
        title="Wuthering Waves - Eventos",  
        description="", # Linha vazia após o título
        color=0x007EB8
    )
    embed.set_image(url="https://i.imgur.com/exemplo.png") # Adicione imagem do banner
    embed.set_footer(text="Servidor: América")

    eventos_ativos = [evento for evento in eventos if evento["inicio"] <= agora <= evento["fim"]]
    if eventos_ativos:
        embed.add_field(name="**Eventos Ativos**", value="", inline=False)  # Linha vazia antes da lista
        for evento in eventos_ativos:
            timestamp_fim = int(evento["fim"].timestamp())
            embed.add_field(
                name=f"🔹 {evento['nome']}",
                value=f"Termina <t:{timestamp_fim}:R> (<t:{timestamp_fim}:f>)",
                inline=False
            )

    eventos_futuros = [evento for evento in eventos if agora < evento["inicio"] <= proximos_dias]
    if eventos_futuros:
        embed.add_field(name="\u200B", value="\u200B", inline=False)  # Linha vazia antes da seção "Eventos Futuros"
        embed.add_field(name="**Eventos Futuros**", value="", inline=False)
        for evento in eventos_futuros:
            timestamp_inicio = int(evento["inicio"].timestamp())
            embed.add_field(
                name=f"🔹 {evento['nome']}",
                value=f"Começa <t:{timestamp_inicio}:R> (<t:{timestamp_inicio}:f>)",
                inline=False
            )

    await channel.send(embed=embed)

@client.event
async def on_ready():
    print(f"✅ Bot {client.user} está online!")
    canal = client.get_channel(CANAL_ID)
    await enviar_mensagem(canal)

client.run(TOKEN)