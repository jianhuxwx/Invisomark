import hashlib
from cryptography.fernet import Fernet
import base64
import sys

def compute_hash(file_path):
    hasher = hashlib.sha256()
    with open(file_path, 'rb') as file:
        buf = file.read()
        hasher.update(buf)
    return hasher.digest()

def encrypt_hash(hash_value, key):
    fernet = Fernet(key)
    return fernet.encrypt(hash_value)

def decrypt_hash(encrypted_hash, key):
    fernet = Fernet(key)
    return fernet.decrypt(encrypted_hash)

def save_encrypted_hash(file_path, encrypted_hash):
    with open(file_path, 'wb') as file:
        file.write(encrypted_hash)

def load_encrypted_hash(file_path):
    with open(file_path, 'rb') as file:
        return file.read()

def hash_similarity(hash1, hash2):
    return sum(x == y for x, y in zip(hash1, hash2)) / len(hash1)

def generate_signature(image_path, key, output_file):
    hash_value = compute_hash(image_path)
    encrypted_hash = encrypt_hash(hash_value, key)
    save_encrypted_hash(output_file, encrypted_hash)

def verify_signature(image_path, key, signature_file):
    original_hash = decrypt_hash(load_encrypted_hash(signature_file), key)
    new_hash = compute_hash(image_path)
    similarity = hash_similarity(original_hash, new_hash)
    return similarity > 0.9

def generate_key_from_string(input_string):
    # 使用SHA-256哈希函数处理输入字符串
    hash = hashlib.sha256(input_string.encode()).digest()
    # 将哈希值转换为base64编码
    return base64.urlsafe_b64encode(hash)


#custom_string = "hello_world"
#key = generate_key_from_string(custom_string)
#generate_signature('/Users/david/Desktop/Code/ATP/vulpinium_11.jpeg', key, '/Users/david/Desktop/Code/ATP/signature.pctf')

# 验证
#result = verify_signature('/Users/david/Desktop/Code/ATP/vulpinium_1.jpeg', key, '/Users/david/Desktop/Code/ATP/signature.pctf')
#print("验证成功" if result else "验证失败")
