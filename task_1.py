str = '1h 45m,360s,25m,30m 120s,2h 60s'
total_minutes = 0

new_str = str.split(',')

for semi_str in new_str:
    each_part = semi_str.split()
    for one_part in each_part:
        if 'h' in one_part:
            total_minutes+=int(one_part.replace('h', ''))*60
        elif 'm' in one_part:
            total_minutes += int(one_part.replace('m', ''))
        elif 's' in one_part:
            total_minutes += int(one_part.replace('s', ''))/60


print(total_minutes)