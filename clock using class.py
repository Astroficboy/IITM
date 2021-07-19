class TimeConverter:
    def __init__(self,time):
        self.time=time
    def Second_to_Minutes(self):
        m = self.time//60
        s = self.time % 60
        return (str(m)+' min '+str(s)+' sec')
    def Second_to_Hours(self):
        m = self.time//60
        s = self.time % 60
        h = m // 60
        m = m % 60
        return (str(h)+' hr '+str(m)+' min '+str(s)+' sec')
    def Second_to_Days(self):
        m = self.time//60
        s = self.time % 60
        h = m // 60
        m = m % 60
        d = h // 24
        h = h % 24
        return (str(d)+' days '+str(h)+' hr '+str(m)+' min '+str(s)+' sec')
    
sec = int(input())
a = TimeConverter(sec)
print(a.Second_to_Minutes())
print(a.Second_to_Hours())
print(a.Second_to_Days())