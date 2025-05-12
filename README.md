# **Birthday Wisher Email Sender**

## **Overview:**
This is the Day 32 project from the 100 Days of Code: The Complete Python Pro Bootcamp.

This is a Python-based application that sends birthday reminders via email. It checks for upcoming birthdays stored in a CSV file and sends a personalized birthday email to the individuals whose birthdays match the current date. The app allows you to use a random birthday greeting from pre-existing letter templates and automates the process of wishing people on their special day.

## **How It Works:**
1. The app reads a CSV file (`birthdays.csv`) that contains a list of people with their birthdays and email addresses.
2. The program gets the current date and checks if it matches any birthday in the CSV.
3. If there is a match, the program selects a random birthday greeting from the `letter_templates` folder.
4. The app sends an email using your Gmail account, wishing the individual a happy birthday with the selected greeting.
5. The program uses SMTP to send the email securely.

## **Features:**
- **Personalized Birthday Greetings**
- **Email Sending**
- **Secure Connection**

## **Requirements:**
- **Python 3.x**
- **pandas** 
- **random** 
- **smtplib** 
- **CSV file (`birthdays.csv`)**: Should contain columns like `month`, `day`, `name`, and `email`.
- **Letter Templates**: A folder named `letter_templates` containing `letter_1.txt`, `letter_2.txt`, and `letter_3.txt` for randomly selected greetings.

## **File Formats:**

* **birthdays.csv**: A CSV file with columns `month`, `day`, `name`, and `email`.
* **letter templates**: Text files (`letter_1.txt`, `letter_2.txt`, `letter_3.txt`) located in a folder named `letter_templates`.

## **Instructions:**

**Setup Email**:
   * Replace `MY_EMAIL` and `MY_PASSWORD` with your actual email credentials.
   * Make sure to allow access to less secure apps or use an **App Password** if using services like Gmail.

