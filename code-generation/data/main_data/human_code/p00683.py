class TextEditor:
    cur_w = 0
    cur_c = 0

    def __init__(self, txt):
        self.words = txt.split(' ')
        self.queries = {
            'forward char': self.forward_char,
            'forward word': self.forward_word,
            'backward char': self.backward_char,
            'backward word': self.backward_word,
            'delete char': self.delete_char,
            'delete word': self.delete_word
        }

    def query(self, q):
        if q[0] == 'i':
            txt = q.split(maxsplit=1)[1][1:-1]
            self.insert(txt)
        else:
            self.queries[q]()

    def forward_char(self):
        if self.cur_c < len(self.words[self.cur_w]):
            self.cur_c += 1
        elif self.cur_w < len(self.words) - 1:
            self.cur_w += 1
            self.cur_c = 0
        else:
            pass

    def forward_word(self):
        if self.cur_c < len(self.words[self.cur_w]):
            self.cur_c = len(self.words[self.cur_w])
        elif self.cur_w < len(self.words) - 1:
            self.cur_w += 1
            while not len(self.words[self.cur_w]) and self.cur_w < len(self.words) - 1:
                self.cur_w += 1
            self.cur_c = len(self.words[self.cur_w])
        else:
            pass

    def backward_char(self):
        if self.cur_c > 0:
            self.cur_c -= 1
        elif self.cur_w > 0:
            self.cur_w -= 1
            self.cur_c = len(self.words[self.cur_w])
        else:
            pass

    def backward_word(self):
        if self.cur_c > 0:
            self.cur_c = 0
        elif self.cur_w > 0:
            self.cur_w -= 1
            while not len(self.words[self.cur_w]) and self.cur_w > 0:
                self.cur_w -= 1
        else:
            pass

    def insert(self, txt):
        st = txt.split(' ')
        new_words = self.words[:self.cur_w]
        if len(st) > 1:
            cw = self.words[self.cur_w]
            new_words.append(cw[:self.cur_c] + st[0])
            new_words.extend(st[1:-1])
            new_words.append(st[-1] + cw[self.cur_c:])
            self.cur_c = len(st[-1])
        else:
            cw = self.words[self.cur_w]
            new_words.append(cw[:self.cur_c] + st[0] + cw[self.cur_c:])
            self.cur_c = self.cur_c + len(st[0])
        new_words.extend(self.words[self.cur_w + 1:])
        self.cur_w = self.cur_w + len(st) - 1
        self.words = new_words

    def delete_char(self):
        cw = self.words[self.cur_w]
        if self.cur_c < len(cw):
            self.words[self.cur_w] = cw[:self.cur_c] + cw[self.cur_c + 1:]
        elif self.cur_w < len(self.words) - 1:
            if len(cw):
                nw = self.words.pop(self.cur_w + 1)
                self.words[self.cur_w] = cw + nw
            else:
                self.words.pop(self.cur_w)
        else:
            pass

    def delete_word(self):
        if self.cur_c < len(self.words[self.cur_w]):
            self.words[self.cur_w] = self.words[self.cur_w][:self.cur_c]
        elif self.cur_w < len(self.words) - 1:
            tmp_w = self.cur_w + 1
            while tmp_w < len(self.words) and not len(self.words[tmp_w]):
                tmp_w += 1
            if tmp_w < len(self.words):
                del self.words[self.cur_w + 1:tmp_w + 1]

    def output(self):
        words = self.words.copy()
        words[self.cur_w] = self.words[self.cur_w][:self.cur_c] + '^' + \
                            self.words[self.cur_w][self.cur_c:]
        print(*words)


n = int(input())
for _ in range(n):
    te = TextEditor(input().strip())
    q = int(input())
    for _ in range(q):
        te.query(input().strip())
    te.output()