class Solution:
    def reformatDate(self, date: str) -> str:

        dates = date.split()[::-1]
        dates[0] = dates[0]
        dates[-1] = dates[-1][:-2].zfill(2)
        month_dict = {"Jan":1, "Feb":2, "Mar":3, "Apr":4, "May":5, "Jun":6, "Jul":7,
        "Aug":8, "Sep":9, "Oct":10, "Nov":11, "Dec":12}
        dates[1] = str(month_dict[dates[1]]).zfill(2)
        print(dates)
        return f"{dates[0]}-{dates[1]}-{dates[2]}"
