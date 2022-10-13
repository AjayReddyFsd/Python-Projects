# slice an email into username, domain and extension

# solution
# email_id = input('please enter your email ID: ')

# at_index = email_id.index('@')
# last_dot_index = len(email_id) - 1 - email_id[::-1].index('.')

# username = email_id[:at_index]
# domain_name = email_id[at_index+1:last_dot_index]
# extension_name = email_id[last_dot_index+1::]

# print(f'username = {username}')
# print(f'domain_name = {domain_name}')
# print(f'extension_name = {extension_name}')


# enhanced solution using split function
email_id = input('please enter your email ID: ')

(username, domain_extension) = email_id.split('@')
(domain, extension) = domain_extension.split('.')

print(f'username = {username}')
print(f'domain_name = {domain}')
print(f'extension_name = {extension}')

