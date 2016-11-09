import json
import sys


def print_result(result_dict):
    for i in result_dict:
        print(i + ": " + result_dict[i][1] + " " + result_dict[i][2])


def walk(data):
    result_dict = {}
    fn = ''
    ln = ''
    for i in data["people"]:
        for k in i:  # first_name|last_name|skills
            fn = i["first_name"]
            ln = i["last_name"]
            if k == "skills":
                for skill in i[k]:  # skills
                    if skill["name"] in result_dict:
                        if skill["level"] > result_dict[skill["name"]][0]:
                            result_dict[skill["name"]] = [skill["level"], fn, ln]
                    else:
                        result_dict[skill["name"]] = [skill["level"], fn, ln]
    print_result(result_dict)


def read_json():
    with open(sys.argv[1], 'r') as f:
        data = json.load(f)

    return walk(data)


def main():
    (read_json())

if __name__ == '__main__':
    main()
