import asyncio
import pyautogui
import discord
client = discord.Client()


#uncomment below line with guild integer
#guild = YOUR GUILD NUMBER HERE

global muteRole

global activeList
activeList = []


class Player:
    def __init__(self, alive, discord_user):
        self.alive = alive
        self.discord_user = discord_user





@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    await asyncio.sleep(10)


@client.event
async def on_message(message):
    global muteRole

    muteRole = discord.utils.get(message.author.guild.roles, name='Muted')
    if message.author == client.user:
        return

    if message.content.startswith('stop'):
        key = False

    if message.content.startswith('start'):
        client.loop.create_task(lookin())
        client.loop.create_task(on_message(message))
    if message.content.startswith('help'):
        await message.channel.send('Usage: start(silent start) bind(can write over old binds)')

    if message.content.startswith('bind'):
        parseString = message.content.split(" ")
        print(parseString)
        lowerKey = parseString[1].lower()

        if lowerKey == 'blue':
            global blue_player
            blue_player = Player(True, message.author)
            activeList.append('blue_player')
            await blue_player.discord_user.remove_roles(muteRole)
            await message.channel.send('Blue Bean Bound to ' + str(blue_player.discord_user))

        elif lowerKey == 'brown':
            global brown_player
            brown_player = Player(True, message.author)
            activeList.append('brown_player')
            await brown_player.discord_user.remove_roles(muteRole)
            await message.channel.send('Blue Bean Bound to ' + str(brown_player.discord_user))

        elif lowerKey == 'purple':
            global purple_player
            purple_player = Player(True, message.author)
            activeList.append('purple_player')
            await purple_player.discord_user.remove_roles(muteRole)
            await message.channel.send('Purple Bean Bound to ' + str(purple_player.discord_user))

        elif lowerKey == 'black':
            global black_player
            black_player = Player(True, message.author)
            activeList.append('black_player')
            await black_player.discord_user.remove_roles(muteRole)
            await message.channel.send('Black Bean Bound to ' + str(black_player.discord_user))

        elif lowerKey == 'red':
            global red_player
            red_player = Player(True, message.author)
            activeList.append('red_player')
            await red_player.discord_user.remove_roles(muteRole)
            await message.channel.send('Red Bean Bound to ' + str(red_player.discord_user))

        elif lowerKey == 'white':
            global white_player
            white_player = Player(True, message.author)
            activeList.append('white_player')
            await white_player.discord_user.remove_roles(muteRole)
            await message.channel.send('White Bean Bound to ' + str(white_player.discord_user))

        elif lowerKey == 'yellow':
            global yellow_player
            yellow_player = Player(True, message.author)
            activeList.append('yellow_player')
            await yellow_player.discord_user.remove_roles(muteRole)
            await message.channel.send('Yellow Bean Bound to ' + str(yellow_player.discord_user))

        elif lowerKey == 'lightblue':
            global light_blue_player
            light_blue_player = Player(True, message.author)
            activeList.append('light_blue_player')
            await light_blue_player.discord_user.remove_roles(muteRole)
            await message.channel.send('Black Bean Bound to ' + str(light_blue_player.discord_user))

        elif lowerKey == 'pink':
            global pink_player
            pink_player = Player(True, message.author)
            activeList.append('pink_player')
            await pink_player.discord_user.remove_roles(muteRole)
            await message.channel.send('Black Bean Bound to ' + str(pink_player.discord_user))

        elif lowerKey == 'lightgreen':
            global light_green_player
            light_green_player = Player(True, message.author)
            activeList.append('light_green_player')
            await light_green_player.discord_user.remove_roles(muteRole)
            await message.channel.send('Black Bean Bound to ' + str(light_green_player.discord_user))

        elif lowerKey == 'green':
            global green_player
            green_player = Player(True, message.author)
            activeList.append('green_player')
            await green_player.discord_user.remove_roles(muteRole)
            await message.channel.send('Black Bean Bound to ' + str(green_player.discord_user))

        elif lowerKey == 'orange':
            global orange_player
            orange_player = Player(True, message.author)
            activeList.append('orange_player')
            await orange_player.discord_user.remove_roles(muteRole)
            await message.channel.send('Black Bean Bound to ' + str(orange_player.discord_user))


async def ResetGame():
    print('gameOverReset')
    if 'blue_player' in activeList:
        await unMute(blue_player.discord_user)

    if 'brown_player' in activeList:
        await unMute(brown_player.discord_user)

    if 'purple_player' in activeList:
        await unMute(purple_player.discord_user)

    if 'black_player' in activeList:
        await unMute(black_player.discord_user)

    if 'red_player' in activeList:
        await unMute(red_player.discord_user)

    if 'white_player' in activeList:
        await unMute(white_player.discord_user)

    if 'yellow_player' in activeList:
        await unMute(yellow_player.discord_user)

    if 'orange_player' in activeList:
        await unMute(orange_player.discord_user)

    if 'light_blue_player' in activeList:
        await unMute(light_blue_player.discord_user)

    if 'pink_player' in activeList:
        await unMute(pink_player.discord_user)

    if 'green_player' in activeList:
        await unMute(green_player.discord_user)

    if 'light_green_player' in activeList:
        await unMute(light_green_player.discord_user)


async def WaitingRoom():
    print('lobby')
    if 'blue_player' in activeList:
        await unMute(blue_player.discord_user)

    if 'brown_player' in activeList:
        await unMute(brown_player.discord_user)

    if 'purple_player' in activeList:
        await unMute(purple_player.discord_user)

    if 'black_player' in activeList:
        await unMute(black_player.discord_user)

    if 'red_player' in activeList:
        await unMute(red_player.discord_user)

    if 'white_player' in activeList:
        await unMute(white_player.discord_user)

    if 'yellow_player' in activeList:
        await unMute(yellow_player.discord_user)

    if 'orange_player' in activeList:
        await unMute(orange_player.discord_user)

    if 'light_blue_player' in activeList:
        await unMute(light_blue_player.discord_user)

    if 'pink_player' in activeList:
        await unMute(pink_player.discord_user)

    if 'green_player' in activeList:
        await unMute(green_player.discord_user)

    if 'light_green_player' in activeList:
        await unMute(light_green_player.discord_user)


async def ButtonRoom():
    print("buttonRoom")
    if 'blue_player' in activeList:
        await Mute(blue_player.discord_user)

    if 'brown_player' in activeList:
        await Mute(brown_player.discord_user)

    if 'purple_player' in activeList:
        await Mute(purple_player.discord_user)

    if 'black_player' in activeList:
        await Mute(black_player.discord_user)

    if 'red_player' in activeList:
        await Mute(red_player.discord_user)

    if 'white_player' in activeList:
        await Mute(white_player.discord_user)

    if 'yellow_player' in activeList:
        await Mute(yellow_player.discord_user)

    if 'orange_player' in activeList:
        await Mute(orange_player.discord_user)

    if 'light_blue_player' in activeList:
        await Mute(light_blue_player.discord_user)

    if 'pink_player' in activeList:
        await Mute(pink_player.discord_user)

    if 'green_player' in activeList:
        await Mute(green_player.discord_user)

    if 'light_green_player' in activeList:
        await Mute(light_green_player.discord_user)


async def Voting():
    if BlueCount > 0:

        if 'blue_player' in activeList:
            print('BlueAlive')

            await unMute(blue_player.discord_user)

    if BrownCount > 0:
        if 'brown_player' in activeList:
            print('BlueAlive')
            await unMute(brown_player.discord_user)

    if PurpleCount > 0:

        if 'purple_player' in activeList:
            print('purple alive')
            await unMute(purple_player.discord_user)

    if BlackCount > 0:

        if 'black_player' in activeList:
            print('blackAlive')
            await unMute(black_player.discord_user)

    if RedCount > 0:

        if 'red_player' in activeList:
            print('red alive')
            await unMute(red_player.discord_user)

    if WhiteCount > 0:

        if 'white_player' in activeList:
            print('WhiteALive')
            await unMute(white_player.discord_user)

    if YellowCount > 0:

        if 'yellow_player' in activeList:
            print('yellow Alive')
            await unMute(yellow_player.discord_user)

    if OrangeCount > 0:

        if 'orange_player' in activeList:
            print('Orange alive')
            await unMute(orange_player.discord_user)

    if LightBlueCount > 0:

        if 'light_blue_player' in activeList:
            print('Light Blue alive')
            await unMute(light_blue_player.discord_user)

    if PinkCount > 0:

        if 'pink_player' in activeList:
            print('pink alive')
            await unMute(pink_player.discord_user)

    if GreenCount > 0:

        if 'green_player' in activeList:
            print('Green Alive')
            await unMute(green_player.discord_user)

    if LightGreenCount > 0:

        if 'light_green_player' in activeList:
            print('Light Green alive')
            await unMute(light_green_player.discord_user)


# pass a thread to this function and kill th e tread on input from listners
async def lookin():

    global BlueCount, BrownCount, PurpleCount, BlackCount, RedCount, WhiteCount, YellowCount, OrangeCount, LightBlueCount, PinkCount, LightBlueCount, PinkCount, GreenCount, LightGreenCount

    BlueCount = len(list(pyautogui.locateAllOnScreen('BlueALive.png', confidence=.97)))
    BrownCount = len(list(pyautogui.locateAllOnScreen('BrownAlive.png', confidence=.99)))
    PurpleCount = len(list(pyautogui.locateAllOnScreen('PurpleAlive.png', confidence=.95)))
    BlackCount = len(list(pyautogui.locateAllOnScreen('BlackAlive.png', confidence=.95)))
    RedCount = len(list(pyautogui.locateAllOnScreen('RedAlive.png', confidence=.96)))
    WhiteCount = len(list(pyautogui.locateAllOnScreen('WhiteAlive.png', confidence=.95)))
    YellowCount = len(list(pyautogui.locateAllOnScreen('YellowAlive.png', confidence=.96)))
    OrangeCount = len(list(pyautogui.locateAllOnScreen('OrangeAlive.png', confidence=.96)))
    LightBlueCount = len(list(pyautogui.locateAllOnScreen('LightBlueAlive.png', confidence=.97)))
    PinkCount = len(list(pyautogui.locateAllOnScreen('PinkAlive.png', confidence=.97)))
    GreenCount = len(list(pyautogui.locateAllOnScreen('GreenAlive.png', confidence=.98)))
    LightGreenCount = len(list(pyautogui.locateAllOnScreen('LightGreen.png', confidence=.975)))

    print("bluecount:")
    print(BlueCount)
    print("redcount:")
    print(RedCount)
    print("purplecount:")
    print(PurpleCount)
    print("blackcount:")
    print(BlackCount)
    print("whitecount:")
    print(WhiteCount)
    print("browncount:")
    print(BrownCount)
    print("yellowcount:")
    print(YellowCount)
    print("lightbluecount:")
    print(LightBlueCount)
    print("pinkcount:")
    print(PinkCount)
    print("greencount:")
    print(GreenCount)
    print("lightgreencount:")
    print(LightGreenCount)
    print("orangecount:")
    print(OrangeCount)

    # print(screenshot)
    if len(list(pyautogui.locateAllOnScreen('amoongusReset.png', confidence=.7))) > 0:
        await ResetGame()

    if len(list(pyautogui.locateAllOnScreen('Lobby.png', confidence=.6))) > 0:
        await WaitingRoom()

    if len(list(pyautogui.locateAllOnScreen('StartingButton.png', confidence=.7))) > 0:
        await ButtonRoom()

    if len(list(pyautogui.locateAllOnScreen('CheckScreen.png', confidence=.7))) > 0:
        await Voting()



async def unMute(Player):

    await Player.remove_roles(muteRole)


async def Mute(Player):

    await Player.add_roles(muteRole)


client.run('YOUR DISCORD TOKEN HERE')


