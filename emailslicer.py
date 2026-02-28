import csv
import os
import matplotlib.pyplot as plt
from collections import Counter

email_address = [] #["krishnamp2120@gmail.com", "krishnamk2120@gmail.com", "kiaraadvani@outlook.com",
                 #"shraddhakapoor@yahoo.com", "srk@outlook.com", "muskelon@spacex.com", "altmansam@openai.in",
                #"leodicaprio@under25.com", "captaincool@yahoo.com", "kohlivirat18@outlook.com", "khannaashi@gmail.com",
                #"pacinoal@godfather.biz", "leomessi10@gmail.com", "netajibose@ina.in", "bacchanamitabh@outlook.com",
                 #"trump.venezuala.atk", "adolf.likejuice", "error404"]

# Permanent storage file
storage_file = "stored_emails.csv"

# Load stored emails if file exists
if os.path.exists(storage_file):
    with open(storage_file, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if row:  # avoid empty rows
                email_address.append(row[0])

usernames_by_domain = {}
usernames = []
domains = []
valid_emails = []
invalid_emails = []
for email in email_address:
    email = email.strip()
    if "@" in email and "." in email:
        valid_emails.append(email)
        username, rest = email.split("@")
        usernames.append(username)
        domain = rest.split(".")[0]
        domains.append(domain)
        # Check if the domain is already in the dictionary, if not add it and append the username to the list
        if domain not in usernames_by_domain:
            usernames_by_domain[domain] = []
        usernames_by_domain[domain].append(username)
    else:
        invalid_emails.append(email)
        # print("Invalid email address")
print(f"{usernames}\n{domains}", end="\n\n")
print(f"The invalid email addresses are: {invalid_emails}", end="\n\n")

# Count the occurrences of each unique domain
# Method 1
# for unique in domains:
#    count = domains.count(unique)
#    print(f"{unique} : {count}")

# max_value = max(domains, key=domains.count)
# print(f"The most common domain is {max_value} with {domains.count(max_value)} occurrences")

# Method 2 using Counter
domain_count = Counter(domains)
if domain_count:
    counter_domain, count = domain_count.most_common(1)[0]
    print(f"The most common domain is {counter_domain} with {count} occurrences")

else:
    counter_domain, count = None, 0

# Print the usernames grouped by domain
print("\nUsernames grouped by domain:")
for domain, usernames in usernames_by_domain.items():
    print(f"{domain} : {usernames}")

# Classify the domains into public and corporate domains

public_list = ["gmail", "outlook", "yahoo"]
public_domains = []
corporate_domains = []
for domain in domains:
    if domain in public_list:
        public_domains.append(domain)
    else:
        corporate_domains.append(domain)

unique_public_domains = list(dict.fromkeys(public_domains))
unique_corporate_domains = list(dict.fromkeys(corporate_domains))

print(f"\nPublic domains: ")
for domain in unique_public_domains:
    print(f"{domain} : {usernames_by_domain[domain]}")

print(f"\nCorporate domains: ")
for domain in unique_corporate_domains:
    print(f"{domain} : {usernames_by_domain[domain]}")

# Count the most arriving public and corporate domains
most_arriving_pd = Counter(public_domains)
most_common_public_domain, counts = most_arriving_pd.most_common(1)[0]
print(most_common_public_domain, counts)
most_arriving_cd = Counter(corporate_domains).most_common(3)
print(most_arriving_cd)

# Count public vs corporate domains
public_domains = [d for d in domains if d in public_list]
corporate_domains = [d for d in domains if d not in public_list]

# Taking user input for email address and validating it, then classifying it as public or corporate domain and adding it to the respective lists
while True:
    new_email = input("Enter your email address: ").strip()
    if new_email == "":
        break

    if "@" in new_email and "." in new_email:
        print("Valid email address. \nAdding it to the database of valid emails.")
        print("Processing your email....")
        valid_emails.append(new_email)
        with open(storage_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([new_email])
        username_new, rest_new = new_email.split("@")
        usernames.append(username_new)
        domain_new = rest_new.split(".")[0]
        domains.append(domain_new)

        if domain_new in public_list:
            public_domains.append(domain_new)
            print("This is a public domain email address.")
            print(f"Welcome {username_new}!")
        else:
            corporate_domains.append(domain_new)
            print("This is a corporate email address.")
        # Check if the domain is already in the dictionary, if not add it and append the username to the list
        if domain_new not in usernames_by_domain:
            usernames_by_domain[domain_new] = []
        usernames_by_domain[domain_new].append(username_new)

    else:
        print("Invalid email address")
        invalid_emails.append(new_email)

# Visualizing Data using Matplotlib

# Bar chart: Valid vs Invalid emails
plt.figure(figsize=(6, 4))
plt.bar(["Valid", "Invalid"], [len(valid_emails), len(invalid_emails)], color=["blue", "red"])
plt.title("Valid vs Invalid Emails")
plt.ylabel("Count")
plt.show()

# Pie chart of public vs corporate emails
plt.figure(figsize=(8, 5))
plt.pie([len(public_domains), len(corporate_domains)],
        labels=["Public", "Corporate"],
        autopct="%1.1f%%",
        colors=["orange", "green"])
plt.title("Distribution of Email Types")
plt.show()

# Bar chart of top domains
domain_count = Counter(domains)
top_domains = domain_count.most_common(5)
domains_names = [d[0] for d in top_domains]
domains_counts = [d[1] for d in top_domains]

plt.figure(figsize=(8, 5))
plt.bar(domains_names, domains_counts, color="maroon")
plt.title("Top 5 Domains")
plt.xlabel("Domain")
plt.ylabel("Count")
plt.show()

# Exporting the data to a CSV file with one username per row and a summary
with open("email_report.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Domain", "Category", "Username", "Count"])

    # Write each username on its own row
    for domain, users in usernames_by_domain.items():
        category = "Public" if domain in public_list else "Corporate"
        for user in users:
            writer.writerow([domain, category, user, 1])

    # Add an empty row before summary
    writer.writerow([])

    # Summary message
    total_emails = len(valid_emails) + len(invalid_emails)
    summary_lines = [
        ["Summary"],
        [f"Total emails processed: {total_emails}"],
        [f"Valid emails processed: {len(valid_emails)}"],
        [f"Invalid emails processed: {len(invalid_emails)}"],
        [f"Most common domain: {counter_domain} ({count} occurrences)"],
        [f"Most common public domain: {most_common_public_domain} ({counts} occurrences)"],
        ["Most common corporate domains:"]
    ]

    # Add top 3 corporate domains
    for corp_domain, corp_count in most_arriving_cd:
        summary_lines.append([f"{corp_domain} ({corp_count} occurrences)"])

    # Write summary to CSV
    writer.writerows(summary_lines)
