#from future import unicode_literals, print_function  # python2
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
import base64

def test():
    private_key = """-----BEGIN RSA PRIVATE KEY---—
    MIIJKAIBAAKCAgEAo3MoMVoj+TwUm/rOg6DDON5rx/hGTAlulySG5GL1Gaz4pAFd
    TpiWDpY0DlOKgxMLweTwui4DzfLfpvROcsv9txJtC4d4jEo5Dq4aG0H0q3y01K4Z
    U51IqrY3YhCbyG7gzAV1yOrvYjsU0cskndEMy4ZJMVXDaCBDXf2J03A0eIT8qCb0
    vCB2c7WK4sX7F9hAzr1h+vDmCS5d4k34pwvKfb0MV5W5mS1Uz8rBNTk47oX9Tax0
    LLElS+aLlG0O8G8MmD8HRAxu4VkpzMTNrn2pgaYYtANWy2tkZW0+vjk64zHwTX/c
    FFM5iG1jDingoN3CUX+igpliBshx4zTVkM4mqh2eXy7XCUDqKwurrx62XP7Vi3/f
    hm2miyOiTFtLcR0dU+L2RG+nxpjVJEx8XgsfW5AOC5fAjkm5h40ATgz0z/3YgPh6
    DaYY+4Cv7H7YXOIjZ9XeOkDCsYrucuSzshgHttshtDQZtwBe9YHbX4d/CnWb56+0
    1j1HxjJH5G+07MW8zW5cogOum+5+HhYgh1fozxCu2Msg/niBCOpXxnrru5zwI11M
    21P2dRlgNfwP/t9RELojIg7ZjvVpjNcTc+veK/VbXaIMDQYuzRHt6+TRs6a51iCp
    AnD5qa43v47sJ5m+YPJqG+Ff60e65ionYmm+CClSNQpruAUHYCBrnGblCtUCAwEA
    AQKCAgEAjlkYRALxGXqNqFqByHkWDE0JKRq8fjQosFELeZQFSdsuoAbgMDcLWKDP
    rTpsg0LvFmpAjKTOg2pmBYz3VVr7F5lgho3xGpz5nCNccSi74S22fxMw03VDeAlB
    qpI0WhbWiFio/9Y7rR0vQJbeyOLrdcT5sZGzoNeYVB8fDZnG2L9ZG0jyE3ViM9uD
    nYQ27clUh7i/wEBU1uIeuZyWVUUbkO439X9cKF8mYeF+6s9vGaxvslniw5lzlequ
    3REt1Y+hNGaP+V+qoW95y/AKAVFHcrYpBX1y9a4NvZeq8Rf+hSdU1OnpzXm9vWcm
    wYsPKop3VWsHKR5UFPw001+ML5Sabl692VvFKO1V+yvWkbaF3qYrWXwgjRZiWgIn
    wDO6cn/0LiyiVMkALULaWG3wrdQRzAmKcdKazsvTlnfDhIgJs8YryBvCnxqH5QyJ
    Iup/w/MJJjIjOaCyyDBHOX6WHlwoWLAk3CgZ0gasqcFs36CiwxRo3UEz1IFx4NuR
    qcSjK3KxQlU/3dTECULCm4IfcVGgIwTgqXuRoaRM+DwBLFljD4QzzSo6bRGMfC4T
    LZRlrJ4sJdxOUAB9sxFwhsTwVYtXYOrRbhOBJGhjkXosgiR2ibJIuS4T7B5s6Rs5
    cK+SHNO1qgLRjhOOdT36oALx2iSrYisCTZ0AM5cbrF9UHUQ85QECggEBAOV1XHaQ
    CdHYWDkcjC9E1j3O4r6dBUu/Dh90Y/f+PBGMEylEj8RK3+pzAHPuaAWlwgbebxLD
    MtxN+ZlJwz2nG82px7YLfEaUBbsBOMqabxsvEhXV0ooSNs6G1cCWnpJMq93h7wse
    ilW5BvCwqNC9zwXauFpfBFz+n5SXH+/lKNZLTu/FSuL53hQL/Epzp8ODKMiEPuXq
    VUbWMYRVBpZ7NsSdqgFY0OjeYVGmJBaBKPyu9srW8ZTVITm2aEMayw1pN2mkvag7
    aOHt7jz+Rq/oe37OxQcDzawN05Ye1zPmrft/gE+m5F4GLkqjiQZUUA6dP/jMrFP1
    oC2M5iaHO1wwNAUCggEBALZbLFXudLPzMiuzOg5t7tRbgPI6xDNdBJywE7e86m+O
    9vv3RkgOIUfjY+BDoe25CeKlhb9nGFWQ3IlU/uhtyH970uYz9bGoYKB2h/vHT1h8
    oIygIhXBwKyVWvwI/vzYv9mlsQs+esLyNw6m/HrJCawEx3Ibk2HF64w4/M5DaaFF
    ccNZYFQibHp2TVXKLGqIwdWvtnTVysVYiy5HmwMac7Jcsb0Wb82Qr9HG09c5+FUq
    QV309XldIYF7qxxmDXvG+vVycfP4QVoFzOIKxUx7gCGp9hq3g5dme6cqT5DHKgqr
    d3ISmgo/F5/jbwUjFWmeFks7z8xOJ2G3kWAr6DnBhJECggEALsBn03xrk8b5ysEn
    SuZCpJtHlcDWeGV4Ei6bw8aYJJcevFTM2hjLYLCH0hcsOKJaUx31EaSV808r4PCn
    iCNJRfEm0M+sRZEZTc3k7Vrj8mz3yV0kpZ8qbZAJc1D9BB/9EJtdIi3Zz7eAU4Ab
    FVTnHnE/CKK9d9klWJgmGLHfTTJQ5geTx4VTm1AJ2n2QHATYRWq0ihHhyCoSMr1E
    N1rpgMwC/H1FK31L5N/uEGvGlx1rCU8cL8/xEho5ShrmblgWwz6eqe1Y5FefJ+:laughing:
    KMo8h0zH1jMPL9QtXTPxcxC4ODr1QMVnWET4H5sMay64lRGzHBVPs1ejiERiDE2X
    aaQkpQKCAQB7f4OnLrcap7lynw7SduEoMFBDvEjkADr/Yr/3z5l1s/zQ58ZRRkCD
    zxv05djkhkyLkk3iMo/oYxL4bvezsaX3sIREIyxiBQZrpdqySWkTJFQW6Nwsn+s8
    9mmIBw+pbaGAZRZh5w58uE1RPwX+oehK93GbddF6he/gJzgO+Niwv7cr9Xunfyi4
    RyZY03MBM10Sus12ktOgkzavQQ9aKq/wO5aj2G4fab2o9F7DhB8KjnN2jk8wwkHO
    z1IzCWpYSYnscHV8JMUdkpAPBfxYr8s3AUQLE/2qq11S+PSpuDhgwX9DYhWwmsoF
    HqIxeHEn9khi6z7vvn4tT4TE/PdpJgYBAoIBAFVc+RCT+tz+cd6nVnIqdrS8j80v
    jf8spfV/HwBYq7l+4g+W8RWkgpOM0iI4krhS/8wQRAHRLHIHRV9fzvYR9eVoO9Bq
    ntCIMISx9AE10pja/wV4b8x/XN4BXCW0Zn15wjp1D9+JUVf6VW2kcAjeyMtgcqRe
    9pxWwKXdcTSH0lRzxGSmAuGOmKc7rXAbQA2HL77rtpSLWnhDctPzNtoP+V4RiM+T
    kf8rTJSciJKtEqmCSznVc6JGTy5Xp/WIRygVcEf2qo+MyHh2pwoxfWOmXZmuMO5z
    +eBOq31vtYCUx8grVAvNpjqXmW8ZNMyql4+tyVlCCLTEm8yggAzruuWQ42w=
    —---END RSA PRIVATE KEY-----"""

    rsa = RSA.importKey(private_key)
    cipher = PKCS1_v1_5.new(rsa)

    def encrypt(msg):
        ciphertext = cipher.encrypt(msg.encode('utf8'))
        return base64.b64encode(ciphertext).decode('ascii')

    def decrypt(msg):
        ciphertext = base64.b64decode(msg.encode('ascii'))
        plaintext = cipher.decrypt(ciphertext, b'DECRYPTION FAILED')
        return plaintext.decode('utf8')
    # ciphertext = encrypt('hello stackoverflow!')
    # print(ciphertext)

    ciphertext = "de4UO0mdT5CGzWi9BUlmjD0SaD8WX+Exl8Ty+3dlAllfs2FNZzaU42qKS69BIDiAIJ0N0qMnCoo4HBR+y1+WTMg+wDSX5/N3RC0XhAE0F5L1S2+z9j6GtUdCAFSJscgI0/dp+7bSvwgGJr1phkCf4mzusI237lTsxy712XvSpSpWPE2zUvkvhEcSOg+Ep74nY8b/ZT3xaaD15DUUrV5neEFYOcU9oCgFpffr7BNo+DLzsjvjkgSH2QhCSLbSp1C2wMEQN/GQViuJCPgtbU8PYc3OO6OLdbxcoTdS8RgQ4Li0DfbaZI+5+l0oNRrNxj92AFiXeqjVkWMS7tUbuvrCUj0dKquyOLtHhKvXfUWUNv6LbBAEMGUXK6m6BkKZsDt6RWPQARbJ+M8Q7X+ES4rEtlSz7pbznNWnxoYHOlIx9fzdbVM/8wexbXLWw5M84JgYmqROcqSWcunBWEZ4sOl360/R0viyGa65lqaO395gWgYNlNhTtaKM6MN7KjdNWkIb405DhGwFzB3SLpyZqPEsOzjHkis3weClcaUhsNzjOaD020tCU2UfpNqslcA06FW4lUl/YpDFKaPyU4M1J63OIq3dJcJs3D/LP6dbjfA80ZwJ1U29jBv08oKyQ9Jm3WiDmEwUO71mcgIb7k+mi1i0H3NOsCoeFMTA7eawH9SBHhU="
    plaintext = decrypt(ciphertext)
    print(plaintext)