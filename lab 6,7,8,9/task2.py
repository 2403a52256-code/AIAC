class sru_student:
    def __init__(self, name, roll_no, hostel_status, fee_paid=False):
        self.name = name
        self.roll_no = roll_no
        self.hostel_status = hostel_status
        self.fee_paid = fee_paid
    def fee_update(self, status):
        self.fee_paid = status
    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Roll No.: {self.roll_no}")
        print(f"Hostel Status: {self.hostel_status}")
        print(f"Fee Paid: {'Yes' if self.fee_paid else 'No'}")
if __name__ == "__main__":
    student1 = sru_student("Anu", 101, "Hosteller")
    student1.display_details()
    student1.fee_update(True)
    print("\nAfter fee update:")
    student1.display_details()