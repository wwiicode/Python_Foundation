from twilio.rest import Client

# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "AC5c9c0fbaf90ace98c3d3a9373ab69c30"
auth_token = "52d42a79ca8f004b789ed8b90ad2aece"
client = Client(account_sid, auth_token)

message = client.messages.create(
	body = "Checking with my pig pig.",
	to="+16505764987", 
	from_="+16283003604")
print(message.sid)
