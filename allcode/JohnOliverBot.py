global creamStocksMarketCap 
global creamStockSharesAvailable 
global creamStockValue

import os

import discord
import pickle
from dotenv import load_dotenv, find_dotenv

load_dotenv("D:\PublicNBAWebsite\.env")

token = os.getenv("DISCORDTOKEN")
guild = "Steelcrawler's serverdasfasd"

client = discord.Client()


# def save_object(obj, param):
#     try:
#         with open((param + ".pickle"), "wb") as f:
#             pickle.dump(obj, f)
#     except Exception as ex:
#         print("Error during pickling object (Possibly unsupported):", ex)

# def load_object(filename):
#     try:
#         with open(filename, "rb") as f:
#             return pickle.load(f)
#     except Exception as ex:
#         return 0



# creamStocksMarketCap = load_object("marketCap.pickle")
# if (load_object("sharesAvailable.pickle") == 0):
#     creamStockSharesAvailable = 5
# else:
#     creamStockSharesAvailable = load_object("sharesAvailable.pickle")
# creamStockValue = creamStocksMarketCap/creamStockSharesAvailable



@client.event
async def on_message(message):
    #if message.author.id in (541319380919910400, 724681050395115520):
    #    await message.add_reaction("\U0001F913") 

    
    
    #if message.author.id == 393251455685099521:
    #    await message.add_reaction("\U0001F5FA")

    if 'collectmymessages' in message.content.lower():
        print("hello")
        channel_id = 841413965836714004
        channel = client.get_channel(channel_id)
        if not channel:
            print("wrongchannel")
            return

        messages = channel.history(limit=300000)
        async for message1 in messages:
            if "yes" in message1.content.lower():
                await message1.delete()
                print("message deleted")


# @client.event
# async def on_reaction_add(reaction, user):
#     if user != client.user and reaction.emoji.name == "kream":
#         global creamStocksMarketCap 
#         creamStocksMarketCap += 5
#         await reaction.message.channel.send("Current CRM Market Cap is at: $" + str(creamStocksMarketCap))
#         save_object(creamStocksMarketCap, "marketCap")
        


# @client.event
# async def on_member_join(member):
#     await member.create_dm()
#     await member.dm_channel.send(
#         'leave.'
#     )

# save_object(creamStockSharesAvailable, "sharesAvailable")


@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')
    print(client.user.id)

client.run(token)
