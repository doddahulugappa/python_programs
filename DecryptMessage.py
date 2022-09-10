import gnupg
passwd = ""
# gpg = gnupg.GPG(gnupghome=r"S:\DecryptRestAPI\gnupg",gpgbinary=r'C:\Program Files (x86)\GnuPG\bin\gpg.exe')
gpg = gnupg.GPG(gpgbinary=r'C:\Program Files (x86)\GnuPG\bin\gpg.exe')

# input_data = gpg.gen_key_input(
#     name_email = "@gmail.com",
#     passphrase = "",
#     key_type = "RSA",
#     key_length = 1024
#
# )
message = """-----BEGIN PGP MESSAGE-----
Version: GnuPG v2
jA0ECQMCVady3RUyJw3X0kcBF+zdkfZOMhISoYBRwR3uk3vNv+TEg+rJnp4/yYIS
pEoI2S82cDiCNBIVAYWB8WKPtH2R2YSussKhpSJ4mFgqyOA01uwroA== =KvJQ
-----END PGP MESSAGE-----"""

decrypted_data = gpg.decrypt(message, passphrase=passwd)
print(decrypted_data)
