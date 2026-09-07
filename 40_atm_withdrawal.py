"""
Problem 40: ATM Withdrawal
Statement: ATM Withdrawal: Approve or reject a withdrawal based on amount, balance, and minimum-balance rules
"""

balance = float(input("Enter current account balance: "))
amount = float(input("Enter amount to withdraw: "))

minimum_balance = 1000  # Minimum balance that must remain in the account

if amount <= 0:
    print("Invalid withdrawal amount")
elif amount % 100 != 0:
    print("Amount should be in multiples of 100")
elif (balance - amount) < minimum_balance:
    print("Transaction Declined: Insufficient balance (minimum balance rule)")
else:
    balance -= amount
    print("Transaction Approved. Amount withdrawn:", amount)
    print("Remaining balance:", balance)
