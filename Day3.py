altitude=int(input("What's the height of the plane?"))
if altitude <= 1000:
    print("Safe to land")
elif altitude>1000 and altitude<=5000:
    print("Bring down to 1000ft")
else:
    print("Go around and try later")
