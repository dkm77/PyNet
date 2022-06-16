import textfsm


with open("step6.output", "r") as f:
    output = f.read()

print(output)

with open("step6.template") as template:
    parser = textfsm.TextFSM(template)
    data = parser.ParseTextToDicts(output)

    for data_dict in data:
        print(data_dict)
