import os
import discord
from discord.ext import commands
from discord import app_commands

from dotenv import load_dotenv
import os

load_dotenv()  # โหลดไฟล์ .env

TOKEN = os.getenv('TOKEN')
print(f'TOKEN: {TOKEN}')  # ตรวจสอบค่าของ TOKEN


from myserver import server_on

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())



# //////////////////// Bot Event /////////////////////////
# คำสั่ง bot พร้อมใช้งานแล้ว
@bot.event
async def on_ready():
    print("Bot Online!")
    print("555")
    synced = await bot.tree.sync()
    print(f"{len(synced)} command(s)")




# แจ้งคนเข้า -ออกเซิฟเวอร์

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(1279026726323880038) # IDห้อง
    text = f"Welcome to the server, {member.mention}!"

    emmbed = discord.Embed(title = 'Welcome to the server!',
                           description = text,
                           color = 0x66FFFF)

    await channel.send(text) # ส่งข้อความไปที่ห้องนี้
    await channel.send(embed = emmbed)  # ส่ง Embed ไปที่ห้องนี้
    await member.send(text) # ส่งข้อความไปที่แชทส่วนตัวของ member


@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(1140633489520205934)  # IDห้อง
    text = f"{member.name} has left the server!"
    await channel.send(text)  # ส่งข้อความไปที่ห้องนี้



# คำสั่ง chatbot
@bot.event
async def on_message(message):
    mes = message.content # ดึงข้อความที่ถูกส่งมา
    if mes == 'hello':
        await message.channel.send("Hello It's me") # ส่งกลับไปที่ห้องนั่น

    elif mes == 'hi bot':
        await message.channel.send("Hello, " + str(message.author.name))

    await bot.process_commands(message)
    # ทำคำสั่ง event แล้วไปทำคำสั่ง bot command ต่อ




# ///////////////////// Commands /////////////////////
# กำหนดคำสั่งให้บอท

@bot.command()
async def hello(ctx):
    await ctx.send(f"hello {ctx.author.name}!")


@bot.command()
async def test(ctx, arg):
    await ctx.send(arg)


# Slash Commands
@bot.tree.command(name='hellobot', description='Replies with Hello')
async def hellocommand(interaction):
    await interaction.response.send_message("Hello It's me BOT DISCORD")


@bot.tree.command(name='name')
@app_commands.describe(name = "What's your name?")
async def namecommand(interaction, name : str):
    await interaction.response.send_message(f"Hello {name}")


# Embeds

@bot.tree.command(name='help', description='Bot Commands')
async def helpcommand(interaction):
    emmbed = discord.Embed(title='Help Me! - Bot Commands',
                           description='Bot Commands',
                           color=0x66FFFF,
                           timestamp= discord.utils.utcnow())


    # ใส่ข้อมูล
    emmbed.add_field(name='/hello1', value='Hello Commmand', inline=True)
    emmbed.add_field(name='/hello2', value='Hello Commmand', inline=True)
    emmbed.add_field(name='/hello3', value='Hello Commmand', inline=False)

    emmbed.set_author(name='Author', url='https://www.youtube.com/@zigzozay', icon_url='https://cdn.discordapp.com/attachments/656703700663926815/1278526554053414973/IMG_3116.png?ex=66d31a64&is=66d1c8e4&hm=bc5eb4a4424f3712a22099388091c981f6823ac3b0b3fa118972aacc6f39f44c&')

    # ใส่รูปเล็ก-ใหญ่
    emmbed.set_thumbnail(url='https://cdn.discordapp.com/attachments/656703700663926815/1278526554053414973/IMG_3116.png?ex=66d31a64&is=66d1c8e4&hm=bc5eb4a4424f3712a22099388091c981f6823ac3b0b3fa118972aacc6f39f44c&')
    emmbed.set_image(url='https://cdn.discordapp.com/attachments/656703700663926815/1279102119592591390/06.png?ex=66d3382d&is=66d1e6ad&hm=2b408779408d5615bcfce4a1de3ab4c04d38877fcb466e63f63b81037d731ad8&')

    # Footer เนื้อหาส่วนท้าย
    emmbed.set_footer(text='Footer', icon_url='https://cdn.discordapp.com/attachments/656703700663926815/1278526554053414973/IMG_3116.png?ex=66d31a64&is=66d1c8e4&hm=bc5eb4a4424f3712a22099388091c981f6823ac3b0b3fa118972aacc6f39f44c&')

    await interaction.response.send_message(embed = emmbed)


server_on()

bot.run(TOKEN)
