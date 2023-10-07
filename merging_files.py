with open("1.txt",encoding="utf-8") as f:
    all_files = {}
    order=[]
    full_text = f.readlines()
    all_files[f.name]={"lines":len(full_text),"text":f"{f.name}\n{len(full_text)}\n{''.join(full_text)}"}
    print(all_files)
    order.append(f.name)
    print(order)

with open("2.txt",encoding="utf-8") as f:
    full_text = f.readlines()

    all_files[f.name] = {"lines": len(full_text), "text": f"{f.name}\n{len(full_text)}\n{''.join(full_text)}"}
    for file in order:
        if all_files[f.name]["lines"]<all_files[file]["lines"]:
            order.insert(order.index(file),f.name)
            break
        else:
            order.append(f.name)

with open("3.txt",encoding="utf-8") as f:
    full_text = f.readlines()
    all_files[f.name] = {"lines": len(full_text), "text": f"{f.name}\n{len(full_text)}\n{''.join(full_text)}"}
    for file in order:
        if all_files[f.name]["lines"]<all_files[file]["lines"]:
            order.insert(order.index(file),f.name)
            break
    if f.name not in order:
        order.append(f.name)
    print(order)

with open("all_files.txt",'w',encoding="utf-8") as f:
    for file in order:
        f.write(f"{all_files[file]['text']}\n")