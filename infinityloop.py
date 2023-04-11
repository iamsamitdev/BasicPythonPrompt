import time

# Infinity Loop
r = 1
while True:
    # loop 30 รอบ
    if r <= 30:
        if r % 2 == 1:
            print(r, "On")
        else:
            print(r, "Off")
    else:
        break
    r = r + 1

    # ทำการ sleep 1 วินาที
    time.sleep(1)
