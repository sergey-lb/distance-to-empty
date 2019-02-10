from lib import calculate_distance_to_empty

consumption_per_100_km = float(input('Введите расход топлива на 100 км ') )
fuel_level = float(input('Введите объем имеющегося топлива ') )

distance_to_empty = calculate_distance_to_empty(consumption_per_100_km, fuel_level)

print('Топлива хватит примерно на ' + str(distance_to_empty) + ' км')
