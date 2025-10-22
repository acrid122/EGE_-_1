'''
1. Парсер системного лога
Дан лог сервера: "2023-10-15 14:23:45 [ERROR] User 'admin' failed login from IP 192.168.1.100".
Извлеките IP-адрес (последнее слово), замените точки на дефисы, проверьте startswith("192"), примените upper() и 
выведите в f-строке f"🚨 Подозрительный IP: {ip:>15} 🚨". 
Обработайте случай, если IP нет (try-except).
'''
s = "2023-10-15 14:23:45 [ERROR] User 'admin' failed login from IP 192.168.1.100"

ind_ip = s.find('IP')
try:
    print(s[ind_ip + 2])
    ind = s.rfind(' ')
    ip = s[ind + 1:]
    ip = ip.replace('.', '-')
    print(s.startswith('192'))
    ip = ip.upper()
    print(f"🚨 Подозрительный IP: {ip} 🚨")
except IndexError:
    print('Айпишника нет')

'''
2. Анализ чата Discord
Сообщение: "@Alice Hello! Today is a great day! 🎉 #python".
Найдите index первого "@", извлеките имя пользователя (до пробела), 
замените "Alice" на "Developer", примените title(), и ljust(25, '*'), выведите в f-строке f"💬 {username}: {message}".
'''
s = "@Alice Hello! Today is a great day! 🎉 #python"
s1 = s.find("@")
s2 = s[s1 + 1: s.find(" ")]
s2 = s2.replace(s2, "Developer")
print(f"💬 {s2.title().ljust(25,"*")}: {s[s.find(" ") + 1:]}")

'''
Обработка ошибок API
Ответ API: '{"status": "error", "code": 404, "message": "User not found"}'.
Используйте find('"message":'), rsplit('"', 2) для извлечения сообщения, strip('"') и capitalize(), 
затем center(40, '=') и проверьте istitle(). Выведите с f-строкой f"❌ API Error: {error}".
'''
s = '{"status": "error", "code": 404, "message": "User not found"}'
ind = s.find('"message":')
s = s[ind:].rsplit('"', 2)
print(s)
ss = s[1]
ss = ss.strip("'").capitalize().center(40, '=')
print(ss.istitle())
print( f"❌ API Error: {ss}")

'''
Парсинг лога безопасности
Лог: "[SECURITY] 2023-10-15T10:30:00Z | Failed brute force | IP: 203.0.113.42 | Attempts: 127".
Используйте rfind("IP:"), split("|") для части с IP, strip("IP: "), translate(str.maketrans(".:", "--")),
 zfill(15) и rjust(20, ' '). Обработайте если IP нет. Выведите f"🔒 Блокировка: {ip}".
'''
s = "[SECURITY] 2023-10-15T10:30:00Z | Failed brute force | IP: 203.0.113.42 | Attempts: 127"
s = s.split("|")
ss = s[2]
try:
    ind = ss.find('IP:')
    ss = ss.strip("IP: ")
    ss = ss.translate(str.maketrans(".:", "--")).zfill(15).rjust(20, ' ')
    print(f"🔒 Блокировка: {ss}")
except IndexError:
    print("Айпишника ")


print(s)

'''
5. Анализ GitHub issues
Заголовок: "Fix #42: Memory leak in Python 3.11 parser".
Проверьте startswith("Fix"), используйте split("#") для номера issue, zfill(3) на номере, 
replace("Fix", "🔧 RESOLVED"), title() и center(50, '-'). Выведите в f-строке.
'''
s = "Fix #42: Memory leak in Python 3.11 parser"
print(s.startswith("Fix"))
s2 = s.split('#')
ind = s.find('#') + 1
s3 = s[ind: ind + 2].zfill(3)
s = s.replace("Fix", "🔧 RESOLVED")
s = s.title().center(50, '-')
print(f"result: {s, s3}")


'''
Парсинг Slack уведомлений
Общение: "🔔 @team New commit by @john_doe: 'feat: add user authentication' #PR123".
Найдите index("#"), rsplit(" ", 1) для номера PR, strip("#") и int(), примените zfill(4), 
replace("PR", "🎯"), затем ljust(20, ' ') и center(40, '*'). Обработайте если PR нет.
'''
s = "🔔 @team New commit by @john_doe: 'feat: add user authentication' #PR123"
ss = s.find("#")
try:
    idp = s[ss:].rsplit(" ", 1)[-1].zfill(4).replace("PR", "🎯").ljust(20, ' ').center(40, '*')
    print(idp)
except ValueError:
    print("Ошибка")

'''
Обработка HTTP заголовков
Заголовок: "Content-Type: application/json; charset=utf-8".
Используйте split(":"), strip() части, проверьте endswith("json"), 
replace("application", "📄 DATA"), upper() и rjust(35, '_'). Выведите f"📋 {header}". Обработайте если ":" нет.
'''
s = "Content-Type: application/json; charset=utf-8"
try:
    print(s.index(':'))
    s1 = s.split(':')
    s1[1] = s1[1].strip()
    print(s.endswith('json'))
    s = s.replace("application", "📄 DATA").upper().rjust(35, '_')
    print(f"📋 {s}")
except ValueError:
    print('Value Error')
    
'''
Анализ Docker логов
Лог: "2023/10/15 09:45:23 [INFO] Container 'web-app-v2.1' started successfully on port 8080".
Используйте rfind("v"), split("'") для имени контейнера, strip("v"), capitalize() и zfill(10), затем replace("-", "_") и 
center(30, '🐳'). Выведите с f-строкой. 
'''
s = "2023/10/15 09:45:23 [INFO] Container 'web-app-v2.1' started successfully on port 8080"
ss = s.rfind("v")
s1 = s.split("'")
print(f"{s1[1].strip("v").capitalize().zfill(10).replace("-", "_").center(30, '🐳')}")
#____
s = "2023/10/15 09:45:23 [INFO] Container 'web-app-v2.1' started successfully on port 8080"
s1 = s.rfind('v')
ss = s[s1-8:s1+4].split("'")
s = ss[0].capitalize().strip("v").zfill(10).replace("-", "_").center(30, '🐳')
print(f"result: {s}")