# def str_to_list(st, devider):
#     result = []
#     directory_string = ''
#     for index in range(len(st)):
#         if st[index] == devider:
#             for sub_index in range(index - 1, 0, -1):
#                 if st[sub_index] != devider:
#                     directory_string += st[sub_index]
#                 else:
#                     break
#             result.append(directory_string[::-1])
#             directory_string = ''
#     return result


def reduce_file_path(path):
    result = ''
    path_list = []
    # Change the function with the build in from python3
    path_list = path.split('/')
    for index in range(len(path_list)):
        if path_list[index] == '..':
            del path_list[index - 1]
            index -= 1
    return result

print(reduce_file_path("/srv/../"))
print(reduce_file_path("/srv/../srv/../srv/../"))
print(reduce_file_path("/srv/././././"))
print(reduce_file_path("/srv/www/htcdocs/wtf"))
print(reduce_file_path("///////////////////"))
print(reduce_file_path("/etc//wtf/"))
