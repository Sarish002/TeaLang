with open("Program.tea", "a+") as Pro:
    Pro.write("\n")
with (open("Program.tea", "r") as Pro):
    g = Pro.read()
    g2 = g.split("\n")
    for line in g2:

        if "Python" in line:
            code = []
            for i in g2[(e + 1): ]:
                if i == "<<<":
                    break
                code.append(i)
            command = "\n".join(code)
            exec(command)

        if "only" in line:
            cond = line[4 : line.index(":")]
            if eval(cond):
                r = line.split(": ")[1]
                if "set " in r:
                    varname = r.split(" ")[1]
                    value = " ".join(r.split(" ")[3:])
                    if "steal" in value:
                        value = input(" ".join(r.split(" ")[3:])[8:-1])
                    try:
                        globals()[varname] = eval(value)
                    except NameError:
                        globals()[varname] = (value)
                    except SyntaxError:
                        globals()[varname] = str(value)
                if "change " in r:
                    varname = r.split(" ")[1]
                    value = " ".join(r.split(" ")[3])
                    try:
                        globals()[varname] = eval(value)
                    except NameError:
                        globals()[varname] = (value)
                    except SyntaxError:
                        globals()[varname] = str(value)
                if "show " in r:
                    print2 = eval(r[4:])
                    print(print2)
                continue
            else:
                line2 = g2[g2.index(line) +  1]
                r = line2.split(": ")[1]
                if "set " in r:
                    varname = r.split(" ")[1]
                    value = " ".join(r.split(" ")[3:])
                    if "steal" in value:
                        value = input(" ".join(r.split(" ")[3:])[8:-1])
                    try:
                        globals()[varname] = eval(value)
                    except NameError:
                        globals()[varname] = (value)
                    except SyntaxError:
                        globals()[varname] = str(value)
                if "change " in r:
                    varname = r.split(" ")[1]
                    value = " ".join(r.split(" ")[3])
                    try:
                        globals()[varname] = eval(value)
                    except NameError:
                        globals()[varname] = (value)
                    except SyntaxError:
                        globals()[varname] = str(value)
                if "show " in r:
                    print2 = eval(r[4:])
                    print(print2)
                continue
        if "set " in line and "otherwise" not in line:
            varname = line.split(" ")[1]
            value = " ".join(line.split(" ")[3:])
            if "steal" in value:
                value = input(" ".join(line.split(" ")[3:])[8:-1])
            try:
                globals()[varname] = eval(value)
            except NameError:
                globals()[varname] = (value)
            except SyntaxError:
                globals()[varname] = str(value)
        if "change " in line and "otherwise" not in line:
            varname = line.split(" ")[1]
            value = " ".join(line.split(" ")[3])
            try:
                globals()[varname] = eval(value)
            except NameError:
                globals()[varname] = (value)
            except SyntaxError:
                globals()[varname] = str(value)
        if "show " in line and "otherwise" not in line:
            print2 = eval(line[4 : ])
            print(print2)

# TeaLang
# Creator: Abhinav. S. Nair
# Date: 5 - 10 - 24
# Functions: Set, Change, Print, Evaluate, If - Else
# Python < TeaLang
