class Colors:
    def __init__(self, color):
        self.color = color

    def __enter__(self):
        if self.color == "pink":
            print("\033[95m", end="")
        if self.color == "blue":
            print("\033[94m", end="")
        if self.color == "grey":
            print("\033[90m", end="")
        if self.color == "red":
            print("\033[91m", end="")
        if self.color == "green":
            print("\033[92m", end="")
        if self.color == "yellow":
            print("\033[93m", end="")
        if self.color == "turquoise":
            print("\033[96m", end="")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("\033[0m", end="")


with Colors("pink"):
    print("printed in pink")

print("printed in default color")

with Colors("blue"):
    print("printed in blue")

print("printed in default color")

with Colors("grey"):
    print("printed in grey")

print("printed in default color")

with Colors("red"):
    print("printed in red")

print("printed in default color")

with Colors("green"):
    print("printed in green")

print("printed in default color")

with Colors("yellow"):
    print("printed in yellow")

print("printed in default color")

with Colors("turquoise"):
    print("printed in turquoise")

print("printed in default color")
