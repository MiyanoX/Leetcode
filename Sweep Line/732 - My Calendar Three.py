class MyCalendarThree:

    def __init__(self):
        self.layers = [[]]

    def book(self, start: int, end: int) -> int:
        event = [start, end]
        
        print(self.layers, len(self.layers))
        print("\n")
        print(event)
        
        
        for layer in self.layers:
            if not self.intersect(event, layer):
                layer.append(event)
                return len(self.layers)
        
        self.layers.append([event])
        return len(self.layers)
        
            
    def intersect(self, new_event: list, layer: list) -> bool:
        for event in layer:
            if not(new_event[0] >= event[1] or new_event[1] <= event[0]):
                return True
        return False
                


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)