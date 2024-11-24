def main():
    N = int(input())

    placeCards = set()
    for _ in range(N):
        a, b, c, plane = input().split()
        x, y, z = int(a), int(b), int(c)
        placeCards.add((x, y, z, plane))

    # Determine the bounds of the box
    x_min, x_max = float("inf"), float("-inf")
    y_min, y_max = float("inf"), float("-inf")
    z_min, z_max = float("inf"), float("-inf")

    for x, y, z, plane in placeCards:
        x_min, x_max = min(x_min, x), max(x_max, x)
        y_min, y_max = min(y_min, y), max(y_max, y)
        z_min, z_max = min(z_min, z), max(z_max, z)

    # Generate all required cards for a closed box
    requiredCards = set()

    # Add top and bottom faces (parallel to xy plane)
    for x in range(x_min, x_max + 1):
        for y in range(y_min, y_max + 1):
            requiredCards.add((x, y, z_min, "xy"))
            requiredCards.add((x, y, z_max, "xy"))

    # Add front and back faces (parallel to xz plane)
    for x in range(x_min, x_max + 1):
        for z in range(z_min, z_max + 1):
            requiredCards.add((x, y_min, z, "xz"))
            requiredCards.add((x, y_max, z, "xz"))

    # Add left and right faces (parallel to yz plane)
    for y in range(y_min, y_max + 1):
        for z in range(z_min, z_max + 1):
            requiredCards.add((x_min, y, z, "yz"))
            requiredCards.add((x_max, y, z, "yz"))

    # Find the missing cards
    missingCards = requiredCards - placeCards

    # If no cards are missing, calculate the volume
    if not missingCards:
        volume = (x_max - x_min) * (y_max - y_min) * (z_max - z_min)
        print(volume)
    else:
        # Print any one missing card
        missingCard = missingCards.pop()
        print(f"{missingCard[0]} {missingCard[1]} {missingCard[2]} {missingCard[3]}")

if __name__ == "__main__":
    main()
