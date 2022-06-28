Investment = 40000
Rent = 700
Loss = 1000

def ROI(Investment, Rent, Loss):
    netprofile = Rent * 12 - Loss
    ROI = (netprofile/Investment) * 100
    print(ROI)

ROI(Investment, Rent, Loss)