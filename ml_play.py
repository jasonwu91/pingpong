"""
The template of the script for the machine learning process in game pingpong
"""

class MLPlay:
    def __init__(self, side):
        """
        Constructor

        @param side A string "1P" or "2P" indicates that the `MLPlay` is used by
               which side.
        """
        self.ball_served = False
        self.side = side

    def update(self, scene_info):
        """
        Generate the command according to the received scene information
        """
        if scene_info["status"] != "GAME_ALIVE":
            return "RESET"

        if not self.ball_served:
            self.ball_served = True
            return "SERVE_TO_LEFT"
        else:       

            if self.side == "1P":
                if scene_info['ball_speed'][0] > 0 and scene_info['ball_speed'][1] > 0:
                    #ball is moving towards 1p and right
                    exp_touch_x = 200-((scene_info['platform_1P'][1] - scene_info['ball'][1])/scene_info['ball_speed'][1]*scene_info['ball_speed'][0] + scene_info['ball'][0] - 200)
                    if exp_touch_x > 0 and exp_touch_x < 200:
                        if exp_touch_x > scene_info['platform_1P'][0]+5 and exp_touch_x < scene_info['platform_1P'][0]+35:
                            #if ball is expected to hit the board
                            return "NONE"
                        elif exp_touch_x > scene_info['platform_1P'][0]+35:
                            return "MOVE_RIGHT"
                        elif exp_touch_x < scene_info['platform_1P'][0]+5:
                            return "MOVE_LEFT"
                    elif exp_touch_x < 0:
                        exp_touch_x = 0-exp_touch_x
                        if exp_touch_x > scene_info['platform_1P'][0]+5 and exp_touch_x < scene_info['platform_1P'][0]+35:
                            #if ball is expected to hit the board
                            return "NONE"
                        elif exp_touch_x > scene_info['platform_1P'][0]+35:
                            return "MOVE_RIGHT"
                        elif exp_touch_x < scene_info['platform_1P'][0]+5:
                            return "MOVE_LEFT"
                    elif exp_touch_x > 200:
                        exp_touch_x = 200-(exp_touch_x-200)
                        if exp_touch_x > scene_info['platform_1P'][0] and exp_touch_x < scene_info['platform_1P'][0]+40:
                            #if ball is expected to hit the board
                            return "NONE"
                        elif exp_touch_x > scene_info['platform_1P'][0]+35:
                            return "MOVE_RIGHT"
                        elif exp_touch_x < scene_info['platform_1P'][0]+5:
                            return "MOVE_LEFT"

                elif scene_info['ball_speed'][0] < 0 and scene_info['ball_speed'][1] > 0:
                    #ball is moving towards 1p and left
                    exp_touch_x = 0-((scene_info['platform_1P'][1] - scene_info['ball'][1])/scene_info['ball_speed'][1]*scene_info['ball_speed'][0] + scene_info['ball'][0])
                    if exp_touch_x > 0 and exp_touch_x < 200:
                        if exp_touch_x > scene_info['platform_1P'][0]+5 and exp_touch_x < scene_info['platform_1P'][0]+35:
                            #if ball is expected to hit the board
                            return "NONE"
                        elif exp_touch_x > scene_info['platform_1P'][0]+35:
                            return "MOVE_RIGHT"
                        elif exp_touch_x < scene_info['platform_1P'][0]+5:
                            return "MOVE_LEFT"
                    elif exp_touch_x < 0:
                        exp_touch_x = 0-exp_touch_x
                        if exp_touch_x > scene_info['platform_1P'][0]+5 and exp_touch_x < scene_info['platform_1P'][0]+35:
                            #if ball is expected to hit the board
                            return "NONE"
                        elif exp_touch_x > scene_info['platform_1P'][0]+35:
                            return "MOVE_RIGHT"
                        elif exp_touch_x < scene_info['platform_1P'][0]+5:
                            return "MOVE_LEFT"
                    elif exp_touch_x > 200:
                        exp_touch_x = 200-(exp_touch_x-200)
                        if exp_touch_x > scene_info['platform_1P'][0]+5 and exp_touch_x < scene_info['platform_1P'][0]+35:
                            #if ball is expected to hit the board
                            return "NONE"
                        elif exp_touch_x > scene_info['platform_1P'][0]+35:
                            return "MOVE_RIGHT"
                        elif exp_touch_x < scene_info['platform_1P'][0]+5:
                            return "MOVE_LEFT"

                else:
                    return "NONE"

            elif self.side == "2P":
                if scene_info['ball_speed'][0] > 0 and scene_info['ball_speed'][1] < 0:
                    #ball is moving towards 2p and right
                    exp_touch_x = 200-((scene_info['platform_2P'][1] - scene_info['ball'][1])/scene_info['ball_speed'][1]*scene_info['ball_speed'][0] + scene_info['ball'][0] - 200)
                    if exp_touch_x > 0 and exp_touch_x < 200:
                        if exp_touch_x > scene_info['platform_2P'][0]+5 and exp_touch_x < scene_info['platform_2P'][0]+35:
                            #if ball is expected to hit the board
                            return "NONE"
                        elif exp_touch_x > scene_info['platform_2P'][0]+35:
                            return "MOVE_RIGHT"
                        elif exp_touch_x < scene_info['platform_2P'][0]+5:
                            return "MOVE_LEFT"
                    elif exp_touch_x < 0:
                        exp_touch_x = 0-exp_touch_x
                        if exp_touch_x > scene_info['platform_2P'][0]+5 and exp_touch_x < scene_info['platform_2P'][0]+35:
                            #if ball is expected to hit the board
                            return "NONE"
                        elif exp_touch_x > scene_info['platform_2P'][0]+35:
                            return "MOVE_RIGHT"
                        elif exp_touch_x < scene_info['platform_2P'][0]+5:
                            return "MOVE_LEFT"
                    elif exp_touch_x > 200:
                        exp_touch_x = 200-(exp_touch_x-200)
                        if exp_touch_x > scene_info['platform_2P'][0]+5 and exp_touch_x < scene_info['platform_2P'][0]+35:
                            #if ball is expected to hit the board
                            return "NONE"
                        elif exp_touch_x > scene_info['platform_2P'][0]+35:
                            return "MOVE_RIGHT"
                        elif exp_touch_x < scene_info['platform_2P'][0]+5:
                            return "MOVE_LEFT"

                elif scene_info['ball_speed'][0] < 0 and scene_info['ball_speed'][1] < 0:
                    #ball is moving towards 2p and left
                    exp_touch_x = 0-((scene_info['platform_2P'][1]+30 - scene_info['ball'][1])/scene_info['ball_speed'][1]*scene_info['ball_speed'][0] + scene_info['ball'][0])
                    if exp_touch_x > 0 and exp_touch_x < 200:
                        pass
                    elif exp_touch_x < 0:
                        exp_touch_x = 0-exp_touch_x
                    elif exp_touch_x > 200:
                        exp_touch_x = 200-(exp_touch_x-200)
                        
                    if exp_touch_x > scene_info['platform_2P'][0]+5 and exp_touch_x < scene_info['platform_2P'][0]+35:
                        #if ball is expected to hit the board
                        return "NONE"
                    elif exp_touch_x > scene_info['platform_2P'][0]+35:
                        return "MOVE_RIGHT"
                    elif exp_touch_x < scene_info['platform_2P'][0]+5:
                        return "MOVE_LEFT"

                else:
                    return "NONE"
            
            else:
                return "NONE"

            


    def reset(self):
        """
        Reset the status
        """
        self.ball_served = False
