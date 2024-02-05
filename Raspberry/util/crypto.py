from dotenv import load_dotenv
import os
import secrets
import hashlib

def print_token():
    # Retrieve the token from the specific file (token.env)
    load_dotenv(dotenv_path=".token.env")
    token = os.getenv("HASHED_TOKEN")
    
    if token is None:
        # If the token is not present, generate a new token
        token = secrets.token_hex(32).encode() #64 alphanumeric characters  
        # Save the key to the specific file (token.env)
        salt=secrets.token_hex(8).encode() #salt di 16 caratteri esadecimali
        with open(".token.env", "a") as env_file:
            env_file.write("HASHED_TOKEN=" +  hashlib.sha3_512(token+ salt).hexdigest())
            env_file.write("\nSALT=" +  salt.decode('utf-8'))
        
        print(f"Token created, save it: {token.decode('utf-8')}")
       
       
def get_token_and_salt():
    # Retrieve the token from the specific file (token.env)
    load_dotenv(dotenv_path=".token.env")
    hashed_token = os.getenv("HASHED_TOKEN")
    salt=os.getenv("SALT")

    return hashed_token,salt

def check_token(token: str) -> bool:
    
    hashed_token,salt=get_token_and_salt()
    
    return hashed_token==hashlib.sha3_512((token +salt).encode()).hexdigest()
    

