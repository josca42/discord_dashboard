# Discord dashboard

This project currently contains code for daily scraping of a discord server, where the results are dumped to a sqlite db. The different tables in the sqlite db are daily dumped to both a parquet and a csv file.


### Get data

The scraping is currently on an ubuntu server. For access to the server send me a message with your public ssh key. Once I have added your ssh key to the list of authorized keys then the data can be downloaded using the following command. 

```
scp -r root@159.223.219.5:/root/data/ . # Download all data

scp -r root@159.223.219.5:/root/data/database . # Only db
scp -r root@159.223.219.5:/root/data/file_dumps . # Only file dumps
```

### Run code

Once I've added the ssh key to the list of authorized keys then you have root access to the server. You are then more than welcome to use the server to develop from.

In order to run the project install the src folder as a python package by running the following command in the root of the project directory.

```
pip install -e .
```

The code for extracting data from a discord server is in the folder src/data/discord2db. The discord server message history is downloaded using the [DiscordChatExpoter](https://github.com/Tyrrrz/DiscordChatExporter). The downloaded data is then processed and stored in a sqlite db.

### TODO
- [ ] Currently only dumps messages from channels and not threads. Fix by getting thread ID and use discordChatExporter.
- [ ] Missing link between reaction and user. Hence, not possible to distiungish wether I reacted to a message or Balaji did.

### Design ideas
Discord is "the virtual/online capital". Hence, create dashboard as metalayer around discord and then link back to discord. For instance instead of creating comment functionality on the dashboard then if people want to comment then create a thread in discord and subsequently link further comments to that discord thread. 

Use discord bot to allow easy navigation from discord to dashboard by adding various slash (/) commands and from dashboard to discord by adding links. Discord links have the following format https://discord.com/channels/>guild_id/>channel_id</>message_id<
