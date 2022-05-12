import discord
from discord.ext import commands
from discord.ext.commands import has_permissions
intents = discord.Intents.all()
intents.members = True
intents.guilds = True
intents.messages = True
intents.all()

bot = commands.Bot(command_prefix='_', intents=intents, case_insensitive=True)

guild_id = YOUR_GUILD_ID
bot_token = "YOUR_BOT_TOKEN"

print("Bot starting...")    
@bot.event
async def on_ready():
    global guild_id
    for guild in bot.guilds:
        if guild.id == guild_id:
            await bot.register_application_commands(guild=guild)
    print(f"\nLogged in as {bot.user}\n")
    print("Guilds:")
    for guild in bot.guilds:
        print(f"- {guild.name} (id: {guild.id})")



@bot.command(    
    application_command_meta=commands.ApplicationCommandMeta(
        options=[
            discord.ApplicationCommandOption(
                name="text",
                type=discord.ApplicationCommandOptionType.string,
                description="Type the Text."
            ),
        ]
    )
)
@has_permissions(administrator=True)
async def send(ctx, *, text):
    await ctx.send(text)


@bot.command(    
    application_command_meta=commands.ApplicationCommandMeta(
        options=[
            discord.ApplicationCommandOption(
                name="message_id",
                type=discord.ApplicationCommandOptionType.string,
                description="The ID of the message.",
            ),
            discord.ApplicationCommandOption(
                name="label",
                type=discord.ApplicationCommandOptionType.string,
                description="Type in the label."
            ),
            discord.ApplicationCommandOption(
                name="role",
                type=discord.ApplicationCommandOptionType.role,
                description="Select the role."
            ),
            discord.ApplicationCommandOption(
                name="color",
                choices=[
                    discord.ApplicationCommandOptionChoice(name="Green", value="Green"),
                    discord.ApplicationCommandOptionChoice(name="Blue", value="Blue"),
                    discord.ApplicationCommandOptionChoice(name="Red", value="Red"),
                    discord.ApplicationCommandOptionChoice(name="Default (Grey)", value="Grey"),
                ],
                type=discord.ApplicationCommandOptionType.string,
                description="The color of the button.",
                required=False
            )
        ]
    )
)
@has_permissions(administrator=True)
async def button (ctx, message_id: str, label: str, role: discord.Role, color: str = "Grey"):
    """
    With this command you can create a button on a specified message.
    This can be used for example accepting the rules on your server.
    After clicking the button, the Bot will add or remove (toggle) the role.
    
    Usage Example:
        
       |  Command  |    Message ID    | Role | Text |
        /rolebutton 974005384509550653 Member Accept

    
    """
    

    message_id = int(message_id)
    msg = await ctx.channel.fetch_message(message_id)
    
    if any(str(emoji) in label for emoji in ctx.guild.emojis):
        components = discord.ui.MessageComponents(
            discord.ui.ActionRow(
                discord.ui.Button(emoji=label, custom_id="rolemsg-" + str(role.id) , style=switch(color)),
            )
        )
    else:
        components = discord.ui.MessageComponents(
                discord.ui.ActionRow(
                    discord.ui.Button(label=label, custom_id="rolemsg-" + str(role.id) , style=switch(color)),
                )
            )
    msg_components = msg.components.to_dict()
    add_components = components.to_dict()
    list = []
    if msg_components:
        for x in msg_components[0]['components']:
            list.append(x)
    for x in add_components[0]['components']:
        list.append(x)
    list = [{'type': 1, 'components': list}]
    newComps = discord.ui.MessageComponents.from_dict(list)
    try: 
        await msg.edit(components=newComps)
    except:
        pass
    await ctx.send(f"<a:success:937438369984708678> [{label}] is now for the Role <@&{role.id}>", ephemeral=True)


@bot.listen()
async def on_component_interaction(interaction):
    member = interaction.user
    if interaction.custom_id.startswith("rolemsg-"):
        role_id = int(interaction.custom_id.split("-", 1)[1])
        role = discord.utils.get(interaction.message.channel.guild.roles, id=role_id)
        if member.get_role(role_id) is None:
            await member.add_roles(discord.utils.get(member.guild.roles, id=role_id))
            embed = discord.Embed(title=" ", description="<a:success:937438369984708678> Successfully added role \"**" + role.name + "**\"", color=0x65f60a)
            await interaction.response.send_message(embed=embed, ephemeral=True)
        else: 
            await member.remove_roles(discord.utils.get(member.guild.roles, id=role_id))
            embed = discord.Embed(title=" ", description="<a:success:937438369984708678> Successfully removed role \"**" + role.name + "**\"", color=0xf60a0a) 
            await interaction.response.send_message(embed=embed, ephemeral=True)

def switch(argument):
    case = {
        "Green": discord.ui.ButtonStyle.success,
        "Blue": discord.ui.ButtonStyle.primary,
        "Red": discord.ui.ButtonStyle.danger,
        "Grey": discord.ui.ButtonStyle.secondary
    }
    return case[argument]


bot.run(bot_token)
