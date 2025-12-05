class Computer:
    def __init__(self, screen_diagonal, model):
        self.model = model
        self.screen_diagonal = screen_diagonal
        self.state = "off"

    def turn_on(self):
        if self.state == "off":
            print(f"Computer {self.model} is turned on")

    def turn_off(self):
        if self.state == "on":
            print(f"Computer {self.model} is turned off")


computer_asus_zenbook = Computer(screen_diagonal=16, model="Asus Zenbook")
computer_asus_vivobook = Computer(screen_diagonal=16, model="Asus Vivobook")
computer_lenovo_yoga = Computer(screen_diagonal=14, model="Lenovo Yoga")

print(computer_lenovo_yoga.model, computer_lenovo_yoga.screen_diagonal)
print(computer_asus_zenbook.model, computer_asus_zenbook.screen_diagonal)

computer_asus_vivobook.turn_on()
computer_asus_vivobook.turn_off()
computer_asus_vivobook.turn_off() 

