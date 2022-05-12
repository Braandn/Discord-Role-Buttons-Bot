# Discord Role Buttons Bot

## About the Bot:
**With this Bot you can add Role buttons to your Discord Server**

This is the new Version of Reaction Roles.

Simple as that you just now have **buttons** instead of **reactions**.

<br>

## How does it look like:

Example: 

![grafik](https://user-images.githubusercontent.com/5453796/168111030-494ae7c8-3935-4d58-a9eb-ab614ecba913.png)



__You can choose Button colors__:

>
> **Grey** (Default)
>
> 🟢 **Green** 
>
> 🔵 **Blue** 
>
> 🔴 **Red**

<br>

## How to install:
> Install the required package: 
```
python3 -m pip install -U novus
```
> Edit Line 12 / 13 in Bot.py

https://github.com/Braandn/Discord-Role-Buttons-Bot/blob/46e2f535c1c49d7b4e69ee248dd6d44adc2b5c75/Bot.py#L12-L13

> Then start the Bot
```
python3 Bot.py
```

This is made with Discord Novus to use SlashCommands


## Usage:
![grafik](https://user-images.githubusercontent.com/5453796/168111287-61a837ab-484c-4fdb-aa44-210ddce690fe.png)

You can use Text, Emojis and Server Emojis for the buttons.
```
/button message_id label role color
```

```
message_id:     Right click on the message > "Copy ID" 
                (Note: Developer Mode needs to be activated)

label:          Your Text / Emoji

role:           Select the Role from the dropdown

color:          Select a Color from the dropdown
```
⚠️ Only working for messages from the bot

You can use `/send text` or `_send text with newline` to send a message with the bot.
