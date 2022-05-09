import discord
from discord.ext import commands
from random import *
import time

client = discord.Client()

global gameOn #guessing game
gameOn = False

global num #answer for said game
num = -1

global tries #of tries for game
tries = 0

@client.event
async def on_ready(): #when it logs in it tells you
    print('Logged on as {}!'.format(client))
    await client.change_presence(activity=discord.Game(name='use $help for help!'))

@client.event
async def on_message(message): #when it recives a message
    global gameOn #global variables
    global num
    global tries
    
    msg = message.content.lower() #lowercase
    newMsg = ''
    
    for i in msg: #deletes all punct (except for $)
        if i not in '!@#%^&()_=~`{}[]|\:";<>?,.':
            newMsg += i

    msgList = newMsg.split()
    
    if message.author == client.user:
        return

    if msgList[0] == 'hi' or msgList[0] == 'hello': #says hi if someone says hi
        if randint(0, 1) == 1:
            await message.channel.send('Hello!')
        else:
            await message.channel.send('Hi!')

    if 'epic' in msg: #posts a funny image
        await message.channel.send(file=discord.File('epic.png'))

    if msgList[0] == '$help':
        helpFile = open("help.txt", "r")
        wholeThing = helpFile.read()
        await message.channel.send(wholeThing)

    if msgList[0] == '$add' or msgList[0] == '$+': #addition
        total = 0
        send = ''
        for i in range(len(msgList) - 1):
            total += int(msgList[i + 1])
            if i == len(msgList) - 2:
                send += msgList[i + 1] + ' = '
            else:
                send += msgList[i + 1] + ' + '
        await message.channel.send(send + str(total))

    if msgList[0] == '$multiply' or msgList[0] == '$*': #multiplication
        product = 1
        send = ''
        for i in range(len(msgList) - 1):
            product *= int(msgList[i + 1])
            if i == len(msgList) - 2:
                send += msgList[i + 1] + ' = '
            else:
                send += msgList[i + 1] + ' * '
        await message.channel.send(send + str(product))

    if msgList[0] == '$subtract' or msgList[0] == '$-': #subtraction
        if len(msgList) == 3:
            total = int(msgList[1]) - int(msgList[2])
            await message.channel.send('{} - {} = {}'.format(msgList[1], msgList[2], total))
        else:
            await message.channel.send('This only works with 2 numbers!')

    if msgList[0] == '$divide' or msgList[0] == '$/': #division
        if len(msgList) == 3:
            total = int(msgList[1]) / int(msgList[2])
            await message.channel.send('{} / {} = {}'.format(msgList[1], msgList[2], total))
        else:
            await message.channel.send('This only works with 2 numbers!')
    
    if msgList[0] == '$guess': #fun guessing game
        if gameOn:
            await message.channel.send("I'm already thinking of a number between 1 and 100. Try to guess it!")
        else:
            gameOn = True
            await message.channel.send("I'm thinking of a number between 1 and 100. Try to guess it!")
            num = randint(1, 100)
        return

    if gameOn: #looks at the guesses
        try:
            msgList[0] = int(msgList[0])
            tries += 1
            if msgList[0] < num:
                await message.channel.send("Your guess was too low!")
                await message.channel.send("Guess again!")
            elif int(msgList[0]) > num:
                await message.channel.send("Your guess was too high!")
                await message.channel.send("Guess again!")
            elif msgList[0] == num:
                await message.channel.send("{} guessed the number correctly!".format(message.author.mention))
                await message.channel.send("It took you {} tries to guess that the number was {}.".format(tries, num))
                gameOn = False
                tries = 0
                num = -1
            else:
                await message.channel.send("I don't know how you got here")
        except ValueError:
            await message.channel.send("That's not an integer!")

    if msgList[0] == '$flip': #flip a coin
        if randint(0, 1) == 1:
            await message.channel.send("Heads!")
        else:
            await message.channel.send("Tails!")
        return

    if msgList[0] == '$roll':
        try:
            msgList[1] = int(msgList[1])
            if int(msgList[1]) <= 1:
                await message.channel.send("That's not a vaild die to roll!")
            else:
                await message.channel.send("I rolled a {}-sided die and got a {}!".format(msgList[1], randint(1, msgList[1])))
        except ValueError:
            await message.channel.send("That's not an integer!")
        except IndexError:
            await message.channel.send("I rolled a 6-sided die and got a {}!".format(randint(1, 6)))

##    if 'im' in msgList:
##        
        

##    if msgList[0] == '$draw':
##        if 

client.run('NjkxODUzMzcyNjYzNTI5NTMy.XnmB0g.ANiE3dlX7EnV8-tVncvdLhuSpW4')
