#! /usr/bin/python3
# -*- coding utf-8 -*-
# (c) 2021 Fomenko A V

class SixRows():
    def __init__(self, input_str):
        self.input_str = input_str

    def coding(self):
        new_str = ""
        output_str = ""
        count = []

        self.input_str = self.input_str.replace(" ", "")

        for i in range(0, 6):
            n = i
            while True:
                try:
                    new_str += self.input_str[n]
                    n += 6
                except Exception as e:
                    break

        for i in range(0, 6):
            if i < (len(new_str) % 6):
                count.append(int(len(new_str) / 6) + 1)
            else:
                count.append(int(len(new_str) / 6))

        n = 0
        for i in count:
            output_str += new_str[n:n+i] + " "
            n += i

        return output_str.strip()

    def decoding(self):
        word_list = self.input_str.split(" ")
        new_str = ""

        for i in range(0, 6):
            for word in word_list:
                try:
                    new_str += word[i]
                except Exception as e:
                    pass

        return new_str
