import sys


def draw_line(tick_length, label=''):
    line = '-'*tick_length
    if label:
        line += ' ' + label
    print(line)


def draw_interval(tick_length):
    if tick_length > 0:
        draw_interval(tick_length-1)
        draw_line(tick_length)
        draw_interval(tick_length-1)


def draw_ruler(inches, tick_length):
    draw_line(tick_length, '0')
    for i in range(1, inches+1):
        draw_interval(tick_length-1)
        draw_line(tick_length, str(i))
    print()

if __name__ == '__main__':
    print("This program prints out an english ruler(scale) with user provided values for number of inches and major"
          " tick length.")
    try:
        num_inches = int(sys.argv[1])
        major_tick_length = int(sys.argv[2])
        draw_ruler(num_inches, major_tick_length)
    except ValueError:
        print("please provide integer values only for number of inches and major tick length.")
