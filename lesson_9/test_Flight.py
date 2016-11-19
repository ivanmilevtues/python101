import unittest
from Flight import *


class TestDate(unittest.TestCase):
    def setUp(self):
        self.date1 = Date(1, 2, 3, "12:32")

    def test_date_constructor(self):
        self.assertEqual(self.date1.day, 1)
        self.assertEqual(self.date1.month, 2)
        self.assertEqual(self.date1.year, 3)
        self.assertEqual(self.date1.hour, "12:32")

    def test_lt(self):
        self.assertTrue(self.date1 < Date(1, 1, 4, '12:32'))
        self.assertTrue(self.date1 < Date(1, 3, 3, '11:11'))
        self.assertTrue(self.date1 < Date(2, 2, 3, '11:11'))
        self.assertTrue(self.date1 < Date(1, 2, 3, '12:33'))

    def test_eq(self):
        self.assertTrue(self.date1 == Date(1, 2, 3, '12:32'))
        self.assertFalse(self.date1 == Date(1, 2, 2, '10:10'))


class TestTerminal(unittest.TestCase):
    def setUp(self):
        self.term1 = Terminal(number=1, max_flight=20)

    def test_termianl_Constructor(self):
        self.assertEqual(self.term1.number, 1)
        self.assertEqual(self.term1.max_flight, 20)

    def test_eq(self):
        self.assertTrue(self.term1 == Terminal(1, 20))
        self.assertFalse(self.term1 == Terminal(2, 20))


class TestFlight(unittest.TestCase):
    def setUp(self):
        self.fl1 = Flight(start_time=Date(29, 11, 2016, hour='12:20'),
                          end_time=Date(29, 11, 2016, hour='15:30'),
                          passengers=100,
                          max_passengers=120, from_dest="Sofia",
                          to_dest="London", terminal=Terminal(2, 30),
                          declined=False)
        self.fl2 = Flight(start_time=Date(29, 11, 2016, hour='12:20'),
                          end_time=Date(29, 11, 2016, hour='15:30'),
                          passengers=120,
                          max_passengers=120, from_dest="Sofia",
                          to_dest="London", terminal=Terminal(2, 30),
                          declined=False)

    def test_flight_empty_seats(self):
        self.assertTrue(self.fl1.flight_empty_seats())
        self.assertFalse(self.fl2.flight_empty_seats())

    def test_eq(self):
        self.assertTrue(self.fl1 == Flight(start_time=Date(29, 11, 2016, hour='12:20'),
                                           end_time=Date(29, 11, 2016, hour='15:30'),
                                           passengers=100,
                                           max_passengers=120, from_dest="Sofia",
                                           to_dest="London", terminal=Terminal(2, 30),
                                           declined=False))
        self.assertFalse(self.fl1 == Flight(start_time=Date(29, 11, 2016, hour='12:20'),
                                           end_time=Date(29, 11, 2016, hour='15:30'),
                                           passengers=100,
                                           max_passengers=1000, from_dest="Sofia",
                                           to_dest="London", terminal=Terminal(2, 30),
                                           declined=False))

    def test_flight_constructor(self):
        self.assertEqual(self.fl1.start_time, Date(29, 11, 2016, hour='12:20'))
        self.assertEqual(self.fl1.end_time, Date(29, 11, 2016, hour='15:30'))
        self.assertEqual(self.fl1.passengers, 100)
        self.assertEqual(self.fl1.max_passengers, 120)
        self.assertEqual(self.fl1.from_dest, "Sofia")
        self.assertEqual(self.fl1.to_dest, "London")
        self.assertEqual(self.fl1.terminal, Terminal(2, 30))
        self.assertFalse(self.fl1.declined)

    def test_flight_duration(self):
        self.assertEqual(self.fl1.flight_duration(), "03:10")


class TestPassenger(unittest.TestCase):
    def setUp(self):
        self.pssngr = Passenger(first_name="Rositsa", last_name="Zlateva",
                                flight=Flight(start_time=Date(29, 11, 2016, hour='12:20'),
                                              end_time=Date(29, 11, 2016, hour='15:30'),
                                              passengers=100,
                                              max_passengers=120, from_dest="Sofia",
                                              to_dest="London", terminal=Terminal(2, 30),
                                              declined=False), age=22)

    def test_passenger_constructor(self):
        self.assertEqual(self.pssngr.first_name, "Rositsa")
        self.assertEqual(self.pssngr.last_name, "Zlateva")
        self.assertEqual(self.pssngr.flight, Flight(start_time=Date(29, 11, 2016, hour='12:20'),
                                                    end_time=Date(29, 11, 2016, hour='15:30'),
                                                    passengers=100,
                                                    max_passengers=120, from_dest="Sofia",
                                                    to_dest="London", terminal=Terminal(2, 30),
                                                    declined=False))
        self.assertEqual(self.pssngr.age, 22)

    def test_eq(self):
        self.assertTrue(self.pssngr, Passenger(first_name="Rositsa", last_name="Zlateva",
                                               flight=Flight(start_time=Date(29, 11, 2016, hour='12:20'),
                                               end_time=Date(29, 11, 2016, hour='15:30'),
                                               passengers=100,
                                               max_passengers=120, from_dest="Sofia",
                                               to_dest="London", terminal=Terminal(2, 30),
                                               declined=False), age=22))


class TestReservation(unittest.TestCase):
    def setUp(self):
        self.f1 = Flight(start_time=Date(29, 11, 2016, hour='12:20'),
                         end_time=Date(29, 11, 2016, hour='15:30'),
                         passengers=100,
                         max_passengers=120, from_dest="Sofia",
                         to_dest="London", terminal=Terminal(2, 30),
                         declined=False)
        self.res1 = Reservation(flight=self.f1, passenger=Passenger("Rositsa", "Zlateva",
                                                                     self.f1, 22),
                                accepted=True)

    def test_reservation_constructor(self):
        self.assertEqual(self.res1.flight, self.f1)
        self.assertEqual(self.res1.passenger, Passenger("Rositsa", "Zlateva", self.f1, 22))
        self.assertTrue(self.res1.accepted)


class TestAllFlight(unittest.TestCase):
    def setUp(self):
        self.f1 = Flight(start_time=Date(29, 11, 2016, hour='12:20'),
                         end_time=Date(29, 11, 2016, hour='15:30'),
                         passengers=100,
                         max_passengers=120, from_dest="Sofia",
                         to_dest="London", terminal=Terminal(2, 30),
                         declined=False)
        self.all_fl = AllFlight(flight=self.f1)
        self.p1 = Passenger("Z", "A", self.f1 ,18)

    def test_allflights_constructor(self):
        self.assertEqual(self.all_fl.flights[0], Flight(start_time=Date(29, 11, 2016, hour='12:20'),
                                                        end_time=Date(29, 11, 2016, hour='15:30'),
                                                        passengers=100,
                                                        max_passengers=120, from_dest="Sofia",
                                                        to_dest="London", terminal=Terminal(2, 30),
                                                        declined=False))

    def test_get_flights_for(self):
        self.assertEqual(self.all_fl.get_flights_for(Date(29, 11, 2016, hour='12:20')), 1)

    def test_get_flights_before(self):
        self.assertEqual(self.all_fl.get_flights_before(Date(29, 11, 2016, hour="12:20"), '13:00'), 1)

    def test_get_flights_to_destination(self):
        self.assertTrue(self.all_fl.get_flights_to_destination("London"))
        self.assertFalse(self.all_fl.get_flights_to_destination("kk"))

    def test_get_flight_to(self):
        self.assertEqual(self.all_fl.get_flight_to("London", Date(29, 11, 2016, '12:20')),
                         [Flight(start_time=Date(29, 11, 2016, hour='12:20'),
                                 end_time=Date(29, 11, 2016, hour='15:30'),
                                 passengers=100,
                                 max_passengers=120, from_dest="Sofia",
                                 to_dest="London", terminal=Terminal(2, 30),
                                 declined=False)])
        self.assertEqual(self.all_fl.get_flight_to("London", Date(29, 12, 2016, '12:20')),[])

    def test_get_flight_from(self):
        self.assertEqual(self.all_fl.get_flight_from("Sofia", Date(29, 11, 2016, '12:20')),
                         [Flight(start_time=Date(29, 11, 2016, hour='12:20'),
                                 end_time=Date(29, 11, 2016, hour='15:30'),
                                 passengers=100,
                                 max_passengers=120, from_dest="Sofia",
                                 to_dest="London", terminal=Terminal(2, 30),
                                 declined=False)])
        self.assertEqual(self.all_fl.get_flight_from("London", Date(29, 12, 2016, '12:20')),[])

    def test_get_terminal_flights(self):
        self.f1 = Flight(start_time=Date(29, 11, 2016, hour='12:20'),
                         end_time=Date(29, 11, 2016, hour='15:30'),
                         passengers=100,
                         max_passengers=120, from_dest="Sofia",
                         to_dest="London", terminal=Terminal(2, 30),
                         declined=False)
        self.assertEqual(self.all_fl.get_terminal_flights(Terminal(1, 20)), [])
        self.assertEqual(self.all_fl.get_terminal_flights(Terminal(2, 20)), [self.f1])

    def test_get_terminal_flights_on(self):
        self.assertEqual(self.all_fl.get_terminal_flights_on(Terminal(2, 20),Date(29, 11, 2016, hour='12:20')), [self.f1])
        self.assertEqual(self.all_fl.get_terminal_flights_on(Terminal(3, 20),Date(29, 11, 2016, hour='12:20')), [])

    def test_terminal_flights_to_dest(self):
        self.assertEqual(self.all_fl.terminal_flights_to_dest(Terminal(2, 20), "London"), [self.f1])
        self.assertEqual(self.all_fl.terminal_flights_to_dest(Terminal(2, 20), "Sofia"), [])

    def test_flights_within_duration(self):
        self.assertEqual(self.all_fl.flights_within_duration(Date(1, 1, 2015, hour='12:20'), Date(29, 12, 2016, hour='12:20')), [self.f1])

    # def test_take_passengers_under_18(self):
    #     self.assertEqual(self.all_f1.take_passengers_under_18(self.f1), 1)

if __name__ == "__main__":
    unittest.main()
