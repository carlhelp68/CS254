import re

# gets every properly formatted email in string
def get_all_emails(string):
	email_characters = r'[-a-zA-Z0-9!#$%&\'*+=?^_`{}|~;]{1,1}[-a-zA-Z0-9!#$%&\'*+=?^_`{}|~;.]{2,53}@[-a-zA-Z0-9]{1,1}[-a-zA-Z0-9.]*'
	string = re.findall(email_characters, string)  
	return(string)

# Helper function to reorder string with parts from the emails in the string
def repl(m):
	return m.groups(0)[2] + " preceded by @ and then preceded by " + m.groups(0)[0]

# obfuscates emails in string
def obfuscate(string):
	email_characters = r'([-a-zA-Z0-9!#$%&\'*+=?^_`{}|~;]{1,1}[-a-zA-Z0-9!#$%&\'*+=?^_`{}|~;.]{2,53})(@)([-a-zA-Z0-9]{1,1}[-a-zA-Z0-9.]*)'
	return(re.sub(email_characters, repl, string))

# def main():
	# print(get_all_emails('-erR-I$CK5+5is@.s-leepy...cat'))
	# print(obfuscate('eris email is eris@-.sle.--epycat, and YAY has email too: all.done+YAY@compl3t3'))
	# print(obfuscate('Here is my email: turtles@SEA-Turtle'))
# main()


