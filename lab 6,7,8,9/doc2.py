class sru_student:
    """
    A class to represent an SRU student.

    Attributes:
        name (str): Name of the student.
        roll_no (str): Roll number of the student.
        hostel_status (bool): True if staying in hostel, False otherwise.
        fee_paid (bool): True if fee is paid, False otherwise.
    """

    def __init__(self, name, roll_no, hostel_status):
        """
        Initialize the sru_student object.

        Args:
            name (str): Student's name.
            roll_no (str): Student's roll number.
            hostel_status (bool): Hostel status.
        """
        self.name = name
        self.roll_no = roll_no
        self.hostel_status = hostel_status
        self.fee_paid = False

    def fee_update(self, status):
        """
            Update the fee payment status.

        Args:
            status (bool): True if fee is paid, False otherwise.
        """
        self.fee_paid = status

    def display_details(self):
        """
        Display the details of the student.
        """
        print(f"Name: {self.name}")
        print(f"Roll No.: {self.roll_no}")
        print(f"Hostel Status: {'Yes' if self.hostel_status else 'No'}")
        print(f"Fee Paid: {'Yes' if self.fee_paid else 'No'}")

if __name__ == "__main__":
    student1 = sru_student("Alice", "SRU123", True)
    student1.fee_update(True)
    student1.display_details()
