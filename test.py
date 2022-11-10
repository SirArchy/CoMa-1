def time_range_scheduler_check(time_ranges, time_value):
    for i in time_ranges:
        # convert time range & time value to decimal numbers
        (time_ranges_min, time_ranges_max) = time_ranges[i].split('-')
        (h, m, s) = time_ranges_min.split(':')
        time_ranges_min = int(h) * 3600 + int(m) * 60 + int(s)
        (h, m, s) = time_ranges_max.split(':')
        time_ranges_max = int(h) * 3600 + int(m) * 60 + int(s)
        (h, m, s) = time_value.split(':')
        time_value = int(h) * 3600 + int(m) * 60 + int(s)

        # check if time value is in time range
        if time_value >= time_ranges_min & time_value <= time_ranges_max:
            return True
        else:
            continue
    return False



test_time_ranges = ["02:00:00-03:00:00","16:00:00-17:50:59"]
test2_time_ranges = ["05:00:00-06:00:00"]
test_time_value = "02:45:32"
print(time_range_scheduler_check(test_time_ranges,test_time_value))
