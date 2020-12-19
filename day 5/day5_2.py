boardin_passes = [line.strip() for line in open("day5_input.txt")]

seat_ids = []
for i, _ in enumerate(boardin_passes):
    row = int(boardin_passes[i][:7].replace("F", "0").replace("B", "1"), 2)
    col = int(boardin_passes[i][7:].replace("R", "1").replace("L", "0"), 2)
    seat_ids.append(row * 8 + col)

seat_ids = sorted(seat_ids)
for i, seat in enumerate(seat_ids):
    if seat_ids[i+1] != seat + 1:
        print(seat + 1)
        break
