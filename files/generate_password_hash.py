#!/usr/bin/env python

import sys, getopt

def main(argv):
   password = ''
   try:
     opts, args = getopt.getopt(argv,"hp:",["password="])
   except getopt.GetoptError:
      print 'generate_password_hash.py -p <password> '
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print 'generate_password_hash.py -p <password> '
         sys.exit()
      elif opt in ("-p", "--password"):
         password= arg

   if not(len(argv)): 
        password = raw_input("Password: ")
   from passlib.hash import sha512_crypt
   hash = sha512_crypt.encrypt(password)
   print hash

if __name__ == "__main__":
   main(sys.argv[1:])

