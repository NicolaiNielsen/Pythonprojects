#collect email form user
#slice the email @
#save first part as username, save 2nd part as domain

print("Enter email")
email = input()

(username, domain) = email.split("@")
print(username + "" + domain)

