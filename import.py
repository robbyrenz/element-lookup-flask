# imports the whole information of elements, contained in a json file, to a PostgreSQL database on Heroku

import json

def main():
    # open and read the json file
    with open("data/periodic_table.json", 'r') as data:
        json_file = json.load(data)

    # print info about Hydrogen
    print(json_file.get("elements")[0])

    # print all of the keys for Hydrogen
    keys_of_hydrogen = json_file.get("elements")[0]
    for key in keys_of_hydrogen.keys():
        print(key)


if __name__ == "__main__":
    main()
