class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        
        # angle between 1 minute is 6 degree

        # 3:00 - 90 degrees
        # angle between 5 minutes - 30 degrees
        # angle between each minute - 6 degrees

        angle_per_minute = 6
        # how many minutes between hour and minute needles
        # hour * 5 % 60 is minute equivalent

        # minutes is 30 - hour is 2.5
        # minute is 15 - hour is 1.5
        # minute is 1 - hour is 2.5/30


        # min is 30 | hour is ((hour * 5 )% 60) + 2.5
        # every 30 min incremenet causes 2.5 incremenet in hour
        # 1 min incremenet causes 2.5/30 incremenet

        # min is 15 | hour is ((hour * 5 )% 60) + 1.25

        
        # 1 min increment will cause 0.1 incremenet

        hour_pos = ((hour * 5)% 60) + ((2.5/30) * minutes)
        
        if hour_pos < minutes:
            min_bet_needles_time_1 = minutes - hour_pos
            min_bet_needles_time_2 = hour_pos - (minutes-60)
            min_bet_needles = min(min_bet_needles_time_1, min_bet_needles_time_2)
        else:
            min_bet_needles_time_1 = hour_pos - minutes
            min_bet_needles_time_2 = minutes - (hour_pos-60)
            min_bet_needles = min(min_bet_needles_time_1, min_bet_needles_time_2)

        angle = angle_per_minute * min_bet_needles
        
        return angle

        # 1:57
        # 1 hour = 5 + (2.5/30) * 57 = 9.75
        # 57 min = 57

        # 57 min vs 57-60

        # 2nd case - hour needle behind 12, min needle ahead of 12
        # e.g. 11:05
        # 55 + (2.5/30)*5 = 55.4166       vs (55.4166 - 60)
        #                  (time from 55) vs (time from 60)

        # 3:30
        # 15 + 2.5 = 17.5
        # 30
        # diff = 30-17.5 = 12.5
        # 12.5 * 6 = 75

        # 3:15
        # 15 + 1.25 = 16.25 - hour
        # 15 - minute
        # 1.25 min - difference between needles
        # 1 minute - 6 degrees
        # 1.25 - 6 * 1.25 = 7.5

        # 3:30 | x = 0.085
        # 15+2.5 = 17.5

