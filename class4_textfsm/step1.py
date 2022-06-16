import textfsm


with open("step1.output", "r") as f:
    output = f.read()

print(output)

with open("step1.template") as template:
    parser = textfsm.TextFSM(template)
    data = parser.ParseText(output)

    print(data)
