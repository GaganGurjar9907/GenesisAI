class DecisionEngine:

    def choose(self, prompt):

        prompt = prompt.lower()

        if "gta" in prompt:
            return "Open World"

        if "racing" in prompt:
            return "Racing"

        if "fps" in prompt:
            return "Shooter"

        return "General"