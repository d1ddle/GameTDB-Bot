![# GameTDB](https://github.com/d1ddle/GameTDB-Bot/blob/main/img/GameTDB-400-1.png?raw=true)
![# -Bot](https://raw.githubusercontent.com/d1ddle/GameTDB-Bot/main/img/discord.png?raw=true)

### Scrape ***GameTDB*** and ***Khinsider*** for Game ***title covers***, descriptions, metadata and ***Game OST's!***

Use the prefix `game` with one or multiple search terms, use an optional {console} term, {results page number}, and the GameTDB-Bot does the heavy lifting!

![# Screenshot](https://github.com/d1ddle/GameTDB-Bot/blob/main/img/gtdb%20-screenshot.png?raw=true)

## How do I use the Bot?
Simply invite the Bot to your discord server using [this link](https://discord.com/api/oauth2/authorize?client_id=824312967586906193&permissions=268815424&scope=bot) (you must have the Manage Server permission) and enter the commands into a channel the Bot has access to.


### Command
> **`game {console} {search terms} {results page no.}`**


### Minimal Use
> **`game {search terms}`**


## Terms
#### {console}
> **`wii`, `ps3`, `ds`, `switch`, `3ds`, `wiiu`**
> If none are specified, the bot searches all, in the order above.
> Results page number still works when searching through all consoles.

#### {search_terms}
> Any Game Title or Game ID
>> **`Mario`**, **`Mario_Kart_Wii`**, **`RMCE01`**
> Multiple Search Terms must be separated by Underscores _

#### {results page no.}
> As searches return more than 1 result, results are split into pages.
> There are 10 results per page.
> The results page number specifies which 10 results to send over.
> If none is specified, page 1 sends.
>> **`Is an integer.`**


### Help
> **`gtdb`** for help!

### Note: Not an official GameTDB or Khinsider Discord Bot. 


## Invite link
> https://discord.com/api/oauth2/authorize?client_id=824312967586906193&permissions=268815424&scope=bot

## Support Server
> https://discord.gg/BuhtqP9

## So, where do I host this bot?
I host my bot on [replit.com](https://replit.com/@d1ddle/GamesTDB-Bot#main.py) at no cost to me at all. For FREE. Seriously -
Using the Python Flask module, I can set up a temporary website hosted by the repl, and a free service called [UptimeRobot](https://uptimerobot.com/) pings the website, keeping the repl awake. This is needed because replit.com shuts down repls that have been inactive for an hour. 
The website for my bot is as follows: https://GamesTDB-Bot.d1ddle.repl.co

### You can view this script above - it's the keep_alive.py
