def main_test():
    import math as m

    LatitudeOne = 40.431968
    LongitudeOne = -86.922644
    # Longitude and Latitude inputs and angle of elevation
    LatitudeTwo = 40.432703
    LongitudeTwo = -86.92344
    Angle = 4.93

    LatitudeDifference = abs(LatitudeTwo-LatitudeOne)
    LongitudeDiffernce = abs(LongitudeTwo-LongitudeOne)
    # Converts longitude to miles
    LongitudeConversion = 69.172 * \
        m.cos(m.radians((LatitudeTwo*.5+LatitudeOne*.5)))

    # Latitude*69 converts latitude to miles    #Calculates the slope distance
    SlopeDistanceMiles = m.sqrt(
        (LatitudeDifference*69)**2+(LongitudeDiffernce*LongitudeConversion)**2)
    # Converts slope distance from miles to feet
    SlopeDistanceFeet = SlopeDistanceMiles*5280
    ElevationChangeFeet = SlopeDistanceFeet * \
        m.tan(m.radians(Angle))  # Calculates elevation change in feet

    print(f"The slope distance is {SlopeDistanceFeet:.1f} feet.")
    # Prints outputs
    print(f"The change in elevation is {ElevationChangeFeet:.1f} feet.")


if __name__ == '__main__':
    main_test()
print("")
