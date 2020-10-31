const { readdirSync } = require('fs');

module.exports = client => {
    readdirSync(`src/commands`).forEach(dir => {
        const commands = readdirSync(`src/commands/${dir}/`).filter(f => f.endsWith(".js"));
        console.log('------------------------');
        for (let file of commands) {
            let pull = require(`../commands/${dir}/${file}`);

            if (pull.name && pull.on) {
                client.commands.set(pull.name, pull);
                console.log(file, "-", "Approved")
            } else {
                continue;
            }

            if (pull.aliases && Array.isArray(pull.aliases)) {
                pull.aliases.forEach(alias => client.aliases.set(alias, pull.name));
            }
        }
        console.log('------------------------');
    });
}