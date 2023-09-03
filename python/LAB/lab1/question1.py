'''
Test code
air tempereature: 50 
wind speed: 5
result(wind chill index): 55
'''
air_temperature = float(input('Kindly enter the air temperature(celcius):'))
wind_speed = float(input('Kindly enter the wind speed(km/h): '))
wci = 13.12 + (0.6215*air_temperature) - (11.37*(wind_speed**0.16)) + (0.3965*(air_temperature*(wind_speed**0.16)))
print(f'The wind chill index is {round(wci)}') # using formatted strings

