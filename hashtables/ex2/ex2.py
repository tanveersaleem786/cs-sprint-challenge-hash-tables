#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination

def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    tickets_dict = {}
    for ticket in tickets:
        tickets_dict[ticket.source] = ticket.destination
    route = []
    destination = tickets_dict["NONE"]
    while destination != "NONE":
        route.append(destination)
        destination = tickets_dict[destination]
    route.append(destination)
    return route
