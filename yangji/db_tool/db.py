
GROUP_NAME_PREFIX = 'PLC_'


LOAD_UNLOAD_SLOTS = [1, 2, 3, 91, 92, 93]
AUTO_RESET_VARS = ['Operation', 'MaterialType', 'PoleType', 'MaterialQuantity']
ACTIVE_TIMESTAMP = {GROUP_NAME_PREFIX + 'Slot_%d_%s' % (s, v): 0 for v in AUTO_RESET_VARS for s in LOAD_UNLOAD_SLOTS}

print(ACTIVE_TIMESTAMP)




d1 = [1,2]
d2 = ['kiko','herman']
d3 = {name + str(age) : age for name in d2 for age in d1}

print(d3)


