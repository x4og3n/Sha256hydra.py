import hashlib

def hash_check(hash_value, password):
    
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    
    if hashed_password == hash_value:
        return password
    else:
        return None

def brute_force(hash_value, wordlist):
    
    with open(wordlist, "r", encoding="utf-8", errors="ignore") as file:
        for line in file:
            
            password = line.strip()
            
            result = hash_check(hash_value, password)
            if result:
                print("Parola bulundu:", result)
                return
    print("Parola bulunamadı.")

if __name__ == "__main__":
    
    target_hash = "936a185caaa266bb9cbe981e9e05cb78cd732b0b3280eb944412bb6f8f8f07af"
    # Wordlist faylinin yolu
    wordlist_path = "rockyou.txt"
    
    brute_force(target_hash, wordlist_path)
