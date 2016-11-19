class Date:
    def __init__(self, day, month, year, hour):
        self.day = day
        self.month = month
        self.year = year
        self.hour = hour

    def __eq__(self, other):
        return (self.day == other.day and self.month == other.month and
                self.year == other.year) # and self.hour == other.hour)

    def __lt__(self, other):
        if self.year < other.year:
            return True
        elif self.year == other.year:
            if self.month < other.month:
                return True
            elif self.month == other.month:
                if self.day < other.day:
                    return True
                elif self.day == other.day:
                    if self.hour <= other.hour:
                        return True
        return False


class Terminal:
    def __init__(self, number, max_flight):
        self.number = number
        self.max_flight = max_flight

    def __eq__(self, other):
        return (self.number == other.number and
                self.max_flight == other.max_flight)


class Flight:
    def __init__(self, start_time, end_time, passengers, max_passengers,
                 from_dest, to_dest, terminal, declined):
        self.start_time = start_time
        self.end_time = end_time
        self.passengers = passengers
        self.max_passengers = max_passengers
        self.from_dest = from_dest
        self.to_dest = to_dest
        self.terminal = terminal
        self.declined = declined
        self.passengers_list[]

    def set_passengers(self, person):
        self.passengers_list.append(person)

    def flight_empty_seats(self):
        return self.passengers < self.max_passengers

    def flight_duration(self):
        hours = int(self.end_time.hour.split(':')[0]) - \
                int(self.start_time.hour.split(':')[0])
        minutes = int(self.end_time.hour.split(':')[1]) - \
            int(self.start_time.hour.split(':')[1])
        if minutes < 0:
            minutes += 60
            hours -= 1
        if hours < 0:
            hours += 24
        if hours < 10:
            hours = '0' + str(hours)
        if minutes < 10:
            minutes = '0' + str(minutes)
        return "{}:{}".format(hours, minutes)

    def __eq__(self, other):
        return (self.start_time == other.start_time and self.end_time == other.end_time and
                self.passengers == other.passengers and self.max_passengers == other.max_passengers and
                self.from_dest == other.from_dest and self.to_dest == other.to_dest and
                self.terminal == other.terminal and self.declined == other.declined)


class Passenger:
    def __init__(self, first_name, last_name, flight, age):
        self.first_name = first_name
        self.last_name = last_name
        self.flight = flight
        self.age = age

    def __eq__(self, other):
        return (self.first_name == other.first_name and
                self.last_name == other.last_name and
                self.flight == other.flight and self.age == other.age)


class Reservation:
    def __init__(self, flight, passenger, accepted):
        self.flight = flight
        self.passenger = passenger
        self.accepted = accepted


class AllFlight:
    def __init__(self, flight):
        self.flights = []
        self.flights.append(flight)

    def set_flight(self, flight):
        self.flight.append(flight)

    def get_flights_for(self, date):
        result = 0
        for flight in self.flights:
            if flight.start_time.day == date.day and\
             flight.start_time.month == date.month and\
             flight.start_time.year == date.year:
                result += 1
        return result

    def get_flights_before(self, date, hour):
        result = 0
        for flight in self.flights:
            if flight.start_time.hour < hour:
                result += 1
        return result

    def get_flights_to_destination(self, destination):
        for flight in self.flights:
            if flight.to_dest == destination:
                return True
        return False

    def get_flight_to(self, destination, date):
        result = []
        for flight in self.flights:
            if flight.to_dest == destination:
                if flight.start_time == date:
                    result.append(flight)
        return result

    def get_flight_from(self, destination, date):
        result = []
        for flight in self.flights:
            if flight.from_dest == destination:
                if flight.start_time == date:
                    result.append(flight)
        return result

    def get_terminal_flights(self, terminal):
        result = []
        for flight in self.flights:
            if flight.terminal.number == terminal.number:
                result.append(flight)
        return result

    def get_terminal_flights_on(self, terminal, date):
        result = []
        for flight in self.flights:
            if flight.terminal.number == terminal.number:
                if flight.start_time == date:
                    result.append(flight)
        return result

    def terminal_flights_to_dest(self, terminal, destination):
        result = []
        for flight in self.flights:
            if flight.terminal.number == terminal.number:
                if flight.to_dest == destination:
                    result.append(flight)
        return result

    def flights_within_duration(self, start_date, end_date):
        result = []
        for flight in self.flights:
            if flight.start_time < end_date and start_date < flight.end_time:
                result.append(flight)
        return result
