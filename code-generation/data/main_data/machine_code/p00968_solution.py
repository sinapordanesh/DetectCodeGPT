def digit_order(n, names):
    res = []
    ref_name = names[0]
    ref_name_items = []
    for i in range(len(ref_name)):
        if ref_name[i].isalpha():
            ref_name_items.append((ref_name[i], 'letter'))
        else:
            num = ""
            j = i
            while j < len(ref_name) and ref_name[j].isdigit():
                num += ref_name[j]
                j += 1
            ref_name_items.append((int(num), 'number'))
            i = j - 1
    
    for name in names[1:]:
        name_items = []
        for i in range(len(name)):
            if name[i].isalpha():
                name_items.append((name[i], 'letter'))
            else:
                num = ""
                j = i
                while j < len(name) and name[j].isdigit():
                    num += name[j]
                    j += 1
                name_items.append((int(num), 'number'))
                i = j - 1
        
        idx = 0
        while idx < len(ref_name_items) and idx < len(name_items):
            if ref_name_items[idx][1] == 'number' and name_items[idx][1] == 'letter':
                res.append('-')
                break
            elif ref_name_items[idx][1] == 'letter' and name_items[idx][1] == 'number':
                res.append('+')
                break
            elif ref_name_items[idx][1] == 'number' and name_items[idx][1] == 'number':
                if ref_name_items[idx][0] < name_items[idx][0]:
                    res.append('-')
                    break
                elif ref_name_items[idx][0] > name_items[idx][0]:
                    res.append('+')
                    break
            elif ref_name_items[idx][1] == 'letter' and name_items[idx][1] == 'letter':
                if ord(ref_name_items[idx][0]) < ord(name_items[idx][0]):
                    res.append('-')
                    break
                elif ord(ref_name_items[idx][0]) > ord(name_items[idx][0]):
                    res.append('+')
                    break
            idx += 1
        
        if idx == len(ref_name_items) and idx < len(name_items):
            res.append('-')
        elif idx < len(ref_name_items) and idx == len(name_items):
            res.append('+')
    
    return res