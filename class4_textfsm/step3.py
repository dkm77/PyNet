import textfsm


with open("step3.output", "r") as f:
    output = f.read()

print(output)

with open("step3.template") as template:
    parser = textfsm.TextFSM(template)
    data = parser.ParseTextToDicts(output)

    for data_dict in data:
        print(data_dict)
