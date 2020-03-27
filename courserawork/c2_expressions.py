# Convert elevator floors
# adding the keyword input, allows you to ask the users for an input.
# input prints out the question and then waits for a response, response is submitted by the enter button.
inp = input('European Floor?')
# int() converts the response to an integer.  Responses in the terminal are saved as a string from the start.
usf = int(inp) + 1
print('US Floor', usf)