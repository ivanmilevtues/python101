def gas_stations(distance, tank_size, stations):
    result_list = []
    stations.append(distance)
    last_station = 0
    for i in range(len(stations)):
        if last_station + tank_size < stations[i]:
            result_list.append(stations[i - 1])
            last_station = stations[i - 1]
    return result_list


def main():
    print(gas_stations(320, 90, [50, 80, 140, 180, 220, 290]))
    print(gas_stations(390, 80, [70, 90, 140, 210, 240, 280, 350]))

if __name__ == '__main__':
    main()
