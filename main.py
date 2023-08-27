import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
player.create_player()
car_manager = CarManager()
scoreboard= Scoreboard()
screen.listen()
screen.onkey(player.move_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    #dectect collision with a car
    for car in car_manager.all_cars:
        if player.distance(car)< 30:
            game_is_on = False
            scoreboard.game_over()

    #make the turtle go faster after each level
    if player.ycor()>280:
        player.goto(0, -280)
        car_manager.move_faster()
        scoreboard.update_score()


screen.exitonclick()
