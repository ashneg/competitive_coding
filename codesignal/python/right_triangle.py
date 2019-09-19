def rightTriangle(sides):
    return ((sorted(sides)[0])**2+(sorted(sides)[1]**2) == (sorted(sides)[-1])**2)
