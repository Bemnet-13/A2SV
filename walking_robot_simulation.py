class Robot:

    def __init__(self, width: int, height: int):
        self.grid = [[x, y] for x in range(width) for y in range(height)]
        self.position = [0, 0]
        self.x_max = self.grid[-1][0]
        self.y_max = self.grid[-1][1]

    def step(self, num: int) -> None:

        while num > 0:
                if self.getDir() == "East":
                    self.position[0] += 1
                    num -= 1
                elif self.getDir() == "North":
                    self.position[1] += 1
                    num -= 1
                
                
                elif self.getDir() == "West":
                    self.position[0] -= 1
                    num -= 1
                else:
                    self.position[1] -= 1
                    num -= 1
                # print(self.position)
    def getPos(self):
        return self.position

    def getDir(self) -> str:
        if self.position[0] < self.x_max and self.position[1] == 0:
            return "East"
        elif self.position[0] == self.x_max and self.position[1] < self.y_max:
            return "North"
        elif self.position[0] > 0 and self.position[1] == self.y_max:
            return "West"
        else:
            return "South"

trial = Robot(20,13)
trial.step(12)
trial.step(21)
print(trial.getPos())
trial.step(17)

print(trial.getPos())

# ["Robot","step","step","getPos","getDir","step","getPos","getDir","getPos","getDir"]