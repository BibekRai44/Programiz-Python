def check(num):
    try:
        float(num)
        return True
    except ValueError:
        return False
print(check('ba132'))
print(check('1.334'))