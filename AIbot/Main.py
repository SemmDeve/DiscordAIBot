import discord
from neuralintents import GenericAssistant

client = discord.Client()
chatbot = GenericAssistant('/Users/kina/Documents/coding_dir/discord_dor/AIbot/intents.json')
chatbot.train_model()
chatbot.save_model()
print("The Bot is done training...")



@client.event
async def on_message(message):
    f = open('/Users/kina/Documents/coding_dir/discord_dor/AIbot/msg.txt', 'w+')
    if message.author == client.user:
        return
    if message.content.startswith('.aibot math'):
        mt = message.content[12:]
        s = mt.split(" ")
        x = int(s[0])
        y = int(s[-1])
        m = s[1]
        output = 0
        if m == '+':
            output = x + y
        elif m == '-':
            output = x - y
        elif m == '*':
            output = x * y
        elif m == '/':
            output = x / y
        elif m == '%':
            output = x % y
        else:
            await message.channel.send("I still learning about that")
        await message.channel.send(output)
    elif message.content.startswith('.aibot'):
        response = chatbot.request(message.content[7:])
        await message.channel.send(response)
    f.write(message.content)




client.run('YOU TOKEN HERE')

