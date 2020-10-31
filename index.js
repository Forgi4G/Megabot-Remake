const { Client, Collection } = require('discord.js');
const client = new Client();
const config = JSON.parse(JSON.stringify(require('./configuration.json')));

const fs = require('fs');

client.commands = new Collection();
client.aliases = new Collection();
client.categories = fs.readdirSync(`./src/commands`);

["commands"].forEach(handler => {
    require(`./src/handlers/${handler}`)(client);
});

client.on("ready", () => {
    console.log(`${client.user.username}#${client.user.discriminator} ---- Megabot-Remake`);
});

client.on("message", message => {
   if (message.author.bot) return;
   if (!message.guild) return;

   if (!message.content.startsWith(config["STANDARD"]["PREFIX"])) return;

    if (!message.member) message.member = message.guild.member(message);

    const args = message.content.slice(config["STANDARD"]["PREFIX"].length).trim().split(/ +/g);
    const cmd = args.shift().toLowerCase();

    if (cmd.length === 0) return;

    let command = client.commands.get(cmd);
    if (!command) command = client.commands.get(client.aliases.get(cmd));

    if (command) {
        command.run(client, message, args);
    }
});

client.login(config["SPECIAL"]["TOKEN"]).catch(error => console.log(error));