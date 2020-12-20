import bcrypt

def hashpw(pwd):
    return bcrypt.hashpw(bytes(pwd, "utf-8"), bcrypt.gensalt())

def verify(pwd, hashed):
    return bcrypt.hashpw(bytes(pwd, "utf-8"), hashed) == hashed
