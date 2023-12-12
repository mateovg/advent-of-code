# Takes out a random amount of cubes, shows them, and puts them back
# Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
# Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
# Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
# Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
# Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
# Which games are possible if there are only
# 12 red, 13 green, and 14 blue

# return the sum of the IDs of games that are possible

def parse_line(line):
    # return game id: [red, green, blue]
    game_id = ""
    cubes = [0, 0, 0]
    line = line.split()
    for i in range(len(line)):
        if line[i] == "Game":
            game_id = int(line[i+1][:-1])
            i += 1

        color = parse_color(line[i])
        if color != -1:
            cubes[color] += int(line[i-1])

        if line[i][-1] == ";":
            if not check_if_valid(cubes):
                return 0
            cubes = [0, 0, 0]
    # one last check
    if not check_if_valid(cubes):
        return 0
    return game_id


def parse_color(color):
    if color[-1] == ";" or color[-1] == ",":
        color = color[:-1]
    if color == "red":
        return 0
    elif color == "green":
        return 1
    elif color == "blue":
        return 2
    else:
        return -1


def check_if_valid(cubes):
    if cubes[0] > 12 or cubes[1] > 13 or cubes[2] > 14:
        return False
    return True


def power_set_cubes(line):
    power = 1
    cubes = [[], [], []]
    line = line.split()
    for i in range(len(line)):
        color = parse_color(line[i])
        if color != -1:
            cubes[color].append(int(line[i-1]))
    for cube in cubes:
        power *= max(cube, default=0)
    return power


def main():
    sum = 0
    power = 0
    with open('input.txt') as f:
        for line in f:
            sum += parse_line(line.strip())
            power += power_set_cubes(line.strip())
    print(sum)
    print(power)


main()
