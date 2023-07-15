import subprocess
import json

#Bu uygulama ile telefonunuzdaki smslerinizi okuyabilirsiniz.
#www.ebubekirbastama.com
#www.ebubekirbastama.com.tr
#www.csharpegitimi.com.tr
def read_sms():
    command = 'adb shell content query --uri content://sms/'
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, _ = process.communicate()
    output = output.decode().strip()

    # SMS'leri JSON formatında alınan çıktıyı analiz edin
    sms_list = output.split('\n')
    sms_list = [sms.strip() for sms in sms_list]
    sms_list = [sms.split(' ') for sms in sms_list]

    # Her bir SMS'nin bilgilerini bir sözlükte toplayın
    sms_messages = []
    for sms in sms_list:
        sms_info = {}
        for item in sms:
            if ':' in item:
                key, value = item.split(':')
                sms_info[key] = value
        sms_messages.append(sms_info)

    return sms_messages

# SMS'leri okuyun ve ekrana yazdırın
sms_messages = read_sms()
for sms in sms_messages:
    print(json.dumps(sms, indent=4))
