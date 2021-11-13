from __future__ import print_function
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
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from oauth2client.service_account import ServiceAccountCredentials
import gspread

# spreadsheet ID: "14wQx1PZWiIk2870zU5n0zXruo4ZD3KJXBFx8MObPZJo"

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = None
if os.path.exists('token.json'):
    creds = Credentials.from_authorized_user_file('token.json', scope)
service = build('sheets', 'v4', credentials=creds)
sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId="14wQx1PZWiIk2870zU5n0zXruo4ZD3KJXBFx8MObPZJo", range='Sheet1!A1:Z54').execute() # do i need the range??
print(result)
#body = { 'values': ['test'] }
#result2 = sheet.values().update(spreadsheetId="14wQx1PZWiIk2870zU5n0zXruo4ZD3KJXBFx8MObPZJo", range='Sheet1!B4', valueInputOption="RAW", body=body).execute()

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
