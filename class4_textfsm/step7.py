import textfsm


with open("step1.output", "r") as f:
    output = f.read()

print(output)

with open("step2.template") as template:
    parser = textfsm.TextFSM(template)
    data = parser.ParseTextToDicts(output)

    for data_dict in data:
        print(data_dict)
