def rectangle_area_perimeter(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter
length = float(input())
width = float(input())
area, perimeter = rectangle_area_perimeter(length, width)
print(f"Area: {area}, Perimeter: {perimeter}")
