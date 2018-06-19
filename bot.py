import random
import asyncio
import aiohttp
import json
from discord import Game
from discord.ext.commands import Bot

BOT_PREFIX = ("?", "!", ">", "*", "-", "_", ":", ".", "^", "<", "+", "&")
TOKEN = "NDQ5MjMyNTc4NzIyMTM2MTA1.Dgotug.57IzHAaTANGhiEHxwT-cSniM6qQ"  # Get at discordapp.com/developers/applications/me

client = Bot(command_prefix=BOT_PREFIX)

#https://www.ranker.com/list/the-catchiest-viral-internet-songs-of-all-time/kel-varnsen
@client.command(name='song',
                description="Sends link to random song",
                brief="Sends link to random song",
                aliases=['rsong', 'randomsong'],
                pass_context=True)
async def song(context):
    possible_responses = [
        'Whats Going On - https://youtu.be/ZZ5LpwO-An4',
        'Trololololo - https://youtu.be/t6FUR_nhGX8',
        'Dragostea Din Tei (Numa Numa) - https://youtu.be/OE8WzYNRPNU',
        'Keyboard Cat - https://youtu.be/J---aiyznGQ',
        'Nyan Cat - https://youtu.be/QH2-TGUlwu4',
    ]
    await client.say(random.choice(possible_responses) + " \n\n" + context.message.author.mention)


@client.command(name='joke',
                description="Tells a funny joke",
                brief="Tells a funny joke",
                aliases=[],
                pass_context=True)
async def joke(context):
    possible_responses = [
        'Can a kangaroo jump higher than a house? \n - \n Of course, a house doesn’t jump at all.',
        'Doctor: "Im sorry but you suffer from a terminal illness and have only 10 to live."\nPatient: "What do you mean, 10? 10 what? Months? Weeks?!"\nDoctor: "Nine."',
        'A man asks a farmer near a field, “Sorry sir, would you mind if I crossed your field instead of going around it? You see, I have to catch the 4:23 train.”\nThe farmer says, “Sure, go right ahead. And if my bull sees you, you’ll even catch the 4:11 one.”',
        'Anton, do you think I’m a bad mother?\nMy name is Paul.',
        'My dog used to chase people on a bike a lot. It got so bad, finally I had to take his bike away.',
        'What is the difference between a snowman and a snowwoman?\n-\nSnowballs.',
        'Mother: "How was school today, Patrick?"\nPatrick: "It was really great mum! Today we made explosives!"\nMother: "Ooh, they do very fancy stuff with you these days. And what will you do at school tomorrow?"\nPatrick: "What school?"',
        '"Mom, where do tampons go?"\n"Where the babies come from, darling."\n"In the stork?"',
        'Man to his priest: “Yesterday I sinned with an 18 year old girl.”\nThe priest: “Squeeze 18 lemons and drink the juice all at once.”\nMan: “And that frees me from my sin?”\nPriest: “No, but it frees your face from that dirty grin.”',
    ]
    await client.say(random.choice(possible_responses) + " \n\n " + context.message.author.mention)


@client.command(name='meme',
                description="Sends a funny meme",
                brief="Sends a funny meme",
                aliases=[],
                pass_context=True)
async def joke(context):
    possible_responses = [
        'https://i.imgflip.com/251f7h.jpg',
        'http://www.funnybeing.com/wp-content/uploads/2016/08/Im-Loving-It-600x600.jpg',
        'http://www.funnybeing.com/wp-content/uploads/2016/08/Im-Sorry-But-I-Cant-See-The-Difference-600x797.jpg',
        'http://www.funnybeing.com/wp-content/uploads/2016/08/Kiss-Her-Like-This-600x600.jpg',
        'http://www.funnybeing.com/wp-content/uploads/2016/08/Ladies-Im-Taken-591x800.jpg',
        'http://www.funnybeing.com/wp-content/uploads/2016/08/Love-Is-In-The-Air-Wrong-600x568.jpg',
        'http://www.funnybeing.com/wp-content/uploads/2016/08/Love-Is-In-The-Air-600x600.jpg',
        'http://www.funnybeing.com/wp-content/uploads/2016/08/Love-Is-Like-A-Fart-539x800.jpg',
        'http://www.funnybeing.com/wp-content/uploads/2016/08/Love-Is-Not-Having-To-Hold-Your-Farts-600x389.jpg',
        'http://www.funnybeing.com/wp-content/uploads/2016/08/Me-Waiting-For-A-Text-Back-533x800.jpg',
        'http://www.funnybeing.com/wp-content/uploads/2016/08/Men-Vs-Women-In-Love-562x800.jpg',
        'http://www.funnybeing.com/wp-content/uploads/2016/08/Mommy-Why-Are-People-So-Cruel-600x795.jpg',
        'http://www.funnybeing.com/wp-content/uploads/2016/08/My-Heart-Aches-600x610.jpg',
        'http://www.funnybeing.com/wp-content/uploads/2016/08/My-Love-For-You-Is-Like-Diarrhea-600x796.jpg',
        'http://www.funnybeing.com/wp-content/uploads/2016/08/Ofcourse-I-Love-You-600x440.jpg',
        'http://www.funnybeing.com/wp-content/uploads/2016/08/Said-I-Love-You-To-Him-600x557.jpg',
        'http://www.funnybeing.com/wp-content/uploads/2016/08/Stop-Running-I-Love-You-600x393.jpg',
        'http://www.funnybeing.com/wp-content/uploads/2016/08/Tell-Me-How-Much-You-Love-Me-600x657.jpg',
        'http://www.funnybeing.com/wp-content/uploads/2016/08/The-Dumb-Shit-You-Do-600x438.jpg',
        'http://www.funnybeing.com/wp-content/uploads/2016/08/Told-My-Crush-That-I-Love-Her-600x518.jpg',
        'http://www.funnybeing.com/wp-content/uploads/2016/08/True-Love-Means-600x452.jpg',
        'http://www.funnybeing.com/wp-content/uploads/2016/08/What-If-I-Told-You-2-600x364.jpg',
        'http://www.funnybeing.com/wp-content/uploads/2016/08/When-She-Come-Home-Drunk-600x600.jpg',
        'http://www.funnybeing.com/wp-content/uploads/2016/08/When-You-Both-Gained-A-Few-Pounds-600x679.png',
        'http://www.funnybeing.com/wp-content/uploads/2016/08/When-You-Love-Him-600x678.png',
        'http://www.funnybeing.com/wp-content/uploads/2016/08/When-You-Love-Him-600x678.png',
        'http://www.funnybeing.com/wp-content/uploads/2016/08/You-Are-My-Password-In-Wow-600x422.jpg',
        'http://www.funnybeing.com/wp-content/uploads/2016/08/You-Cant-Deny-Our-Love-600x485.jpg',
        'http://www.funnybeing.com/wp-content/uploads/2016/08/You-Love-Her-But-She-Loves-Him-600x373.jpg',
        'http://www.funnybeing.com/wp-content/uploads/2016/08/Youre-The-Type-Of-Guy-600x424.jpg',
        'http://www.funnybeing.com/wp-content/uploads/2016/08/A-Relationship-Like-This-600x600.jpg',
        'http://www.funnybeing.com/wp-content/uploads/2016/08/All-You-Need-Is-Love-600x413.jpg',
        'http://www.funnybeing.com/wp-content/uploads/2016/08/And-I-Will-Always-Love-You-517x800.jpg',
        'http://www.funnybeing.com/wp-content/uploads/2016/08/And-Then-I-Realized-600x787.jpg',
        'http://www.funnybeing.com/wp-content/uploads/2016/08/As-Long-As-You-Love-Me-509x800.png',
        'http://www.funnybeing.com/wp-content/uploads/2016/08/Brothers-This-One-Is-About-Love-600x481.jpg',
        'http://www.funnybeing.com/wp-content/uploads/2016/08/Girl-You-Should-Sell-Hotdogs-600x590.jpg',
        'http://www.funnybeing.com/wp-content/uploads/2016/08/Hey-Derp-Isnt-That-Your-Crush-600x438.jpg',
        'http://www.funnybeing.com/wp-content/uploads/2016/08/Hey-You-Yea-You-600x450.jpg',
        'http://www.funnybeing.com/wp-content/uploads/2016/08/Hold-Still-Im-Gonna-Love-On-You-600x586.jpg',
        'http://www.funnybeing.com/wp-content/uploads/2016/08/How-I-Feel-When-Someone-600x459.jpg',
        'http://www.funnybeing.com/wp-content/uploads/2016/08/I-Do-This-Out-Of-Love-600x611.jpg',
        'http://www.funnybeing.com/wp-content/uploads/2016/08/I-Dont-Think-I-Love-You-Anymore-600x442.jpg',
        'http://www.funnybeing.com/wp-content/uploads/2016/08/I-Love-This-Post-600x702.jpg',
        'http://www.funnybeing.com/wp-content/uploads/2016/08/I-Love-You-Couch-600x462.jpg',
        'http://www.funnybeing.com/wp-content/uploads/2016/08/I-Love-You-So-Much-600x420.jpg',
        'http://www.funnybeing.com/wp-content/uploads/2016/08/I-Love-You-This-Much-No-Lie-600x592.jpg',
        'http://www.funnybeing.com/wp-content/uploads/2016/08/I-Love-You-This-Much-600x472.jpg',
        'http://www.funnybeing.com/wp-content/uploads/2016/08/I-Love-You-Zebra-542x800.jpg',
        'http://www.funnybeing.com/wp-content/uploads/2016/08/I-Love-You-There-I-Said-It-600x438.jpg',
        'http://www.funnybeing.com/wp-content/uploads/2016/08/I-Must-Destroy-You-600x401.jpg',

    ]
    await client.say(random.choice(possible_responses) + " \n\n " + context.message.author.mention)


@client.command(name='hello',
                description="Says hello to you",
                brief="Says hello to you",
                aliases=['hi', 'hey'],
                pass_context=True)
async def hello(context):
    possible_responses = [
        'Hey',
        'Hello',
        'Hi',
    ]
    await client.say(random.choice(possible_responses) + " " + context.message.author.mention + "!")


@client.command(name='prefix',
                description="Says hello to you",
                brief="Says hello to you",
                aliases=['prefixes'],
                pass_context=True)
async def prefix(context):
    possible_responses = [
        '1. ? \n2. ! \n3. > \n4. * \n5. - \n6. _ \n7. : \n8. . \n9. ^ \n10. < \n11. + \n12. &',
    ]
    await client.say(random.choice(possible_responses) + " " + context.message.author.mention + "!")


TaskList = []

@client.command()
async def addtask(*args):
  output = ""
  for word in args:
    output += word
    #output += " "
  TaskList.append(output)
  await client.say("The task '" + output + "' has been added to the list!")

@client.command()
async def showtasks():
  await client.say(TaskList)

@client.command()
async def cleartasks():
  TaskList[:] = []
  await client.say("Tasks has been cleared")


@client.event
async def on_ready():
    await client.change_presence(game=Game(name="!help"))
    print("Logged in as " + client.user.name)


async def list_servers():
    await client.wait_until_ready()
    while not client.is_closed:
        print("Current servers:")
        for server in client.servers:
            print("- " + server.name)
        await asyncio.sleep(600)


client.loop.create_task(list_servers())
client.run(TOKEN)
