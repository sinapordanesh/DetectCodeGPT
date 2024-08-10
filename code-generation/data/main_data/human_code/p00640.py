class Page:
    def __init__(self, name, buttons):
        self.name = name
        self.buttons = buttons


class Button:
    def __init__(self, line):
        self.x1 = int(line[0])
        self.y1 = int(line[1])
        self.x2 = int(line[2])
        self.y2 = int(line[3])
        self.link = line[4]


class Buffer:
    def __init__(self, page):
        self.pointer = 0
        self.length = 0
        self.contents = [page]
        self.pages = {}

    def click(self, x, y):
        page = self.contents[self.pointer]
        for button in page.buttons:
            if button.x1 <= x <= button.x2 and button.y1 <= y <= button.y2:
                link = button.link
                self.contents = self.contents[:self.pointer+1]
                self.contents.append(self.pages[link])
                self.pointer += 1
                self.length = self.pointer

    def back(self):
        self.pointer = max(0, self.pointer - 1)

    def forward(self):
        self.pointer = min(self.length, self.pointer + 1)

    def show(self):
        print(self.contents[self.pointer].name)


def page_detail():
    name, bi = input().split()
    buttons = []
    for _ in range(int(bi)):
        buttons.append(Button(input().split()))
    page = Page(name, buttons)
    return page, name


while True:
    n = int(input())
    if n == 0:
        break
    input()
    pages = {}
    for i in range(n):
        page, name = page_detail()
        pages[name] = page
        if i == 0:
            buffer = Buffer(page)

    buffer.pages = pages

    m = int(input())
    for _ in range(m):
        s = input()
        if s == "show":
            buffer.show()
        elif s == "back":
            buffer.back()
        elif s == "forward":
            buffer.forward()
        else:
            _, x, y = s.split()
            buffer.click(int(x), int(y))


