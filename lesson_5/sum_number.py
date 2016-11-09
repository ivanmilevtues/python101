import sys


def sum_file_nums():
    buffer_sum = ''
    num_list = []
    with open(sys.argv[1], "r") as f:
        buffer_sum = f.read()
    f.closed
    num_list = buffer_sum.split(' ')
    if num_list[len(num_list) - 1] == '\n':
        num_list.pop(len(num_list) - 1)
    for i in range(len(num_list)):
        num_list[i] = int(num_list[i])
    return sum(num_list)


def main():
    print(sum_file_nums())

if __name__ == '__main__':
    main()
