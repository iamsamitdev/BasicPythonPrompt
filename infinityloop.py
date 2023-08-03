import time

# Infinity Loop
r = 1
while True:
    if r > 30:
        break
    if r % 2 == 1:
        print(r, "On")
    else:
        print(r, "Off")
    r = r + 1

    # ทำการ sleep 1 วินาที
    time.sleep(1)
