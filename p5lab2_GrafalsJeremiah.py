def feet_to_steps(feet):
    steps = int(feet/2.5)
    return steps

if __name__ == '__main__':
    feet = float(input())
    steps = feet_to_steps(feet)
    print(steps)
    