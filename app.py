import streamlit as st
import re

def is_valid_email(email):
    # Regular expression for basic email validation
    email_regex = re.compile(r'^[a-zA-Z][a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')

    # Check if the email matches the regular expression
    if email_regex.match(email):
        # Split email into username and domain
        username, domain = email.split('@')

        # Check username length
        if 3 <= len(username) <= 20:
            # Check for valid characters in the username
            if all(char.isalnum() or char in ['.', '_', '+', '-'] for char in username):
                # Check domain length
                if 3 <= len(domain) <= 20:
                    # Check for valid characters in the domain
                    if all(char.isalnum() or char in ['-', '.'] for char in domain):
                        # Check for a valid top-level domain (TLD)
                        valid_tlds = ["com", "org", "net"]
                        tld = domain.split('.')[-1]
                        if tld in valid_tlds:
                            return True, "Valid Email!"
                        else:
                            return False, f"Invalid Email: Invalid top-level domain '{tld}'"
                    else:
                        return False, "Invalid Email: Invalid characters in the domain"
                else:
                    return False, "Invalid Email: Domain length should be between 3 and 20 characters"
            else:
                return False, "Invalid Email: Invalid characters in the username"
        else:
            return False, "Invalid Email: Username length should be between 3 and 20 characters"
    else:
        return False, "Invalid Email: Does not match the expected format"

def main():
    st.title("Enhanced Email Validator App")

    # Get email input from the user
    email = st.text_input("Enter your Email:")

    if st.button("Validate Email"):
        # Check if the email is valid using the custom function
        is_valid, result_message = is_valid_email(email)

        if is_valid:
            st.success(result_message)
        else:
            st.error(result_message)

            # Additional details on what is wrong with the email
            st.write("Additional Details:")
            if len(email) < 6:
                st.write("- Length should be at least 6 characters.")
            if not email[0].isalpha():
                st.write("- Should start with an alphabetic character.")
            if email.count("@") != 1:
                st.write("- Should contain exactly one '@'.")
            if not (email.endswith(".com") or email.endswith(".org")):
                st.write("- Should end with '.com' or '.org'.")

if __name__ == "__main__":
    main()
