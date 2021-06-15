import discord
import os
import re
from better_profanity import profanity
from discord.ext import commands
from discord.ext.commands import has_permissions,CheckFailure
from discord.utils import get
from dotenv import load_dotenv

formats = ['jpg', 'jpeg', 'png', 'gif', 'svg', 'tiff', 'psd', 'eps', 'raw', 'mp4', 'mp3', 'mov', 'wmv', 'flv', 'avi', 'avchd', 'webm', 'mkv', 'vob', 'ogg', 'ogv', 'gifv', 'm4v', 'm4v', 'mpg', 'mp2', 'mpeg', 'mpe', 'mpv', 'svi', '3gp', '3g2', 'wav']
profanity.load_censor_words_from_file("CensorWords.txt")
intents = discord.Intents.all()
client = commands.Bot(command_prefix="!", intents=intents)
wl = 'WarnedList.txt'
regex = r"(?i)\b((?:https?:(?:/{1,3}|[a-z0-9%])|[a-z0-9.\-]+[.](?:com|net|org|edu|gov|mil|aero|asia|biz|cat|coop|info|int|jobs|mobi|museum|name|post|pro|tel|travel|xxx|ac|ad|ae|af|ag|ai|al|am|an|ao|aq|ar|as|at|au|aw|ax|az|ba|bb|bd|be|bf|bg|bh|bi|bj|bm|bn|bo|br|bs|bt|bv|bw|by|bz|ca|cc|cd|cf|cg|ch|ci|ck|cl|cm|cn|co|cr|cs|cu|cv|cx|cy|cz|dd|de|dj|dk|dm|do|dz|ec|ee|eg|eh|er|es|et|eu|fi|fj|fk|fm|fo|fr|ga|gb|gd|ge|gf|gg|gh|gi|gl|gm|gn|gp|gq|gr|gs|gt|gu|gw|gy|hk|hm|hn|hr|ht|hu|id|ie|il|im|in|io|iq|ir|is|it|je|jm|jo|jp|ke|kg|kh|ki|km|kn|kp|kr|kw|ky|kz|la|lb|lc|li|lk|lr|ls|lt|lu|lv|ly|ma|mc|md|me|mg|mh|mk|ml|mm|mn|mo|mp|mq|mr|ms|mt|mu|mv|mw|mx|my|mz|na|nc|ne|nf|ng|ni|nl|no|np|nr|nu|nz|om|pa|pe|pf|pg|ph|pk|pl|pm|pn|pr|ps|pt|pw|py|qa|re|ro|rs|ru|rw|sa|sb|sc|sd|se|sg|sh|si|sj|Ja|sk|sl|sm|sn|so|sr|ss|st|su|sv|sx|sy|sz|tc|td|tf|tg|th|tj|tk|tl|tm|tn|to|tp|tr|tt|tv|tw|tz|ua|ug|uk|us|uy|uz|va|vc|ve|vg|vi|vn|vu|wf|ws|ye|yt|yu|za|zm|zw)/)(?:[^\s()<>{}\[\]]+|\([^\s()]*?\([^\s()]+\)[^\s()]*?\)|\([^\s]+?\))+(?:\([^\s()]*?\([^\s()]+\)[^\s()]*?\)|\([^\s]+?\)|[^\s`!()\[\]{};:'.,<>?«»“”‘’])|(?:(?<!@)[a-z0-9]+(?:[.\-][a-z0-9]+)*[.](?:com|net|org|edu|gov|mil|aero|asia|biz|cat|coop|info|int|jobs|mobi|museum|name|post|pro|tel|travel|xxx|ac|ad|ae|af|ag|ai|al|am|an|ao|aq|ar|as|at|au|aw|ax|az|ba|bb|bd|be|bf|bg|bh|bi|bj|bm|bn|bo|br|bs|bt|bv|bw|by|bz|ca|cc|cd|cf|cg|ch|ci|ck|cl|cm|cn|co|cr|cs|cu|cv|cx|cy|cz|dd|de|dj|dk|dm|do|dz|ec|ee|eg|eh|er|es|et|eu|fi|fj|fk|fm|fo|fr|ga|gb|gd|ge|gf|gg|gh|gi|gl|gm|gn|gp|gq|gr|gs|gt|gu|gw|gy|hk|hm|hn|hr|ht|hu|id|ie|il|im|in|io|iq|ir|is|it|je|jm|jo|jp|ke|kg|kh|ki|km|kn|kp|kr|kw|ky|kz|la|lb|lc|li|lk|lr|ls|lt|lu|lv|ly|ma|mc|md|me|mg|mh|mk|ml|mm|mn|mo|mp|mq|mr|ms|mt|mu|mv|mw|mx|my|mz|na|nc|ne|nf|ng|ni|nl|no|np|nr|nu|nz|om|pa|pe|pf|pg|ph|pk|pl|pm|pn|pr|ps|pt|pw|py|qa|re|ro|rs|ru|rw|sa|sb|sc|sd|se|sg|sh|si|sj|Ja|sk|sl|sm|sn|so|sr|ss|st|su|sv|sx|sy|sz|tc|td|tf|tg|th|tj|tk|tl|tm|tn|to|tp|tr|tt|tv|tw|tz|ua|ug|uk|us|uy|uz|va|vc|ve|vg|vi|vn|vu|wf|ws|ye|yt|yu|za|zm|zw)\b/?(?!@)))"

async def clearShit(message):
  if message.content.startswith('$clear'):
    mgs = []
    number = 10
    mgs = await message.channel.history(limit=number).flatten()
    for x in mgs:
      await x.delete()

async def Check_Mod_Mention(message):
  modId = 853978191387688981
  rolesToCheckAgainst = [
    message.guild.get_role(modId)
  ]

    # 'rolesWerePinged' will be true if any of the roles were pinged
  rolesWerePinged = any(item in rolesToCheckAgainst for item in message.role_mentions)
  if message.channel.name == 'for_support':
    if rolesWerePinged:
      supportmsg = '<@%s>'%message.author.id +' Please wait your query will be taken into consideration soon'
      await message.channel.send(supportmsg)
    else:
      await message.delete()
  else:
    if rolesWerePinged:
      await message.delete()


@client.event
async def on_ready():
  print('We Have Looged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  msgkick = message
  #msgBan = message
  message_content = message.content.lower()
  #if message.content.startswith('$Hello Manager'):
    #await message.channel.send('Jada mat bol mai roh padungi :(')
  if profanity.contains_profanity(message_content):
    await message.delete()
    await message.channel.send('Using Swear words is Prohibited')
    await message.channel.send('Warning For <@%s>!!! If you continue this behaviour you will be kick out!!'% message.author.id)
    file = open(wl,'r')
    readfile = file.read()
    flag = 0
    if str(message.author.id) in readfile:
      flag = 1
    file.close()
    if flag == 1:
      banid = message.author.id
      msgkick.content = '!ban <@%s>'%banid
      await client.process_commands(msgkick)
    else:
      file = open(wl,'a')
      file.write('%s\n'%message.author.id)


  if '@everyone' in message.content or '@here' in message.content:
    await message.delete()

  await Check_Mod_Mention(message)

  if re.search(regex,message.content):
    filelinks = open('AllowedLinks','r')
    readfl = filelinks.read()
    for link in readfl:
      if link in message.content:
        return  #check for links
      else:
        await message.delete()
    filelinks.close()

  #to delete images
  attachments = [f for f in message.attachments if f.filename.split('.')[-1] in formats]
  if attachments:
    await message.delete()

  await clearShit(message)


async def check_rules_acceptance(channel,message,user,emoji):
  c_channel = client.get_channel(853571038817288242)
  msgID = 853589659295547402
  rules_msg = await c_channel.fetch_message(msgID)
  roleID = 853166599329808445
  guild = client.guilds[0]
  role = get(guild.roles, id=roleID)
  if emoji.name == '\N{THUMBS UP SIGN}' and role in user.roles and message == rules_msg:
    default_role = discord.utils.get(guild.roles, id=853166599329808445)
    new_role = discord.utils.get(guild.roles, id=853166897835278386)

    await user.add_roles(new_role)
    await user.remove_roles(default_role)


@client.event
async def on_raw_reaction_add(payload):
    channel = await client.fetch_channel(payload.channel_id)
    message = await channel.fetch_message(payload.message_id)
    #user = await client.fetch_user(payload.mem)
    user = payload.member
    emoji = payload.emoji
    await check_rules_acceptance(channel,message,user,emoji)


@client.event
async def on_member_join(member):
  default_role = discord.utils.get(member.guild.roles, id=853166599329808445)
  await member.add_roles(default_role)

@client.command(pass_context = True)
@has_permissions(administrator=True)
async def kick(ctx, member: discord.Member, *, reason=None):
     await member.kick(reason=reason)

@kick.error
async def kick_error(error, ctx):
    if isinstance(error,CheckFailure):
        await client.send_message(ctx.message.channel, "Looks like you don't have the permission.")

@client.command(pass_context = True)
async def ban(ctx, member: discord.Member, *, reason=None):
     await member.ban(reason=reason)
client.run(os.getenv('TOKEN'))
