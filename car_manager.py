from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.all_cars =[]
        self.level=1


    def create_car(self):
        random_chance = random.randint(1,6)
        if random_chance==1:
            new_car = Turtle("square")
            new_car.shapesize(1, 2)
            #new_car.hideturtle()
            new_car.penup()
            new_car.color(random.choice(COLORS))
            starting_y = random.randint(-250, 250)
            new_car.goto(300,starting_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE)

    def move_faster(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE+MOVE_INCREMENT* int(self.level))
        self.level+=1





