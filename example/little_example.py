from disco.bot import Plugin

class LittleExamplePlugin(Plugin):

    def load(self, ctx):
        # This is called when the plugin is loaded. Set variables here, etc.
        self.loaded = True

    @Plugin.command('isco')
    def on_ping(self, event):
        event.channel.send_message('This is disco!')

