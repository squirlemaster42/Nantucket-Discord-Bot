import discord
import random
from discord.ext import commands
import os
import time
import psutil
import datetime
import string
import random
import csv
from csv import writer
import os.path



class Minecraft(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.version = '2.0'
        self.processID = psutil.Process(os.getpid())
        print("Minecraft commands loaded")

    def addRowToCSV(self, file_name, list_of_elem):
        with open(os.path.join(os.path.dirname(__file__), os.pardir, file_name), 'a+', newline='') as write_obj:
            csv_writer = writer(write_obj)
            csv_writer.writerow(list_of_elem)

    def dictFromCSV(self, file_name):
        with open(os.path.join(os.path.dirname(__file__), os.pardir, file_name), mode='r') as inp:
            reader = csv.reader(inp)
            checkpoints = {rows[0]: [rows[1], rows[2], rows[3]] for rows in reader}
        return checkpoints

    @commands.command()
    async def addCheckpoint(self, ctx, name, xCoord, yCoord, zCoord):

        try:
            int(xCoord)
            int(yCoord)
            int(zCoord)
        except ValueError:
            await ctx.send("Coordinates must be integers.")
            return

        checkpoints = self.dictFromCSV("checkpoints.csv")

        try:
            checkpoints[name]
            await ctx.send("A checkpoint already exists with that name.")
        except KeyError:
            data = [name, xCoord, yCoord, zCoord]
            self.addRowToCSV('checkpoints.csv', data)
            await ctx.send("Checkpoint \"" + data[0] + "\" added.")

    @commands.command()
    async def getCheckpoint(self, ctx, name):

        checkpoints = self.dictFromCSV("checkpoints.csv")

        try:
            await ctx.send(name + " is at " + checkpoints[name][0] + ", " + checkpoints[name][1] + ", " + checkpoints[name][2] + ".")
        except KeyError:
            await ctx.send("There is no checkpoint with that name.")

    @commands.command()
    async def deleteCheckpoint(self, ctx, name):

        checkpoints = self.dictFromCSV("checkpoints.csv")

        try:
            checkpoints[name]
        except KeyError:
            await ctx.send("No checkpoint exists with that name.")
            return

        savedLines = list()

        with open(os.path.join(os.path.dirname(__file__), os.pardir, 'checkpoints.csv'), 'r') as readFile:

            reader = csv.reader(readFile)

            for row in reader:

                savedLines.append(row)

                for field in row:

                    if field == name:
                        savedLines.remove(row)

        with open(os.path.join(os.path.dirname(__file__), os.pardir, 'checkpoints.csv'), 'w') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(savedLines)

        await ctx.send('Checkpoint \"' + name + '\" deleted.')

    @commands.command()
    async def allCheckpoints(self, ctx):

        checkpoints = self.dictFromCSV('checkpoints.csv')

        embed = discord.Embed(
            color=discord.Colour.green(),
            title='Checkpoints'
        )
        for checkpoint in checkpoints:
            embed.add_field(name=checkpoint,
                            value='(' + checkpoints[checkpoint][0] + ', ' + checkpoints[checkpoint][1] + ', ' + checkpoints[checkpoint][2] + ')',
                            inline=False)

        await ctx.send(embed=embed)



def setup(client):
    client.add_cog(Minecraft(client))


if __name__ == '__main__':
    os.system('python3 main.py')