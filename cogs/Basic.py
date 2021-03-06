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
        #for channel in channels:
            #await channel.send(f'I have arrived with version {self.version} loaded')
            #await channel.send(f'Boot time:{self.up}')

    @commands.Cog.listener()
    async def on_message(self, message):
        desmondQuestion = random.random()
        if desmondQuestion <= 0.01:
            await message.channel.send('Why isn\'t Desmond in this server?')
        # if you want a stdout record of messages uncomment this
        #print(
        #    f"{message.channel}: {message.author}: {message.author.name}: {message.content}")
        if desmondQuestion <= 0.05:
            if message.author.id == 117379258606813190:
                await message.channel.send('Objectively, a dub.')
            if message.author.id == 189210165155856384:
                await message.channel.send('Go take a shower Sam. Stinky.')
            if message.author.id == 592047866592362517:
                await message.channel.send('Delaney.')
                await message.channel.send('Delaney.')
                await message.channel.send('Delaney.')
                await message.channel.send('Delaney.')
                await message.channel.send('Hi.')
            if message.author.id == 571325175841161247:
                await message.channel.send('Masa you are a legend.')
            if message.author.id == 247539199937478666:
                await message.channel.send('Hi Bwaise!')
            if message.author.id == 326823021081788416:
                await message.channel.send('https://www.youtube.com/watch?v=GK2GUxOnjDQ')
            if message.author.id == 314198862560493569:
                await message.channel.send('https://www.youtube.com/watch?v=2WaDvi11hmA')
            if message.author.id == 409855271066796033:
                await message.channel.send('Garrett your new IQP is Pikmin 4.')
            if message.author.id == 540277525511667723:
                await message.channel.send('Bane of Arthropods is the only good sword enchantment.')
            if message.author.id == 171769768276262912:
                await message.channel.send('Jakob, I, Dominic Golding, have always envied your incredible beard')
            if message.author.id == 174994662153519105:
                await message.channel.send('Overwatch is dead.')
            if message.author.id == 689113642276356136:
                await message.channel.send('Jazz is dead.')
            if message.author.id == 368482797263781899:
                await message.channel.send('Go eat cold pasta Tony.')
            if message.author.id == 606668276029980673:
                await message.channel.send('Hi Alicia.')
            if message.author.id == 824295193074204683:
                await message.channel.send('Hi Abby.')
            if message.author.id == 813793810433048596:
                await message.channel.send('Iris you have elite music taste.')
            if message.author.id == 826545442124201994:
                await message.channel.send('Jane I cannot believe you actually typed in the Discord.')
            if message.author.id == 509535927832674315:
                await message.channel.send('Honey has no place in tomato sauce.')
            if message.author.id == 231623681770520577:
                await message.channel.send('Funny guy. Right here. Real funny.')
            if message.author.id == 671901829134680064:
                await message.channel.send('\'Ell Govna.')

        text = []
        for str in message.content.upper().split():
            text.append(str.translate(
                str.maketrans('', '', string.punctuation)))
        for x in text:

            if x == 'BOT' and (message.author.display_name != message.guild.me.display_name):
                await message.channel.send('Beep boop')
                break
            if (x == 'DOMINIC' or x == 'DOM') and (message.author.display_name != message.guild.me.display_name):
                await message.channel.send('\'Ello ' + message.author.display_name.split(' ')[0])
                break
            if (x == 'IQP') and (message.author.display_name != message.guild.me.display_name):
                await message.channel.send('IQP is a key and essential part to your engineering education.')
                break


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
