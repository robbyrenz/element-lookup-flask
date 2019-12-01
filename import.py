# imports the whole information of elements, contained in a json file, to a PostgreSQL database on Heroku

import json

def main():
    # open and read the json file
    with open("data/periodic_table.json", 'r') as data:
        json_file = json.load(data)

    # print info about Hydrogen
    # print(json_file.get("elements")[0])

    # print all of the keys for Hydrogen
    # keys_of_hydrogen = json_file.get("elements")[0]
    # print("The keys of Hydrogen:")
    # for key in keys_of_hydrogen.keys():
    #     print(key)
    # print()

    # now print and count all of the keys of all the elements
    all_elements = json_file.get("elements")  # all_elements now holds a list of dicts
    total_number_of_elements= 0
    for element in all_elements:
        # print(f"Element name: {element.get("name")}") -> why is this not working!?!?
        key_count = 0  # hold the number of keys for each element
        element_name = element.get("name")
        print(f"Name of element: {element_name}:")
        print(f"The keys of {element_name}:")

        for key in element.keys():
            key_count += 1  # increment the key count for this particular element by 1
            # if key == "name":
            #     continue  # skip printing out the name of the element
            print(f"\t{key}")  # print the name of the key

        print(f"Total number of keys for {element_name}: {key_count}")  # at the end of each element, print out the total number of keys
        print()
        total_number_of_elements += 1  # increment the total number of elements it processed
        
    print(f"The total number of elements processed: {total_number_of_elements}")  # finally print out the total number of elements


if __name__ == "__main__":
    main()
