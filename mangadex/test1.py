def get_time(x: int) -> str:
    time_string = ''
    minute = second = 0

    second = x % 60
    x = x // 60

    minute = x % 60
    x = x // 60

    if x != 0:
        time_string = f'{x:02}:'

    time_string += f"{minute:02}:{second:02}"
    return time_string


zero = 'zeroth'

big = [
    'one', 'two', 'three', "four", "five", "six", "seven", "eight", "nine",
    'ten'
]

one = [
    "first", "second", "third", "fourth", "fifth", "sixth", "seventh",
    "eighth", "ninth", 'tenth'
]

teen = [
    "eleventh", "twelfth", "thirteenth", "fourteenth", "fifteenth",
    "sixteenth", "seventeenth", "eighteenth", "nineteenth"
]

ten = [
    'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty',
    'ninety'
]

time = [f"00:00 - {zero} second"]

h, m, s = map(int, input().split())
t = h*3600 + m * 60 + s

for i in range(1, t + 1):
    s = [get_time(i), '-']

    if (i // 1000) != 0:
        if (x := i // 1000) <= 10:
            ind = x - 1
            s.append(big[ind])
        else:
            if 11 <= x <= 19:
                ind = x - 11
                s.append(teen[ind].replace('th', ''))
            else:
                tenth_ind = x // 10 - 2
                s.append(ten[tenth_ind])

                ones_ind = x % 10 - 1
                s.append(one[ones_ind])

        if i % 1000 == 0:
            s.append('thousandth second')
            time.append(" ".join(s))
            continue
        else:
            s.append("thousand")

            if i % 1000 <= 99:
                s.append('and')

    i = i % 1000
    if i // 100 != 0:
        ind = (i // 100) % 10 - 1
        if ind >= 0:
            s.append(big[ind])
            if i % 100 == 0:
                s.append('hundredth second')
                time.append(' '.join(s))
                continue
            else:
                s.append("hundred and")

    if 20 <= (x := i % 100) <= 99:
        tenth_ind = x // 10 - 2
        if x % 10 == 0:
            s.append(f'{ten[tenth_ind][:-1]}ieth second')
            time.append(' '.join(s))
            continue
        s.append(ten[tenth_ind])

        ones_ind = x % 10 - 1
        s.append(one[ones_ind])

    if 11 <= x <= 19:
        s.append(teen[(x % 10) - 1])

    if 1 <= x <= 10:
        s.append(one[x - 1])

    s.append('second')
    time.append(' '.join(s))

with open('test.txt', 'w') as fl:
    print('\n'.join(time), file=fl)