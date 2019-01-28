# Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого это цифры числа.
# Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

from collections import deque

class Hex:
    def __init__(self):
        self._left_number = ""
        self._right_number = ""
        self._buffer = "0"
        self._hex_sum = {
            "0": { "0": "0", "1": "1", "2": "2", "3": "3", "4": "4", "5": "5", "6": "6", "7": "7", "8": "8", "9": "9", "A": "A", "B": "B", "C": "C", "D": "D", "E": "E", "F": "F" },
            "1": { "0": "1", "1": "2", "2": "3", "3": "4", "4": "5", "5": "6", "6": "7", "7": "8", "8": "9", "9": "A", "A": "B", "B": "C", "C": "D", "D": "E", "E": "F", "F": "10" },
            "2": { "0": "2", "1": "3", "2": "4", "3": "5", "4": "6", "5": "7", "6": "8", "7": "9", "8": "A", "9": "B", "A": "C", "B": "D", "C": "E", "D": "F", "E": "10", "F": "11" },
            "3": { "0": "3", "1": "4", "2": "5", "3": "6", "4": "7", "5": "8", "6": "9", "7": "A", "8": "B", "9": "C", "A": "D", "B": "E", "C": "F", "D": "10", "E": "11", "F": "12" },
            "4": { "0": "4", "1": "5", "2": "6", "3": "7", "4": "8", "5": "9", "6": "A", "7": "B", "8": "C", "9": "D", "A": "E", "B": "F", "C": "10", "D": "11", "E": "12", "F": "13" },
            "5": { "0": "5", "1": "6", "2": "7", "3": "8", "4": "9", "5": "A", "6": "B", "7": "C", "8": "D", "9": "E", "A": "F", "B": "10", "C": "11", "D": "12", "E": "13", "F": "14" },
            "6": { "0": "6", "1": "7", "2": "8", "3": "9", "4": "A", "5": "B", "6": "C", "7": "D", "8": "E", "9": "F", "A": "10", "B": "11", "C": "12", "D": "13", "E": "14", "F": "15" },
            "7": { "0": "7", "1": "8", "2": "9", "3": "A", "4": "B", "5": "C", "6": "D", "7": "E", "8": "F", "9": "10", "A": "11", "B": "12", "C": "13", "D": "14", "E": "15", "F": "16" },
            "8": { "0": "8", "1": "9", "2": "A", "3": "B", "4": "C", "5": "D", "6": "E", "7": "F", "8": "10", "9": "11", "A": "12", "B": "13", "C": "14", "D": "15", "E": "16", "F": "17" },
            "9": { "0": "9", "1": "A", "2": "B", "3": "C", "4": "D", "5": "E", "6": "F", "7": "10", "8": "11", "9": "12", "A": "13", "B": "14", "C": "15", "D": "16", "E": "17", "F": "18" },
            "A": { "0": "A", "1": "B", "2": "C", "3": "D", "4": "E", "5": "F", "6": "10", "7": "11", "8": "12", "9": "13", "A": "14", "B": "15", "C": "16", "D": "17", "E": "18", "F": "19" },
            "B": { "0": "B", "1": "C", "2": "D", "3": "E", "4": "F", "5": "10", "6": "11", "7": "12", "8": "13", "9": "14", "A": "15", "B": "16", "C": "17", "D": "18", "E": "19", "F": "1A" },
            "C": { "0": "C", "1": "D", "2": "E", "3": "F", "4": "10", "5": "11", "6": "12", "7": "13", "8": "14", "9": "15", "A": "16", "B": "17", "C": "18", "D": "19", "E": "1A", "F": "1B" },
            "D": { "0": "D", "1": "E", "2": "F", "3": "10", "4": "11", "5": "12", "6": "13", "7": "14", "8": "15", "9": "16", "A": "17", "B": "18", "C": "19", "D": "1A", "E": "1B", "F": "1C" },
            "E": { "0": "E", "1": "F", "2": "10", "3": "11", "4": "12", "5": "13", "6": "14", "7": "15", "8": "16", "9": "17", "A": "18", "B": "19", "C": "1A", "D": "1B", "E": "1C", "F": "1D" },
            "F": { "0": "F", "1": "10", "2": "11", "3": "12", "4": "13", "5": "14", "6": "15", "7": "16", "8": "17", "9": "18", "A": "19", "B": "1A", "C": "1B", "D": "1C", "E": "1D", "F": "1E" }
        }

    def _sum(self, a, b):
        if(len(a) > 1 or len(b) > 1):
            raise ValueError('invalid parameter')
        return self._hex_sum[a][b]

    def _prepear_number(self, a, b):
        left = deque(a.upper())
        right = deque(b.upper())
        if(len(left) < len(right)):
            left, right = right, left
        right.extendleft("0" * (len(left) - len(right)))
        left.reverse()
        right.reverse()
        return (left, right)

    def _get_number(self, val):
        if(len(val) > 1):
            number = val[1]
            self._buffer = "1"
        else:
            number = val[0]
            self._buffer = "0"
        return number

    def addition(self, a, b):
        result = []
        self._buffer = "0"

        numbers = self._prepear_number(a, b)
        top_number = numbers[0]
        bottom_number = numbers[1]

        for i in range(len(top_number)):
            sum = self._sum(top_number[i], bottom_number[i])
            
            if(self._buffer == "1"):
                if(len(sum) > 1):
                    number = self._sum(sum[1], self._buffer)
                else:
                    n = self._sum(sum[0], self._buffer)
                    number = self._get_number(n)
            else:
                number = self._get_number(sum)

            result.append(number)

        if(self._buffer == "1"):
            result.append(self._buffer)

        return list(reversed(result))

    def multiplication(self, a, b):
        hex_number = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]

        top_number = a.upper()
        bottom_number = b.upper()
        if(len(top_number) < len(bottom_number)):
            top_number, bottom_number = bottom_number, top_number

        buffer = []
        i = 0
        for n in list(reversed(bottom_number)):
            if(n == "0"):
                continue

            temp = "0"
            for h in hex_number:
                if(h == n):
                    break
                temp = "".join(self.addition(temp, top_number))
            temp += "0" * i
            i += 1
            buffer.append(temp)

        result = "0"
        for part in buffer:
            result = "".join(self.addition(result, part))

        return list(result)


hex = Hex()

print(hex.addition("abff", "c1"))    # ['A', 'C', 'C', '0']
print(hex.addition("1fff", "2ff"))   # ['2', '2', 'F', 'E']
print(hex.addition("fff", "ffff"))   # ['1', '0', 'F', 'F', 'E']
print(hex.addition("157fe", "abff"))   # ['2', '0', '3', 'F', 'D']

print()
print(hex.multiplication("10a", "b3c"))  # ['B', 'A', 'C', '5', '8']
print(hex.multiplication("abff", "c1"))  # ['8', '1', 'A', 'B', '3', 'F']

