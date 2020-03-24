import json
import csv

courses = {1: 'Linux', 2: 'Git', 3: 'Vim'}

json_str = json.dumps(courses)

# print(json_str)

# with open('courses.py', 'w') as f:
#     f.write(json_str)
#
# with open('courses.json', 'w') as f1:
#     f1.write(json_str)

# with open('courses.json', 'w') as f2:
#     json.dump(courses, f2)

# print(json.loads(json_str))

# with open('courses.json') as f3:
#     print(json.load(f3))

with open('test.csv') as f4:
    data = list(csv.reader(f4))
    for i in data:
        print(i)
    ## 加newline解决空行的问题
    with open('test_w.csv', 'w', newline='') as f5:
        csv.writer(f5).writerows(data)


