def get_tips(bills_n_tips):
    return [bill * tip for bill, tip in bills_n_tips]

def add_bill_update_tips(new_bill, bills_n_tips, tip_rate=0.18):
    bills_n_tips.append((new_bill, tip_rate))
    tip_out = sum(get_tips(bills_n_tips))
    return tip_out



def test_tip_out():
    waiter_bills_n_tips = []
    print(add_bill_update_tips(58.90, waiter_bills_n_tips, 0.15))
    print(add_bill_update_tips(31.58, waiter_bills_n_tips))
    print(add_bill_update_tips(81.44, waiter_bills_n_tips, 0.20))
    print(get_tips(waiter_bills_n_tips))
    print(len(waiter_bills_n_tips))

print (test_tip_out())

class TipOutTracker():

    def __init__(self, new_bill, tip_rate=0.18):
        self.new_bill = new_bill
        self.tip_rate = tip_rate
        self.bills_n_tips = [(new_bill, tip_rate)]
        self.tip_out = 0

    def get_tips(self, bills_n_tips):
        return [bill * tip for bill, tip in self.bills_n_tips]

    def add_bill(self, new_bill, tip_rate=0.18):
        self.bills_n_tips.append((new_bill, tip_rate))
        self.tip_out = sum(self.get_tips(self.bills_n_tips))
        return self.tip_out

    def __len__(self):
        return len(self.bills_n_tips)



tot = TipOutTracker(58.90)
tot.add_bill(31.58, 0.18)
tot.add_bill(81.44, 0.20)
tot.add_bill(95, 0.25)
tot.add_bill(50, 0.12)
# print(tot.total_tip_out())
print(len(tot))
