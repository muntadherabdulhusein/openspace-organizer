  def assign_colleagues(self, colleagues):
        # Shuffle the list of colleagues randomly
        random.shuffle(colleagues)

Flatten the list of seats from all tables
        seats = [seat for table in self.tables for seat in table.occupants]

Assign each colleague to a seat
        for i, colleague in enumerate(colleagues):
            seats[i].set_occupant(colleague)

def print_status(self):
        for idx, table in enumerate(self.tables):
            print(f"Table {idx + 1}:")
            for seat_idx, seat in enumerate(table.occupants):
                status = "Free" if seat.free else f"Occupied by {seat.occupant}"
                print(f"  Seat {seat_idx + 1}: {status}")


open_space.print_status()