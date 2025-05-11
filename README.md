# **Birthday Reminder Email Sender**

## **Overview:**
This is a Python-based application that sends birthday reminders via email. It checks for upcoming birthdays stored in a CSV file and sends a personalized birthday email to the individuals whose birthdays match the current date. The app allows you to use a random birthday greeting from pre-existing letter templates and automates the process of wishing people on their special day.

## **How It Works:**
1. The app reads a CSV file (`birthdays.csv`) that contains a list of people with their birthdays and email addresses.
2. The program gets the current date and checks if it matches any birthday in the CSV.
3. If there is a match, the program selects a random birthday greeting from the `letter_templates` folder.
4. The app sends an email using your Gmail account, wishing the individual a happy birthday with the selected greeting.
5. The program uses SMTP to send the email securely.

## **Features:**
- **Birthday Lookup**: Automatically checks for birthdays on the current date.
- **Personalized Birthday Greetings**: Selects a random birthday template and inserts the recipient's name.
- **Email Sending**: Sends birthday emails through SMTP.
- **Secure Connection**: Uses TLS encryption for secure email sending.

## **Example:**
No visual example here since this is a script that sends emails. However, when executed on the correct day, the recipient will receive a personalized birthday email!

## **Requirements:**
- **Python 3.x** (Ensure you are using Python 3 or later)
- **pandas** (For reading the CSV file with birthdays and email addresses)
- **random** (To randomly select a birthday letter template)
- **smtplib** (For sending emails using SMTP)
- **CSV file (`birthdays.csv`)**: Should contain columns like `month`, `day`, `name`, and `email`.
- **Letter Templates**: A folder named `letter_templates` containing `letter_1.txt`, `letter_2.txt`, and `letter_3.txt` for randomly selected greetings.

### Required Libraries:
- `pandas` – Install via `pip install pandas`
- `smtplib` – Pre-installed with Python for sending emails
- `random` – Pre-installed with Python for selecting random templates

## **Installation:**

1. **Clone or download** the repository to your local machine.
2. Ensure you have **Python 3.x** installed. You can download Python from [here](https://www.python.org/downloads/).
3. Install the required libraries with the following command:

   ```bash
   pip install pandas
````

4. **Update your email credentials** in the script (`MY_EMAIL` and `MY_PASSWORD`) with your own details.

5. **Enable "Less secure apps"** in your email account if required (for Gmail, this can be done in your Google account settings).

6. **Prepare your CSV file** (`birthdays.csv`):

   * Ensure your `birthdays.csv` file contains the following columns: `month`, `day`, `name`, and `email`.
   * Example `birthdays.csv` format:

   ```
   month,day,name,email
   5,11,John Doe,johndoe@example.com
   5,11,Jane Smith,janesmith@example.com
   ```

7. **Place the letter templates** (`letter_1.txt`, `letter_2.txt`, `letter_3.txt`) in a folder named `letter_templates`.

8. **Make sure you have the correct email provider SMTP settings** (currently set for Gmail).

## **Usage:**

1. Run the script using the command:

   ```bash
   python birthday_email_sender.py
   ```

2. The app will:

   * Check if today is anyone's birthday based on the CSV file.
   * If a birthday is found, it will pick a random greeting letter from the `letter_templates` folder.
   * The app will send a birthday email to the person using your Gmail account.

## **Important Notes:**

* **Security Warning**: It's recommended to use **App Passwords** (Google-specific) instead of your main Gmail password, especially if you have two-factor authentication enabled.
* **Less Secure Apps**: If using Gmail, ensure that "Less secure apps" are allowed in your Google account settings. However, a safer option would be to use OAuth2 or App Passwords.

## **File Formats:**

* **birthdays.csv**: A CSV file with columns `month`, `day`, `name`, and `email`.
* **letter templates**: Text files (`letter_1.txt`, `letter_2.txt`, `letter_3.txt`) located in a folder named `letter_templates`.

