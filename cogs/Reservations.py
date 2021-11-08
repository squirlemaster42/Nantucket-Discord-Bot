import discord
import random
from discord.ext import commands
import os
import time
import psutil
import datetime
from datetime import date
import string
import random
import csv
from csv import writer
import os.path


class Reservations(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.version = '3.0'
        self.processID = psutil.Process(os.getpid())
        print("Reservation commands loaded")

    @commands.command()
    async def getDate(self, ctx):
        todayDate = date.today().strftime("%m/%d/%Y")  # using datetime to get the current date in format MM/DD/YY

        separatedDate = todayDate.split(
            '/')  # date time keeping leading zeros in days (11/07/21) so we must remove them
        if separatedDate[1][0] == '0':
            monthDateSeparation = todayDate.index('/')
            todayDate = todayDate[:monthDateSeparation + 1] + todayDate[monthDateSeparation + 2:]

        await ctx.send(todayDate)  # send the date to the requester

    @commands.command()
    async def reserve(self, ctx, room, start, end, date='NaN', reason=''):  # get person reserving from ctx.author

        # ensure room is correct
        room = room.upper()
        if room != 'K' and room != 'L':
            await ctx.send('The room reserved must be either "k" for the kitchen or "l" for the living room.')
            return

        # format time
        start = formatTime(start)
        end = formatTime(end)
        print("Start :" + start)
        print("End :" + end)

        # format date
        if date != 'NaN':
            separated = date.split('/')
            for block in separated:
                try:
                    int(block)
                except:
                    await ctx.send('Date must be formatted month / day / last two digits of year.')
                    return
        else:
            date = getTodayDate()
        print("Date :" + date)

        requester = ctx.author.display_name.split(' ')[0] # should get the first name of the requester
        print("Requester: " + requester)

        reservation = requester + reason # the actual text that will be placed in the spreadsheet
        print("Reservation: " + reservation)

        ## HERE IS WHERE WE EDIT THE SPREADSHEET - KD

        await ctx.send('Room reserved!')

        return

def formatTime(time):
    time = time.upper()
    try:
        splitIndex = time.index('M') - 1
    except:
        raise Exception('Time isn\'t formatted properly')
    separatedTime = [time[:splitIndex], time[splitIndex:]]
    return separatedTime[0] + ":00:00" + separatedTime[1]


def getTodayDate():
    todayDate = date.today().strftime("%m/%d/%Y")
    separatedDate = todayDate.split('/')
    if separatedDate[1][0] == '0':
        monthDateSeparation = todayDate.index('/')
        todayDate = todayDate[:monthDateSeparation + 1] + todayDate[monthDateSeparation + 2:]
    return todayDate


def setup(client):
    client.add_cog(Reservations(client))


if __name__ == '__main__':
    os.system('python3 main.py')
