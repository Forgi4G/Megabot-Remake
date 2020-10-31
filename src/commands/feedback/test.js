module.exports = {
    name: "test",
    category: "feedback",
    aliases: [],
    description: "Testing command",
    on: true,
    run: async (client, message, args) => {
        message.channel.send("This test worked.");
    }
}