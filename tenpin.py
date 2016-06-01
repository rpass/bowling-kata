class Game:
    def __init__(self):
        self.rolls = []

    def roll(self, pins):
        self.rolls.append(pins)

    def score(self):
        total = 0
        for i in range(len(self.rolls) / 2):
            frame_total = self.rolls[i*2] + self.rolls[i*2 + 1]
            total += frame_total

            if frame_total == 10:
                total += self.rolls[i*2 + 2]

        return total
