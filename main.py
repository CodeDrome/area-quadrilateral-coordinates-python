import quadrilateralareascoordinates


def main():

    print("-----------------------------------")
    print("| codedrome.com                   |")
    print("| Calculating Areas of            |")
    print("| Quadrilaterals from Coordinates |")
    print("-----------------------------------\n")

    quadrilateral_1 = {"coordinates": [[6,19],[3,2],[17,5],[19,15]], "area": 0}
    quadrilateral_1["area"] = quadrilateralareascoordinates.calculate_area(quadrilateral_1["coordinates"])
    print(quadrilateral_1)

    print()

    quadrilateral_2 = {"coordinates": [[-4,9],[-7,-8],[7,-5],[9,5]], "area": 0}
    quadrilateral_2["area"] = quadrilateralareascoordinates.calculate_area(quadrilateral_2["coordinates"])
    print(quadrilateral_2)


main()
