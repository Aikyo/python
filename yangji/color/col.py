
def get_crane():
    di = {}
    di['locked'] = False
    di['feifei'] = False
    di['xiaoma'] = color(di)
    return di
def color(di):
    if di.get('feifei'):
        return 'kkkkk'
    else:
        return 'meiyoufeifei'
d = get_crane()

print(d)




