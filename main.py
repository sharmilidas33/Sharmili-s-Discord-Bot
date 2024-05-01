import discord
import os
from discord.ext import commands
import google.generativeai as genai

from keep_alive import keep_alive

token = os.environ['SECRET_KEY']
os.getenv('GOOGLE_API_KEY')

bot = commands.Bot(command_prefix="@", intents=discord.Intents.all())

model = genai.GenerativeModel('gemini-pro',
                              safety_settings=[
                                  {
                                      "category": "HARM_CATEGORY_DANGEROUS",
                                      "threshold": "BLOCK_NONE",
                                  },
                                  {
                                      "category": "HARM_CATEGORY_HARASSMENT",
                                      "threshold": "BLOCK_NONE",
                                  },
                                  {
                                      "category": "HARM_CATEGORY_HATE_SPEECH",
                                      "threshold": "BLOCK_NONE",
                                  },
                                  {
                                      "category":
                                      "HARM_CATEGORY_SEXUALLY_EXPLICIT",
                                      "threshold": "BLOCK_NONE",
                                  },
                                  {
                                      "category":
                                      "HARM_CATEGORY_DANGEROUS_CONTENT",
                                      "threshold": "BLOCK_NONE",
                                  },
                              ])


@bot.event
async def on_ready():
  if bot.user is not None:
    print(f"Logged in as: {bot.user.name}!")
  else:
    print("Failed to log in to Discord.")


@bot.event
async def on_member_join(member):
  channel = discord.utils.get(member.guild.channels, name='welcome')
  if channel:
    await channel.send(
        f'Welcome to Sharmili\'s Discord Bot server, {member.mention}!')


@bot.event
async def on_message(message):
  if message.author == bot.user:
    return
  content = message.content.lower()
  if content in ['hello', 'hi', 'HELLO', 'HI', 'Hello', 'Hi']:
    await message.channel.send(
        f'Hello {message.author.mention}! Welcome to Sharmili\'s Discord Bot server. Use the command @heybot first and then your message, to get started!'
    )

  await bot.process_commands(message)


@bot.command(name="heybot")
async def askai(ctx: commands.Context, *, prompt: str):
  response = model.generate_content(prompt)
  await ctx.reply(response.text)


keep_alive()

try:
  bot.run(token)
except discord.errors.HTTPException:
  print("\n\n\nBLOCKED BY RATE LIMITS\nRESTARTING NOW\n\n\n")
  os.system('kill 1')
os.system("python restarter.py")
