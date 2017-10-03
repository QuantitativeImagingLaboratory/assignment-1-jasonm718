
def linear_interpolation(pt1, pt2, unknown):
    """Computes the linear interpolation for the unknown values using pt1 and pt2
    take as input
    pt1: known point pt1 and f(pt1) or intensity value
    pt2: known point pt2 and f(pt2) or intensity value
    unknown: take and unknown location
    return the f(unknown) or intentity at unknown"""

    """
        Linear interpolation Formula:     
        I = ((i1(x2 - x))/(x2 - x1)) + ((i2(x - x1))/(x2 - x1))
    """
    # Write your code for linear interpolation here

    I= int(pt1) + unknown*(int(pt2)-int(pt1))
    return I

def bilinear_interpolation(pt1, pt2, pt3, pt4, unknown):
    """Computes the linear interpolation for the unknown values using pt1 and pt2
    take as input
    pt1: known point pt1 and f(pt1) or intensity value
    pt2: known point pt2 and f(pt2) or intensity value
    pt1: known point pt3 and f(pt3) or intensity value
    pt2: known point pt4 and f(pt4) or intensity value
    unknown: take and unknown location
    return the f(unknown) or intentity at unknown"""

    # Write your code for bilinear interpolation here
    # May be you can reuse or call linear interpolatio method to compute this task

    i1 = linear_interpolation(pt1,pt2,unknown[0])
    i2 = linear_interpolation(pt3,pt4, unknown[0])

    result = linear_interpolation(i1,i2,unknown[1])

    return result
