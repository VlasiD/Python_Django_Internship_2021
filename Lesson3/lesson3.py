import csv
import json

# function definition
f1 = lambda x: x / (x + 100)
f2 = lambda x: 1 / x
f3 = lambda x: 20 * (f1(x) + f2(x)) / x


# generator definition
def range_generator():
    for i in range(5, 91):
        yield i


generator = range_generator()

# creates a dictionary with the results of calculations in the range from the generator
data = {x: [f1(x), f2(x), f3(x)] for x in generator}
print(data)

# writes results to csv file
with open('result.csv', 'w', newline='') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow((["x", "f1(x)", "f2(x)", "f3(x)"]))
    for pair in data.items():
        row = [pair[0]] + pair[1]
        csv_writer.writerow(row)

# reads the csv file and presents the result as a list
with open('result.csv', 'r') as file:
    csv_reader = csv.reader(file)
    data_list = [row for row in csv_reader][1:]
    print(data_list)

# converts the list to json file
with open('data.json', 'w') as file:
    json.dump(data_list, file, indent=4)