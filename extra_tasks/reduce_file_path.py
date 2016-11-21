def reduce_file_path(path):
    result = []
    path_list = []
    str_res = ''
    # Change the function with the build in from python3
    path_list = path.split('/')
    # print(path_list)
    for i in range(len(path_list)):
        # result.append('/')
        if path_list[i] == '.':
            continue
        if path_list[i] == '..':
            result.pop(len(result) - 1)
        else:
            result.append(path_list[i])

    for i in result:
        if i != '':
            str_res += '/'
            str_res += i
    return str_res if str_res != '' else '/'


print(reduce_file_path("/srv/../"))
print(reduce_file_path("/srv/../srv/../srv/../"))
print(reduce_file_path("/srv/././././"))
print(reduce_file_path("/srv/www/htcdocs/wtf"))
print(reduce_file_path("///////////////////"))
print(reduce_file_path("/etc//wtf/"))
