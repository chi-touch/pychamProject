class SevenSegment:
    def displays(self, number):
        if len(number) != 8:
            raise ValueError("invalid number")

        list1 = []
        list1 += number
        self.horizontal(list1[0])

        self.vertical(list1[5], list1[1])
        self.horizontal(list1[6])
        self.vertical(list1[4], list1[2])
        self.horizontal(list1[3])

    def check_lastNumber(self, number):
        for num in number:
            if num != "0" or num != 1:
                raise BaseException("invalid number")

    def horizontal(self, digit):
        if digit == "1":
            return "# # # # "

    def vertical(self, digit, digit2):
        if digit == "1" and digit2 == "1":
            for num in range(4):
                return "#    #"

        elif digit == "0" and digit2 == "1":
            for num in range(4):
                return "      #"
        elif digit == "1" and digit2 == "0":
            for num in range(4):
                return "#      "


display = SevenSegment()
answer = input("Enter a number: ")
display.displays(answer)
