from pprint import pprint

import discord
import random
from discord.ext import commands
import os
import time
import psutil
import datetime
import string
import random

def listToString(s):
    str1 = ""
    for ele in s:
        str1 += str(ele) + "  "
    return str1


class Basic(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.version = '3.0'
        self.processID = psutil.Process(os.getpid())
        print("Basic commands loaded")

    def getBotStat(self):
        sendTo = []
        text_channel_list = []
        for guild in self.client.guilds:
            for channel in guild.text_channels:
                text_channel_list.append(channel)
        for channel in text_channel_list:
            if channel.name.__contains__('bot'):
                sendTo.append(channel)
        return sendTo
        # for guild in self.client.guilds:
        #     for channel in guild.text_channels:
        #         if channel.name == 'bot-status' and guild.name == 'D and D':
        #             sendTo = channel
        # return sendTo

    @commands.Cog.listener()
    async def on_ready(self):
        self.up = time.strftime("%Y-%m-%d %H:%M:%S",
                                time.localtime(self.processID.create_time()))
        os.system('clear')
        channels = self.getBotStat()
        for channel in channels:
            await channel.send(f'I have arrived with version {self.version} loaded')
            await channel.send(f'Boot time:{self.up}')

    @commands.Cog.listener()
    async def on_message(self, message):
        # if you want a stdout record of messages uncomment this
        #print(
        #    f"{message.channel}: {message.author}: {message.author.name}: {message.content}")
        text = []
        for str in message.content.upper().split():
            text.append(str.translate(
                str.maketrans('', '', string.punctuation)))
        for x in text:

            if x == 'BOT' and (message.author.display_name != message.guild.me.display_name):
                await message.channel.send('Beep boop')


    def helpEmbed(self):
        embed = discord.Embed(
            color=discord.Colour.teal(),
            title='Help'
        )
        embed.add_field(name='!help',
                        value='This message',
                        inline=False)
        embed.add_field(name='!randomMembers',
                        value='Takes in a number up to the number of non-bot members and returns that many members randomly (defaults to 5).',
                        inline=False)
        embed.add_field(name='!printRoles',
                        value='Prints out all roles of the requesting member (except for @everyone)',
                        inline=False)
        embed.add_field(name='!addCheckpoint',
                            value='Takes a name and three coordinates and saves a checkpoint.  FORMAT: !addCheckpoint {NAME} {XCOORD} {YCOORD} {ZCOORD}',
                            inline=False)
        embed.add_field(name='!getCheckpoint',
                            value='Takes a name of a checkpoint and returns its coordinates.  FORMAT: !getCheckpoint {NAME}',
                            inline=False)
        embed.add_field(name='!deleteCheckpoint',
                            value='Takes a name of a checkpoint and deletes it.  FORMAT: !deleteCheckpoint {NAME}',
                            inline=False)
        embed.add_field(name='!allCheckpoints',
                        value='Prints out all checkpoints and their coordinates.',
                        inline=False)
        return embed

    @commands.command()
    async def randomMembers(self, ctx, num='5'):
        realMembers = [member for member in ctx.guild.members if not member.bot]
        if int(num) > len(realMembers):
            await ctx.send('The sample size must be less than or equal to the number of non-bot users in the server.')
            return
        members = random.sample(realMembers, int(num))
        memberName = []
        for member in members:
            if member.nick is None:
                memberName.append(member.name)
            else:
                memberName.append(member.nick)
        await ctx.send(listToString(memberName))

    @commands.command()
    async def help(self, ctx):
        await ctx.channel.send(embed=self.helpEmbed())

    @commands.command()
    async def shutdown(self, ctx):
        if ctx.message.author.id == 462279607853514760:  # replace OWNERID with your user id
            print("shutdown")
            await ctx.send("Goodbye world")
            try:
                await self.client.close()
            except:
                print("EnvironmentError")
                self.client.clear()
        else:
            await ctx.send("You do not own this bot, dummy.")

    @commands.command()
    async def printRoles(self, ctx):
        await ctx.send('You have these roles: ' + listToString(ctx.author.roles[1:]))

    @commands.command()
    async def hampter(self, ctx):
        await ctx.send(file=discord.File('hampter.jpeg'))

    @commands.command()
    async def secret(self, ctx):
        embed = discord.Embed(
            color=discord.Colour.red(),
            title='Secret Step 1'
        )
        embed.add_field(name='First Clue', value='What color is best?', inline=False)
        await ctx.channel.send(embed=embed)

    @commands.command()
    async def red(self, ctx):
        await ctx.send('Well done.')
        embed = discord.Embed(
            color=discord.Colour.red(),
            title='Secret Step 2'
        )
        embed.add_field(name='Second Clue', value='What food do you throw away the outside, cook the inside, then eat the outside and throw away the inside?', inline=False)
        await ctx.channel.send(embed=embed)

    @commands.command()
    async def corn(self, ctx):
        await ctx.send('Two down.')
        embed = discord.Embed(
            color=discord.Colour.red(),
            title='Secret Step 3'
        )
        embed.add_field(name='Third Clue',
                        value='Grunkle Stan, are you wearing a blindfold?  Hahaha, nah but with these cataracts I might as well be.  What is that a ________?',
                        inline=False)
        await ctx.channel.send(embed=embed)

    @commands.command()
    async def woodpecker(self, ctx):
        await ctx.send('Last one.')
        embed = discord.Embed(
            color=discord.Colour.red(),
            title='Secret Step 4'
        )
        embed.add_field(name='Final Clue',
                        value='What animal does Keith\'s roomate have a tattoo of?',
                        inline=False)
        await ctx.channel.send(embed=embed)

    @commands.command()
    async def phoenix(self, ctx):
        await ctx.send('I commend the effort.  Here is your reward: a wrestling match video circa 2013, as well exclusive interviews at the end.')
        await ctx.send('https://www.youtube.com/watch?v=LOuc0RDR97I&t=1s')

    @commands.command()
    async def hiDom(self, ctx):
        await ctx.send('Grandma\'s sucking eggs again')

def setup(client):
    client.add_cog(Basic(client))


if __name__ == '__main__':
    os.system('python3 main.py')
