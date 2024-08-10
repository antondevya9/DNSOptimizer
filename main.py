import dns.resolver
import time
import speedtest
import psutil
import subprocess
import os
import ctypes
import sys

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
if is_admin():
    pass
else:
    print("Запустите от имени Администратора!")
    input("Нажмите любую кнопку для выхода...")
    sys.exit()
    

w1 = "blank"
w2 = "blank"
w3 = "blank"
w4 = "blank"
w5 = "blank"
w6 = "blank"
w7 = "blank"
w8 = "blank"
w9 = "blank"
w10 = "blank"
w11 = "blank"
w12 = "blank"
w13 = "blank"
w14 = "blank"
w15 = "blank"
w16 = "blank"
w17 = "blank"
w18 = "blank"
w19 = "blank"
w20 = "blank"
w21 = "blank"

def language_russian():
    global w1, w2, w3, w4, w5, w6, w7, w8, w9, w10, w11, w12, w13, w14, w15, w16, w17, w18, w19, w20, w21
    w1 = "!!! Выберите Ipv4_default, если не знаете что выбрать !!!"
    w2 = "Пинг"
    w3 = "Загрузка"
    w4 = "Выгрузка"
    w5 = "DNS для адаптера"
    w6 = "успешно изменен на"
    w7 = "Ошибка при измении DNS для адаптера"
    w8 = "Тестирование скорости интернета перед сменой DNS, подождите..."
    w9 = "Список IPv:"
    w10 = "Введите номер IPv:"
    w11 = "Тестирование скорости ответа DNS серверов"
    w12 = "Лучший DNS сервер:"
    w13 = "Доступные сетевые адаптеры:"
    w14 = "Выберите адаптер: "
    w15 = "Некорректный выбор"
    w16 = "Вы выбрали:"
    w17 = "Ошибка ввода:"
    w18 = "Тестирование скорости интернета после смены DNS, подождите..."
    w19 = "Тест скорости интернета перед сменой DNS:"
    w20 = "Тест скорости интернета после смены DNS:"
    w21 = "Выбранный DNS:"
def language_english():
    global w1, w2, w3, w4, w5, w6, w7, w8, w9, w10, w11, w12, w13, w14, w15, w16, w17, w18, w19, w20, w21
    w1 = "!!! Choose Ipv4_default if you don't know what to select !!!"
    w2 = "Ping"
    w3 = "Download"
    w4 = "Upload"
    w5 = "DNS for adapter"
    w6 = "successfully changed to"
    w7 = "Error changing DNS for adapter"
    w8 = "Testing internet speed before changing DNS, please wait..."
    w9 = "List of IPv:"
    w10 = "Enter IPv number:"
    w11 = "Testing DNS server response speed"
    w12 = "Best DNS server:"
    w13 = "Available network adapters:"
    w14 = "Select adapter: "
    w15 = "Invalid selection"
    w16 = "You selected:"
    w17 = "Input error:"
    w18 = "Testing internet speed after changing DNS, please wait..."
    w19 = "Internet speed test before changing DNS:"
    w20 = "Internet speed test after changing DNS:"
    w21 = "Selected DNS: "


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("DNSOptimizer\nDeveloper: github.com/antondevya9\n\n")
dns_groups = {
    f"Ipv4_default": {
    "US - Google Public DNS": ["8.8.8.8", "8.8.4.4"],
    "US - OpenDNS": ["208.67.222.222", "208.67.220.220"],
    "US - OpenDNS - 2": ["208.67.222.220", "208.67.220.222"],
    "RU - Yandex": ["77.88.8.1", "77.88.8.8"],
    "AU - Cloudflare": ["1.1.1.1", "1.0.0.1"],
    "US - Norton ConnectSafe Basic": ["199.85.126.10", "199.85.127.10"],
    "US - Level 3 - A": ["209.244.0.3", "209.244.0.4"],
    "US - Level 3 - B": ["4.2.2.1", "4.2.2.2"],
    "US - Level 3 - C": ["4.2.2.3", "4.2.2.4"],
    "US - Level 3 - D": ["4.2.2.5", "4.2.2.6"],
    "US - Comodo Secure": ["8.26.56.26", "8.20.247.20"],
    "US - Dyn": ["216.146.35.35", "216.146.36.36"],
    "US - Norton DNS": ["198.153.192.1", "198.153.194.1"],
    "US - Comodo": ["156.154.70.22", "156.154.71.22"],
    "US - VeriSign Public DNS": ["64.6.64.6", "64.6.65.6"],
    "US - Qwest": ["205.171.3.65", "205.171.2.65"],
    "RU - Safe DNS": ["195.46.39.39", "195.46.39.40"],
    "DE - DNS WATCH": ["84.200.69.80", "84.200.70.40"],
    "US - Sprintlink": ["199.2.252.10", "204.97.212.10"],
    "US - UltraDNS": ["204.69.234.1", "204.74.101.1"],
    "GB - Zen Internet": ["212.23.8.1", "212.23.3.1"],
    "GB - Orange DNS": ["195.92.195.94", "195.92.195.95"],
    "US - Hurricane Electric": ["74.82.42.42"],
    "FR - FDN": ["80.67.169.12", "80.67.169.40"],
    "US - Neustar 1": ["156.154.70.1", "156.154.71.1"],
    "US - Neustar 2": ["156.154.70.5", "156.154.71.5"],
    "RU - AdGuard": ["94.140.14.14", "94.140.15.15"],
    "US - Quad9 Security": ["9.9.9.9", "149.112.112.112"],
    "US - Quad9 No Security": ["9.9.9.10", "149.112.112.10"],
    "US - NextDNS": ["45.90.28.230", "45.90.30.230"]
    },
    "Ipv4_Family": {
    "US - OpenDNS Family": ["208.67.222.123", "208.67.220.123"],
    "US - Norton ConnectSafe Family": ["199.85.126.30", "199.85.127.30"],
    "RU - Yandex Family": ["77.88.8.7", "77.88.8.3"],
    "AU - Cloudflare Malware + Adult Blocking": ["1.1.1.3", "1.0.0.3"],
    "IE - CleanBrowsing Family": ["185.228.168.168", "185.228.169.168"],
    "IE - CleanBrowsing Adult Filter": ["185.228.168.10", "185.228.169.11"],
    "US - Neustar Family Secure": ["156.154.70.3", "156.154.71.3"],
    "US - Neustar Business Secure": ["156.154.70.4", "156.154.71.4"],
    "RU - AdGuard Family": ["94.140.14.15", "94.140.15.16"]
    },
    "Ipv4_Secure": {
    "US - Norton ConnectSafe Secure": ["199.85.126.20", "199.85.127.20"],
    "RU - Yandex Safe": ["77.88.8.88", "77.88.8.2"],
    "AU - Cloudflare Malware Blocking": ["1.1.1.2", "1.0.0.2"],
    "US - Comodo Secure": ["8.26.56.26", "8.20.247.20"],
    "IE - CleanBrowsing Secure": ["185.228.168.9", "185.228.169.9"],
    "US - Neustar Threat Protection": ["156.154.70.2", "156.154.71.2"]
    },
    "Ipv6_Default": {
    "US - Google Public DNS": ["2001:4860:4860::8888", "2001:4860:4860::8844"],
    "US - OpenDNS Sandbox": ["2620:0:ccc::2", "2620:0:ccd::2"],
    "RU - Yandex DNS": ["2a02:6b8::feed:0ff", "2a02:6b8:0:1::feed:0ff"],
    "AU - Cloudflare": ["2606:4700:4700::1111", "2606:4700:4700::1001"],
    "DK - Censurfridns": ["2001:67c:28a4::", "2a01:3a0:53:53::"],
    "US - Cesidian Root": ["2001:470:6c:521::2", "2001:470:6d:521::1"],
    "US - DNS WATCH": ["2001:1608:10:25::1c04:b12f", "2001:1608:10:25::9249:d69b"],
    "US - FDN": ["2001:910:800::12", "2001:910:800::40"],
    "US - Neustar 1": ["2610:a1:1018::1", "2610:a1:1019::1"],
    "US - Neustar 2": ["2610:a1:1018::5", "2610:a1:1019::5"],
    "RU - AdGuard": ["2a10:50c0::ad1:ff", "2a10:50c0::ad2:ff"],
    "US - Quad9 Security": ["2620:fe::fe", "2620:fe::9"],
    "US - Quad9 No Security": ["2620:fe::10", "2620:fe::fe:10"],
    "US - NextDNS": ["2a07:a8c0::46:1af1", "2a07:a8c1::46:1af1"]
    },
    "Ipv6_Family": {
    "RU - Yandex Family": ["2a02:6b8::feed:a11", "2a02:6b8:0:1::feed:a11"],
    "AU - Cloudflare Malware + Adult Blocking": ["2606:4700:4700::1113", "2606:4700:4700::1003"],
    "IE - CleanBrowsing Family": ["2a0d:2a00:1::", "2a0d:2a00:2::"],
    "IE - CleanBrowsing Adult Filter": ["2a0d:2a00:1::1", "2a0d:2a00:2::1"],
    "US - Neustar Family Secure": ["2610:a1:1018::3", "2610:a1:1019::3"],
    "US - Neustar Business Secure": ["2610:a1:1018::4", "2610:a1:1019::4"],
    "RU - AdGuard Family": ["2a10:50c0::bad1:ff", "2a10:50c0::bad2:ff"]
    },
    "Ipv6_Secure": {
    "RU - Yandex Safe": ["2a02:6b8::feed:bad", "2a02:6b8:0:1::feed:bad"],
    "AU - Cloudflare Malware Blocking": ["2606:4700:4700::1112", "2606:4700:4700::1002"],
    "IE - CleanBrowsing Secure": ["2a0d:2a00:1::2", "2a0d:2a00:2::2"],
    "US - Neustar Threat Protection": ["2610:a1:1018::2", "2610:a1:1019::2"]
    }
}
def internet_speedtest():
    st = speedtest.Speedtest()
    st.download()
    st.upload()
    ping = f"{w2}: {round(st.results.ping, 1)} ms"
    download = f"{w3}: {round(st.results.download / (1024 * 1024), 2)} MB/s"
    upload = f"{w4}: {round(st.results.upload / (1024 * 1024), 2)} MB/s"
    results = f"--------------------------\n{ping}\n{download}\n{upload}\n--------------------------"
    return results

def measure_dns_response_time(dns_server):
    try:
        resolver = dns.resolver.Resolver()
        resolver.nameservers = [dns_server]
        start_time = time.time()
        resolver.resolve('google.com', 'A')
        end_time = time.time()
        return (end_time - start_time) * 1000
    except Exception as e:
        return float('inf')

def print_dns_times(group_name, dns_servers):
    times = {}
    for name, servers in dns_servers.items():
        print(f"{name}={', '.join(servers)}")
        for server in servers:
            avg_time = sum(measure_dns_response_time(server) for _ in range(5)) / 5
            times[server] = avg_time
            print(f"  {server}: {avg_time:.2f} ms")
    return times

def get_best_dns_group(dns_servers):
    provider_times = {}
    for dns_server, time in dns_servers.items():
        provider = next((name for name, servers in dns_groups[selected_group].items() if dns_server in servers), "Unknown")
        if provider not in provider_times:
            provider_times[provider] = []
        provider_times[provider].append(time)
    best_provider = min(provider_times, key=lambda p: sum(provider_times[p]) / len(provider_times[p]))
    
    best_dns_servers = [server for name, servers in dns_groups[selected_group].items() if name == best_provider for server in servers]
    
    return best_dns_servers

def get_network_adapters():
    adapters = psutil.net_if_addrs()
    return adapters

def set_dns(adapter_name, dns_servers):
    try:
        subprocess.run(f"netsh interface ip set dns name={adapter_name} source=dhcp", shell=True, check=True)
        
        for index, dns in enumerate(dns_servers):
            cmd = f"netsh interface ip add dns name={adapter_name} {dns} index={index + 1}"
            subprocess.run(cmd, shell=True, check=True)
        
        print(f"{w5} {adapter_name} {w6} {', '.join(dns_servers)}")
    except subprocess.CalledProcessError as e:
        print(f"{w7} {adapter_name}: {e}")

def main():
    clear()
    print("Select language\Выберите язык:")
    print("1 - Русский\n2 - English")
    choosed_language = int(input("Выбор: "))
    clear()
    if choosed_language == 1:
        language_russian()
    elif choosed_language == 2:
        language_english()
    global selected_group
    clear()
    print(w8)
    test1 = internet_speedtest()
    clear()
    print(w1)
    print(w9)
    for idx, group in enumerate(dns_groups.keys(), start=1):
        print(f"{idx}. {group}")

    choice = int(input("\n" + w10))
    selected_group = list(dns_groups.keys())[choice - 1]
    
    clear()

    print(f"{w11} {selected_group}")
    dns_times = print_dns_times(selected_group, dns_groups[selected_group])
    best_dns = get_best_dns_group(dns_times)
    print(w12, best_dns)
    clear()
    adapters = get_network_adapters()
    print(w13)
    for index, adapter in enumerate(adapters, start=1):
        print(f"{index}. {adapter}")

    try:
        choice = int(input(w14)) - 1
        if choice < 0 or choice >= len(adapters):
            raise ValueError(w15)
        
        adapter_name = list(adapters.keys())[choice]
        print(w16, adapter_name)
        
        set_dns(adapter_name, best_dns)
    
    except (ValueError, IndexError) as e:
        print(w17, e)
    clear()
    print(w18)
    test2 = internet_speedtest()
    clear()
    print(w19)
    print(test1)
    print(w20)
    print(test2)
    print(w21, best_dns)

if __name__ == "__main__":
    main()