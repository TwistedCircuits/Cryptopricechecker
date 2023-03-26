import os
import discord
from discord.ext import commands
import requests

# Initialize the Coinbase API endpoint
COINBASE_API_ENDPOINT = 'https://api.coinbase.com/v2'

# Initialize the Discord bot
bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command(name='!crypto')
async def get_crypto_prices(ctx):
    # Fetch the price data for all cryptocurrencies from Coinbase
    response = requests.get(f'{COINBASE_API_ENDPOINT}/prices', params={'currency': 'USD'})
    prices = response.json()['data']
    
    # Format the price data into a readable string
    price_str = ''
    for crypto, values in prices.items():
        price_str += f'{crypto.capitalize()}: ${values["amount"]:.2f}\n'
    
    # Send the price data to the Discord channel
    await ctx.send(f'**Current Crypto Prices:**\n{price_str}')

# Start the bot
bot.run(os.environ['DISCORD_BOT_TOKEN'])
