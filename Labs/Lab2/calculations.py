from transport import Bus, Train, Airplane

def create_transport(mode, distance, speed, ticket_price):
    if mode == 'bus':
        return Bus(distance, speed, ticket_price)
    elif mode == 'train':
        return Train(distance, speed, ticket_price)
    elif mode == 'airplane':
        return Airplane(distance, speed, ticket_price)
    else:
        raise ValueError("Invalid transport mode")

def get_trip_info(transport, passengers):
    time = transport.calculate_time()
    cost = transport.calculate_cost(passengers)
    return time, cost