#dealing with leap years gave me cancer
def is_leap_year(d:int, m:int, y:int)->bool:
    if y % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True
def end_28th(d:int, m:int, y:int)->bool:
    return (d == 28 and m == 2) and not is_leap_year(d,m,y)
def end_29th(d:int, m:int, y:int)->bool:
    return (d == 29 and m == 2)
def end_30th(d:int, m:int, y:int)->bool:
    return (d == 30 and m == (9 or 4 or  6 or 11))
def end_31th(d:int, m:int, y:int)->bool:
    return (d == 31)
def is_end_of_month(d: int, m: int, y: int)->bool:
    return (end_29th(d,m,y) or end_30th(d,m,y) or end_31th(d,m,y) or end_28th(d,m,y))

day, month, year, name, endd, endm, endy = 1, 1, 1900, 0, 31, 12, 2000
s = 0
while (day, month, year) != (endd, endm, endy):
    if name == 6 and day == 1:
        s += 1
    name = (name+1)%7
    if is_end_of_month(day, month, year):
        day = 1
        month = 1 if month == 12 else month+1
        year = year + 1 if month == 1 else year

    else:
        day += 1
    
print(s)