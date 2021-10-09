from django.test import TestCase

# Create your tests here.
class TestLoan(TestCase) :

    def testLoanID(self):
        self.assertAlmostEquals(1,1)


if __name__ == "__main__" :
    TestCase.main()