from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
import sqlite3

def search(request):
    # GET 방식으로 title 이라는 이름으로 값 전달
    title = request.GET.get('title')
    desc = request.GET.get('desc')
    print(title)
    return HttpResponse('검색어 : %s, %s' % (title, desc))

def shopD(request):
    conn = sqlite3.connect('sqlite_shop_data.db')
    cursor = conn.cursor()
    sql = '''
        SELECT * FROM shop 
        ORDER BY shop_id desc limit ?, 20
    '''

    new_page =1
    start = (new_page-1)*20

    cursor.execute(sql, (start,))
    result = cursor.fetchall()

    html = ''''''
    for row in result:
        html += '%s, %s, %s, %s, %s, %s,<br>' % (row[0],row[1],row[2],row[3],row[4],row[5])

    cursor.close()
    conn.close()

    return HttpResponse(html)

def data(request):
    d = { 'name': '홍', 'age': 33}
    return JsonResponse(d)

def main(request):
    text = '''
        <ul>
            <li>1</li>
            <li>2</li>
        </ul>
    '''
    return render(request, 'main.html')
    return HttpResponse(text)

def shop(request):
    conn = sqlite3.connect('sqlite_shop_data.db')
    cursor = conn.cursor()
    sql = '''
        SELECT * FROM shop
        ORDER BY shop_id DESC
    '''
    cursor.execute(sql)
    result = cursor.fetchall()

    html = ''
    for row in result:
        html += '매장명: %s<br>' % row[1]

    cursor.close()
    conn.close()

    return HttpResponse(html)
    #return JsonResponse(result, safe=False)