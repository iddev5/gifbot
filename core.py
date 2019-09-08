import discord, random
import command

#global msg_count 
msg_count = 0

async def small_info(i, msg):
    global msg_count
    if msg_count == 7:
        await msg.send("Want to give feedback, report bug, send gifs or request/suggest features?\nDM me in Discord or contact through Twitter. See info command for more info")
        msg_count = 0
    else:
        msg_count += 1

async def gif_command(msg, cmd_name):
    mod = command.import_command('g_'+cmd_name)
    this_id    = mod.ID
    this_list  = mod.List
    this_color = mod.Color
    this_title = mod.Title

    await small_info(msg_count, msg)
    gif = random.choice(this_list)

    folder = discord.Embed(title = random.choice(this_title), color = random.choice(this_color))
    folder.set_image(url = gif)
    folder.set_footer(text = ("ID: "+this_id+"{}").format(this_list.index(gif)))

    await msg.send(embed = folder)
