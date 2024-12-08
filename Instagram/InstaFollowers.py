from WindowOperation import WindowOperation
from conf.MyLogger import customlogger

logger = customlogger("InstaFollowers")

class InstaFollowers:
    def __init__(self):
        self.removeCounter = 0

        self.windowOpObj = WindowOperation()

        self.followers_selected = None
        self.select_followers_x_coordinates = 810
        self.select_followers_y_coordinates = 210

        self.start_follower_x_coordinates = 910
        self.start_follower_y_coordinates = 360

        self.end_follower_x_coordinates = 910
        self.end_follower_y_coordinates = 650

        self.remove_follower_x_coordinates = 860
        self.remove_follower_y_coordinates = 380

        self.confirm_follower_x_coordinates = 720
        self.confirm_follower_y_coordinates = 560

        logger.info("Insta followers initiated")

    def select_followers(self):
        self.windowOpObj.click_at_coordinates(self.select_followers_x_coordinates, self.select_followers_y_coordinates)
        logger.info("Followers selected")

    def remove_followers(self, no_of_followers=5):
        remove_follower_y_coordinatescopy = self.remove_follower_y_coordinates
        for i in range(no_of_followers):
            self.windowOpObj.click_at_coordinates(self.remove_follower_x_coordinates, self.remove_follower_y_coordinates)
            self.remove_follower_y_coordinates += 60
            self.windowOpObj.add_delay(1)
            self.windowOpObj.click_at_coordinates(self.confirm_follower_x_coordinates, self.confirm_follower_y_coordinates)
            self.windowOpObj.add_delay(1)
            logger.info(f"Loop {self.removeCounter+1}, follower {i+1} removed!")
        self.removeCounter += 1
        self.remove_follower_y_coordinates = remove_follower_y_coordinatescopy


        # first remove 860, 380
        # second remove 860 440
        # third remove 860 500
        # fourth remove 860 560
        # fifth remove 860 620

        # confirm 720 560

    def start(self, counter):
        self.windowOpObj.add_delay()
        self.windowOpObj.change_tab()
        self.windowOpObj.add_delay()
        if self.followers_selected is None or self.followers_selected == False:
            self.select_followers()
            self.followers_selected = True
            self.windowOpObj.add_delay(2)
            self.windowOpObj.scroll(self.start_follower_x_coordinates, self.start_follower_y_coordinates, 40)
        for _ in range(counter):
            self.windowOpObj.scroll(self.start_follower_x_coordinates, self.start_follower_y_coordinates, 1)
            self.remove_followers()
            self.windowOpObj.add_delay(3)


    @staticmethod
    def clean_up():
        """Cleanup resources"""
        logger.info("cleanup")