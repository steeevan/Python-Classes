**Problem 1:** Create a program that calculates the area of a rectangle. Ask the user to input the
length and width of the rectangle and display the calculated area.
question1 = int(input(&quot;What is length of the rectangle?&quot;))question2 = int(input(&quot;What is width of the
rectangle?&quot;))answer = question1 * question2print(answer)

**Problem 2:** Write a program that calculates the square of the first 10 positive integers and stores
the results in a list. Print the list of squares.
list =
[1,2,3,4,5,6,7,8,9,10]print(list[0]**2)print(list[1]**2)print(list[2]**2)print(list[3]**2)print(list[4]**2)print
(list[5]**2)print(list[6]**2)print(list[7]**2)print(list[8]**2)print(list[9]**2)

**Problem 3:** Implement a program that checks if a given year is a leap year. Ask the user to input a
year and display whether it&#39;s a leap year or not.
year = int(input(&quot;What year is it?&quot;))if (year%400 == 0) or (year%4==0 and year%100!=0): print(&quot;It is a
leap Year&quot;)else: print(&quot;Not a leap Year&quot;)

**Problem 4:** Create a program that simulates a simple ATM machine. Allow the user to deposit
and withdraw funds from their account. Keep track of the account balance.def __init__(self, balance):
self.balance = balance def check_balance(self): return self.balance def deposit(self,
amount): self.balance += amount return f&quot;Deposited {amount} units. New balance:
{self.balance}&quot; def withdraw(self, amount): if self.balance &gt;= amount: self.balance -=
amount return f&quot;Withdrawn {amount} units. New balance: {self.balance}&quot; else: return
&quot;Insufficient funds.&quot;def main(): initial_balance = 1000 atm = ATM(initial_balance) while True:
print(&quot;Options:&quot;) print(&quot;1. Check Balance&quot;) print(&quot;2. Deposit&quot;) print(&quot;3. Withdraw&quot;)
print(&quot;4. Exit&quot;) choice = int(input(&quot;Enter your choice: &quot;)) if choice == 1:
print(&quot;Balance:&quot;, atm.check_balance()) elif choice == 2: amount = float(input(&quot;Enter deposit
amount: &quot;)) print(atm.deposit(amount)) elif choice == 3: amount = float(input(&quot;Enter
withdrawal amount: &quot;)) print(atm.withdraw(amount)) elif choice == 4: print(&quot;Exiting...&quot;)
break else: print(&quot;Invalid choice. Please choose again.&quot;)if __name__ == &quot;__main__&quot;: main()

**Problem 5:** Write a program that prompts the user for their age and checks if they are eligible to
vote (18 years or older).

Age = int(input(&quot;How old are you?&quot;))if Age &gt;= 18: print(&quot;Eligible to vote&quot;)else: print(&quot;Not eligible to
vote&quot;)

**Problem 6:** Implement a temperature conversion program that converts Fahrenheit to Celsius.
Ask the user for a temperature in Fahrenheit and display the equivalent temperature in
Celsius.Degrees = int(input(&quot;How many degrees Farenheit?&quot;))Degrees = (Degrees - 32) *
5/9print(Degrees)

**Problem 7:** Create a program that generates a list of the first 20 odd numbers. Print the list.
print(&quot;1&quot;)print(&quot;3&quot;)print(&quot;5&quot;)print(&quot;7&quot;)print(&quot;9&quot;)print(&quot;11&quot;)print(&quot;13&quot;)print(&quot;15&quot;)print(&quot;17&quot;)print(&quot;19&quot;)pri
nt(&quot;21&quot;)print(&quot;23&quot;)print(&quot;25&quot;)print(&quot;27&quot;)print(&quot;29&quot;)print(&quot;31&quot;)print(&quot;33&quot;)print(&quot;35&quot;)print(&quot;37&quot;)print(&quot;39&quot;
)

**Problem 8:** Write a program that asks the user to input a number and determines if it&#39;s a prime
number.num = int(input(&quot;What number?&quot;))if num &gt; 1: for i in range(2, int(num/2)+1): if
(num % i) == 0: print(num, &quot;is not a prime number&quot;) break else: print(num, &quot;is a prime
number&quot;)else: print(num, &quot;is not a prime number&quot;)

**Problem 9:** Implement a basic grade calculator. Ask the user to input a percentage score and
display their corresponding letter grade (A, B, C, D, F).grade = int(input(&quot;Enter the grade(1-100): &quot;))if
grade &gt;= 90: print(&quot;A&quot;)elif grade &lt;= 89 and grade &gt;= 80: print(&quot;B&quot;)elif grade &lt;= 79 and grade &gt;= 70:
print(&quot;C&quot;)elif grade &lt;= 69 and grade &gt;= 60: print(&quot;D&quot;)else: print(&quot;F&quot;)

**Problem 10:** Create a program that generates a random number between 1 and 50. Allow the
user to guess the number and provide feedback (higher, lower, or correct) until they guess it
correctly.import randomdef main(): target_number = random.randint(1, 50) guessed_number = 0
attempts = 0 print(&quot;Welcome to the Guess the Number game!&quot;) while guessed_number !=
target_number: try: guessed_number = int(input(&quot;Please guess a number (between 1 and 50):
&quot;)) attempts += 1 if guessed_number &lt; target_number: print(&quot;Your guess is too low.
Try again!&quot;) elif guessed_number &gt; target_number: print(&quot;Your guess is too high. Try
again!&quot;) else: print(f&quot;Congratulations! You guessed the correct number {target_number}.
It took you {attempts} attempts.&quot;) except ValueError: print(&quot;Please enter a valid number.&quot;)if
__name__ == &quot;__main__&quot;: main()
**Problem 11:** Write a program that takes a list of numbers as input and prints the sum of all the
numbers divisible by 3 in the list.
divisible = [3,636,7,578,23,8,4,3]if (divisible[0]%3==0): print(&quot;3 is divisible by 3&quot;)if (divisible[1]%3==0):
print(&quot;636 is divisible by 3&quot;)if (divisible[2]%3==0): print(&quot;7 is not divisible by 3&quot;)if (divisible[3]%3==0):

print(&quot;578 is not divisible by 3&quot;)if (divisible[4]%3==0): print(&quot;23 is divisible by 3&quot;)if (divisible[5]%3==0):
print(&quot;8 is divisible by 3&quot;)if (divisible[6]%3==0): print(&quot;4 is divisible by 3&quot;)if (divisible[7]%3==0): print(&quot;3
is divisible by 3&quot;)
