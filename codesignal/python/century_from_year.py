def centuryFromYear(year):
    # print(type(year))
    if(len(str(year))>3):
        return (int(str(year)[:2])+1) if int(str(year)[2:])>0 else int(str(year)[:2])
    if(len(str(year))>2):
        return (int(str(year)[:1])+1) if int(str(year)[1:])>0 else int(str(year)[:1])
    else: return 1
