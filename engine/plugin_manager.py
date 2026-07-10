class PluginManager:

    def __init__(self):

        self.plugins = {}

    def register(self, name, plugin):

        self.plugins[name] = plugin

        print(f"✅ Plugin Registered -> {name}")

    def load(self, name):

        if name in self.plugins:

            print(f"Loading Plugin -> {name}")

            return self.plugins[name]

        print(f"❌ Plugin Not Found -> {name}")

        return None

    def list_plugins(self):

        print("\n========== PLUGINS ==========\n")

        if not self.plugins:

            print("No Plugins Installed")

            return

        for plugin in self.plugins:

            print(plugin)