class Company:
    def __init__(self,name):
        self.name = name
        self.marks = []
        self.average = 0

    def rate(self,studentName,score):
        marked = False
        for mark in self.marks:
            if mark[1] == studentName:
                print ("You already rate the company")
                marked=True

        if not marked:
            m = [studentName,score]
            self.marks.append(m)
            self.setAverage()

    def getRates(self):
        for mark in self.marks:
            print ("Student Name: " + mark[0] + " - Mark: "  + str(mark[1]))

    def removeRate(self,studentName):
        for mark in self.marks:
            if mark[0] == studentName:
                self.marks.remove(mark)
        self.setAverage()

    def setAverage(self):
        sum = 0
        for mark in self.marks:
            sum += mark[1]
        self.average = sum/len(self.marks)

    def getAverage(self):
        return self.average
