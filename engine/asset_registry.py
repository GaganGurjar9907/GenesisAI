class AssetRegistry:

    def __init__(self):

        self.assets = {}

    def register(self, category, name):

        if category not in self.assets:
            self.assets[category] = []

        self.assets[category].append(name)

        print(f"✅ Registered [{category}] -> {name}")

    def get_assets(self, category):

        return self.assets.get(category, [])

    def show(self):

        print("\n========== ASSET REGISTRY ==========\n")

        for category, items in self.assets.items():

            print(category)

            for item in items:

                print(f"   • {item}")

            print()