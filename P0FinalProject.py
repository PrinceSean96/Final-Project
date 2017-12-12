import turtle
import random
import time

class Game():

    def __init__(self):
        self.places = {"Paris":(48.856614, 2.352222), "Japan":(36.204824, 138.252924), "Africa":(-8.783195, 34.508523),
                       "New Jersey":(40.058324, -74.405661), "Canada":(56.130366,-106.346771),
                       "New Zealand":(-40.900557, 174.885971), "Australia":(-25.274398, 133.775136)}

        self.current_place = random.choice(list(self.places.keys()))
        self.wn = turtle.Screen()
        self.wn.setup(width=1100, height=650, startx=0, starty=0)
        self.wn.bgpic("world-map.gif")
        self.wn.onclick(self.mark_place)
        self.t = turtle.Turtle()
        self.get_user_place()

        self.wn.mainloop()

    def mark_place(self, x, y):
        """
        #t = turtle
        :param x:
        :param y:
        :return:
        """
        # self.t = turtle.Turtle()
        self.t.goto(x, y)
        long = 195 * 2 * x / self.wn.window_width()
        lat = 120 * 2 * y / self.wn.window_height()
        print(long)
        print(lat)
        if self.check_for_winner(lat, long):
            self.t.write("Great job!")
            time.sleep(3)
            # FIXME go to next place
            self.current_place = random.choice(list(self.places.keys()))
            self.get_user_place()

        # if abs(lat - self.places["Paris"] [0]) < 10:
        #     print("Great Job!")
        # if abs(long - self.places["Paris"] [1]) < 10:
        #     print("Great Job!")
        # if abs(lat - self.places["Japan"] [0]) < 10:
        #     print("Great Job!")
        # if abs(long - self.places["Japan"] [1]) < 10:
        #     print("Great Job!")
        # if abs(lat - self.places["Africa"] [0]) < 10:
        #     print("Great Job!")
        # if abs(long - self.places["Africa"] [1]) < 10:
        #     print("Great Job!")
        # if abs(lat - self.places["New Jersey"] [0]) < 10:
        #     print("Great Job!")
        # if abs(long - self.places["New Jersey"] [1]) < 10:
        #     print("Great Job!")
        # if abs(lat - self.places["Canada"] [0]) < 10:
        #     print("Great Job!")
        # if abs(long - self.places["Canada"] [1]) < 10:
        #     print("Great Job!")
        # if abs(lat - self.places["New Zealand"] [0]) < 10:
        #     print("Great Job!")
        # if abs(long - self.places["New Zealand"] [1]) < 10:
        #     print("Great Job!")
        # if abs(lat - self.places["Australia"] [0]) < 10:
        #     print("Great Job!")
        # if abs(long - self.places["Australia"] [1]) < 10:
        #     print("Great Job!")

    def check_for_winner(self, lat, long):
        if abs(lat - self.places[self.current_place][0]) < 10 and abs(long - self.places[self.current_place][1] < 10):
            return True
        return False

    def get_user_place(self):
        """
         #self.place[input(...)] = (long,lat)
        :param longitude:
        :param latitude:
        :return:
        """

        self.t.clear()
        self.t.write('Where is {0}?'.format(self.current_place), move=False, align='center', font=('Arial', 40, 'normal'))
        self.am_i_clicked = False

    def am_i_clicked(self):
        self.am_i_clicked = True



    def check_winner(self):
        print("Youre Correct!")

def main():
    map_places = Game()

main()
