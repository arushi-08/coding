class MyCalendar:

    def __init__(self):
        self.booking = []
        heapify(self.booking)

    def book(self, start: int, end: int) -> bool:
        
        if not self.booking:
            heappush(self.booking, (-end, start))
            return True
        
        
        if start >= -self.booking[0][0]:
            heappush(self.booking, (-end, start))
            return True
        
        for b in self.booking:
            ed, st = b
            ed = -ed
            if st <= start and start < ed: # starttime inside existing booking
                return False
            if st < end and end <= ed: # endtime inside existing booking
                return False
            if start <= st and ed <= end: # completely covering booking
                return False

        heappush(self.booking, (-end, start))
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
