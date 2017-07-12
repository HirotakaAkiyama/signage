from django.shortcuts import render
from urllib.request import urlopen
from bs4 import BeautifulSoup

# Create your views here.
def post_list(request):

    html = urlopen("http://www.hakobus.jp/result.php?in=165&out=155")  # web情報の取得
    soup = BeautifulSoup(html, "html.parser")  # 扱える形に変換

    # バス時刻表
    times_soup = soup.findAll('td', {'width': '50'})  # バスの時刻表が書いてあるタグを指定して抜き出す
    busTime_Array = []
        # listに似たものになっているため切り分けてテキストとして配列に保存
    for bus_times in times_soup:
        for bus_time in bus_times.findAll('div'):  # さらに細かくタグを指定して正確に情報を抜き出す
            bus_time = bus_time.text
            if bus_time != "":  # 空白を除く
                busTime_Array.append(bus_time)  # 配列に追加

    # バス行き先
    dests_soup = soup.findAll('td', {'width': '120'})  # バスの行き先が書いてあるタグを指定して抜き出す
    busDest_Array = []
    # データを切り分けてテキストとして配列に保存
    for bus_dests in dests_soup:
        for bus_dest in bus_dests.findAll('div'):  # さらに細かく指定して正確に情報を抜き出す
            bus_dest = bus_dest.text
            busDest_Array.append(bus_dest)  # 配列に追加

    # バス接近情報
    infos_soup = soup.findAll('td', {'width': '160'})  # バスの接近情報が書いてあるタグを指定して抜き出す
    busInfo_Array = []
    # データを切り分けてテキストとして配列に保存
    for bus_infos in infos_soup:
        bus_infos = bus_infos.text
        busInfo_Array.append(bus_infos)  # 配列に追加

    Arrays = {
        'busTimes':busTime_Array,
        'busDests':busDest_Array,
        'busInfos':busInfo_Array,
    }

    #print(busTime_Array)
    #print(busDest_Array)
    #print(busInfo_Array)

    return render(request, 'sig/post_list.html', Arrays)
