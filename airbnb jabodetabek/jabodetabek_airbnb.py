# mengimpor library
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Membuat object url JAKARTA
url = 'https://www.airbnb.com/s/Jakarta--Indonesia/homes?refinement_paths%5B%5D=%2Fhomes&flexible_trip_dates%5B%5D=april&flexible_trip_dates%5B%5D=may&flexible_trip_lengths%5B%5D=weekend_trip&date_picker_type=calendar&source=structured_search_input_header&search_type=autocomplete_click&click_referer=t%3ASEE_ALL%7Csid%3A3a31a533-0c2a-4ad5-a847-3c07e80563cf%7Cst%3ASTAYS_LARGE_AREA_DESTINATION_CAROUSELS&tab_id=home_tab&query=Jakarta%2C%20Indonesia&place_id=ChIJnUvjRenzaS4RILjULejFAAE&disable_auto_translation=false'

# Membuat object page
page = requests.get(url)
page

# Mengambil informasi website 'page'
soup = BeautifulSoup(page.text, 'lxml')
soup

# Sekarang tutorial untuk pergi ke setiap halaman (1,2,3,dst)
hal_next = soup.find('a',{'aria-label':'Next'}).get('href')
hal_next

# menambahkan domain depan
hal_next_lengkap = 'https://www.airbnb.com'+hal_next
hal_next_lengkap

# TAHAP 1
# Membuat Dataframe kosong yang nantinya akan diisi oleh informasi dari website airbnb
dataku = pd.DataFrame({'Links':[''], 'Judul':[''], 'Deskripsi':[''], 'Harga':[''],
                   'Rating':[''], 'Review':['']})

# Mengambil satu demi satu posting kamar
postings = soup.find_all('div', class_ = '_8ssblpx')
for post in postings:
    try: 
        link = post.find('a', class_='_mm360j').get('href')
        link_lengkap = 'https://www.airbnb.com'+link
        judul = post.find('meta', {'itemprop':'name'}).get('content')
        harga = post.find('span', class_='_155sga30').text
        rating = post.find('span', class_='_10fy1f8').text
        review = post.find('span', class_='_a7a5sx').text
        deskripsi = post.find('div', class_='_kqh46o').text
        dataku = dataku.append({'Links':link_lengkap, 'Judul':judul,
                                'Deskripsi':deskripsi, 'Harga':harga, 'Rating':rating,
                                'Review':review}, ignore_index=True)
    except:
        pass 
    
# Membuat Dataframe kosong yang nantinya akan diisi oleh informasi dari website airbnb
dataku2 = pd.DataFrame({'Links':[''], 'Judul':[''], 'Deskripsi':[''], 'Harga':['']})

# Lalu untuk melihat melihat satu demi satu posting kamar lakukan for loop (tanpa rating dan review)
for post in postings:
      link = post.find('a', class_='_mm360j').get('href')
      link_lengkap = 'https://www.airbnb.com'+link
      judul = post.find('meta', {'itemprop':'name'}).get('content')
      harga = post.find('span', class_='_155sga30').text
      deskripsi = post.find('div', class_='_kqh46o').text
      dataku2 = dataku2.append({'Links':link_lengkap, 'Judul':judul,
                                'Deskripsi':deskripsi, 'Harga':harga},
                                ignore_index=True)
# Data yang di dapat akan menjadi lebih banyak dibandingkan dengan data yang diambil dengan mensertakan kolom rating & review hal ini dikarnakan ada beberapa postingan yang memuat kamar baru.
    

# Mulai seperti tahap awal
# 1 Membuat url JAKARTA
url = 'https://www.airbnb.com/s/Jakarta--Indonesia/homes?refinement_paths%5B%5D=%2Fhomes&flexible_trip_dates%5B%5D=april&flexible_trip_dates%5B%5D=may&flexible_trip_lengths%5B%5D=weekend_trip&date_picker_type=calendar&source=structured_search_input_header&search_type=autocomplete_click&click_referer=t%3ASEE_ALL%7Csid%3A3a31a533-0c2a-4ad5-a847-3c07e80563cf%7Cst%3ASTAYS_LARGE_AREA_DESTINATION_CAROUSELS&tab_id=home_tab&query=Jakarta%2C%20Indonesia&place_id=ChIJnUvjRenzaS4RILjULejFAAE&disable_auto_translation=false'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'lxml')

dataku_jakarta = pd.DataFrame({'Links':[''], 'Judul':[''], 'Deskripsi':[''], 'Harga':[''],
                   'Rating':[''], 'Review':['']})

# Lakukan loop mencari panah sampai tidak ada (hal ke 15)
while True:   
    postings = soup.find_all('div', class_ = '_8ssblpx')
    for post in postings:
        try:
            link = post.find('a', class_='_mm360j').get('href')
            link_lengkap = 'https://www.airbnb.com'+link
            judul = post.find('meta', {'itemprop':'name'}).get('content')
            harga = post.find('span', class_='_155sga30').text
            rating = post.find('span', class_='_10fy1f8').text
            review = post.find('span', class_='_a7a5sx').text
            deskripsi = post.find('div', class_='_kqh46o').text
            dataku_jakarta = dataku_jakarta.append({'Links':link_lengkap, 'Judul':judul, 
                                    'Deskripsi':deskripsi, 'Harga':harga, 'Rating':rating,
                                    'Review':review}, ignore_index=True)
        except:
            pass
    
    try:
        hal_next = soup.find('a',{'aria-label':'Next'}).get('href')
        hal_next_lengkap = 'https://www.airbnb.com'+hal_next
        hal_next_lengkap
    except:
        print('Index sudah selesai')
        break
    
    url = hal_next_lengkap
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'lxml')
datakuaa = pd.read_csv('airbnb_jabodetabek_2021-06-04/jakarta.csv')
# convert dataku = pd.DataFrame kedalam csv
data_jakarta = dataku_jakarta.to_csv('jakarta.csv')

# 2 Membuat object url BOGOR
url = 'https://www.airbnb.com/s/Bogor--Jawa-Barat/homes?refinement_paths%5B%5D=%2Fhomes&flexible_trip_dates%5B%5D=april&flexible_trip_dates%5B%5D=may&flexible_trip_lengths%5B%5D=weekend_trip&date_picker_type=calendar&source=structured_search_input_header&search_type=autocomplete_click&click_referer=t%3ASEE_ALL%7Csid%3A3a31a533-0c2a-4ad5-a847-3c07e80563cf%7Cst%3ASTAYS_LARGE_AREA_DESTINATION_CAROUSELS&tab_id=home_tab&query=Bogor%2C%20Jawa%20Barat&place_id=ChIJN4R5EuPDaS4RkLn-FG1XAQM&disable_auto_translation=false'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'lxml')

dataku_bogor = pd.DataFrame({'Links':[''], 'Judul':[''], 'Deskripsi':[''], 'Harga':[''],
                   'Rating':[''], 'Review':['']})

# Lakukan loop mencari panah sampai tidak ada (hal ke 15)
while True:   
    postings = soup.find_all('div', class_ = '_8ssblpx')
    for post in postings:
        try:
            link = post.find('a', class_='_mm360j').get('href')
            link_lengkap = 'https://www.airbnb.com'+link
            judul = post.find('meta', {'itemprop':'name'}).get('content')
            harga = post.find('span', class_='_155sga30').text
            rating = post.find('span', class_='_10fy1f8').text
            review = post.find('span', class_='_a7a5sx').text
            deskripsi = post.find('div', class_='_kqh46o').text
            dataku_bogor = dataku_bogor.append({'Links':link_lengkap, 'Judul':judul, 
                                    'Deskripsi':deskripsi, 'Harga':harga, 'Rating':rating,
                                    'Review':review}, ignore_index=True)
        except:
            pass
    
    try:
        hal_next = soup.find('a',{'aria-label':'Next'}).get('href')
        hal_next_lengkap = 'https://www.airbnb.com'+hal_next
        hal_next_lengkap
    except:
        print('Index sudah selesai')
        break
    
    url = hal_next_lengkap
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'lxml')
    
# convert dataku = pd.DataFrame kedalam csv
data_bogor = dataku_bogor.to_csv('bogor.csv')

# 3 Membuat object url DEPOK
url = 'https://www.airbnb.com/s/Depok--Kota-Depok--Jawa-Barat/homes?refinement_paths%5B%5D=%2Fhomes&flexible_trip_dates%5B%5D=april&flexible_trip_dates%5B%5D=may&flexible_trip_lengths%5B%5D=weekend_trip&date_picker_type=calendar&source=structured_search_input_header&search_type=autocomplete_click&click_referer=t%3ASEE_ALL%7Csid%3A3a31a533-0c2a-4ad5-a847-3c07e80563cf%7Cst%3ASTAYS_LARGE_AREA_DESTINATION_CAROUSELS&tab_id=home_tab&query=Depok%2C%20Kota%20Depok%2C%20Jawa%20Barat'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'lxml')

dataku_depok = pd.DataFrame({'Links':[''], 'Judul':[''], 'Deskripsi':[''], 'Harga':[''],
                   'Rating':[''], 'Review':['']})

# Lakukan loop mencari panah sampai tidak ada (hal ke 15)
while True:   
    postings = soup.find_all('div', class_ = '_8ssblpx')
    for post in postings:
        try:
            link = post.find('a', class_='_mm360j').get('href')
            link_lengkap = 'https://www.airbnb.com'+link
            judul = post.find('meta', {'itemprop':'name'}).get('content')
            harga = post.find('span', class_='_155sga30').text
            rating = post.find('span', class_='_10fy1f8').text
            review = post.find('span', class_='_a7a5sx').text
            deskripsi = post.find('div', class_='_kqh46o').text
            dataku_depok = dataku_depok.append({'Links':link_lengkap, 'Judul':judul, 
                                    'Deskripsi':deskripsi, 'Harga':harga, 'Rating':rating,
                                    'Review':review}, ignore_index=True)
        except:
            pass
    
    try:
        hal_next = soup.find('a',{'aria-label':'Next'}).get('href')
        hal_next_lengkap = 'https://www.airbnb.com'+hal_next
        hal_next_lengkap
    except:
        print('Index sudah selesai')
        break
    
    url = hal_next_lengkap
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'lxml')
    
# convert dataku = pd.DataFrame kedalam csv
data_depok = dataku_depok.to_csv('depok.csv')

# 4 Membuat object url TANGSEL
url = 'https://www.airbnb.com/s/Tangerang-Selatan--South-Tangerang-City--Banten--Indonesia/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_dates%5B%5D=april&flexible_trip_dates%5B%5D=may&flexible_trip_lengths%5B%5D=weekend_trip&date_picker_type=calendar&query=Tangerang%20Selatan%2C%20South%20Tangerang%20City%2C%20Banten%2C%20Indonesia&place_id=ChIJlcAZBLH6aS4R5K9KLBxIBoc&checkin=2021-04-01&checkout=2021-04-02&adults=1&source=structured_search_input_header&search_type=autocomplete_click'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'lxml')

dataku_tangerang = pd.DataFrame({'Links':[''], 'Judul':[''], 'Deskripsi':[''], 'Harga':[''],
                                  'Rating':[''], 'Review':['']})

# Lakukan loop mencari panah sampai tidak ada (hal ke 15)
while True:   
    postings = soup.find_all('div', class_ = '_8ssblpx')
    for post in postings:
        try:
            link = post.find('a', class_='_mm360j').get('href')
            link_lengkap = 'https://www.airbnb.com'+link
            judul = post.find('meta', {'itemprop':'name'}).get('content')
            harga = post.find('span', class_='_155sga30').text
            rating = post.find('span', class_='_10fy1f8').text
            review = post.find('span', class_='_a7a5sx').text
            deskripsi = post.find('div', class_='_kqh46o').text
            dataku_tangerang = dataku_tangerang.append({'Links':link_lengkap, 'Judul':judul, 
                                    'Deskripsi':deskripsi, 'Harga':harga, 'Rating':rating,
                                    'Review':review},ignore_index=True)
        except:
            pass
    
    try:
        hal_next = soup.find('a',{'aria-label':'Next'}).get('href')
        hal_next_lengkap = 'https://www.airbnb.com'+hal_next
        hal_next_lengkap
    except:
        print('Index sudah selesai')
        break
    
    url = hal_next_lengkap
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'lxml')
    
# convert dataku = pd.DataFrame kedalam csv
data_tangerang = dataku_tangerang.to_csv('tangerang.csv')

# 5 Membuat object url BEKASI
url = 'https://www.airbnb.com/s/Bekasi--Jawa-Barat/homes?refinement_paths%5B%5D=%2Fhomes&flexible_trip_dates%5B%5D=april&flexible_trip_dates%5B%5D=may&flexible_trip_lengths%5B%5D=weekend_trip&date_picker_type=calendar&source=structured_search_input_header&search_type=autocomplete_click&click_referer=t%3ASEE_ALL%7Csid%3A3a31a533-0c2a-4ad5-a847-3c07e80563cf%7Cst%3ASTAYS_LARGE_AREA_DESTINATION_CAROUSELS&tab_id=home_tab&query=Bekasi%2C%20Jawa%20Barat&place_id=ChIJv4cuuHGGaS4Ril-OFHGHMec&disable_auto_translation=false'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'lxml')

dataku_bekasi = pd.DataFrame({'Links':[''], 'Judul':[''], 'Deskripsi':[''], 'Harga':[''],
                                  'Rating':[''], 'Review':['']})

# Lakukan loop mencari panah sampai tidak ada (hal ke 15)
while True:   
    postings = soup.find_all('div', class_ = '_8ssblpx')
    for post in postings:
        try:
            link = post.find('a', class_='_mm360j').get('href')
            link_lengkap = 'https://www.airbnb.com'+link
            judul = post.find('meta', {'itemprop':'name'}).get('content')
            harga = post.find('span', class_='_155sga30').text
            rating = post.find('span', class_='_10fy1f8').text
            review = post.find('span', class_='_a7a5sx').text
            deskripsi = post.find('div', class_='_kqh46o').text
            dataku_bekasi = dataku_bekasi.append({'Links':link_lengkap, 'Judul':judul, 
                                    'Deskripsi':deskripsi, 'Harga':harga, 'Rating':rating,
                                    'Review':review},ignore_index=True)
        except:
            pass
    
    try:
        hal_next = soup.find('a',{'aria-label':'Next'}).get('href')
        hal_next_lengkap = 'https://www.airbnb.com'+hal_next
        hal_next_lengkap
    except:
        print('Index sudah selesai')
        break
    
    url = hal_next_lengkap
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'lxml')
    
# convert dataku = pd.DataFrame kedalam csv
data_bekasi = dataku_bekasi.to_csv('bekasi.csv')


# 6 Membuat object url YOGYAKARTA
url = 'https://www.airbnb.com/s/Yogyakarta--Indonesia/homes?refinement_paths%5B%5D=%2Fhomes&flexible_trip_dates%5B%5D=april&flexible_trip_dates%5B%5D=may&flexible_trip_lengths%5B%5D=weekend_trip&date_picker_type=calendar&source=structured_search_input_header&search_type=unknown&click_referer=t%3ASEE_ALL%7Csid%3A3a31a533-0c2a-4ad5-a847-3c07e80563cf%7Cst%3ASTAYS_LARGE_AREA_DESTINATION_CAROUSELS&tab_id=home_tab&ne_lat=-7.6530994797534895&ne_lng=110.53576003845217&sw_lat=-7.933044211694349&sw_lng=110.18454086120607&zoom=12&search_by_map=true&query=Yogyakarta%2C%20Indonesia'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'lxml')

dataku_yogya = pd.DataFrame({'Links':[''], 'Judul':[''], 'Deskripsi':[''], 'Harga':[''],
                                  'Rating':[''], 'Review':['']})

# Lakukan loop mencari panah sampai tidak ada (hal ke 15)
while True:   
    postings = soup.find_all('div', class_ = '_8ssblpx')
    for post in postings:
        try:
            link = post.find('a', class_='_mm360j').get('href')
            link_lengkap = 'https://www.airbnb.com'+link
            judul = post.find('meta', {'itemprop':'name'}).get('content')
            harga = post.find('span', class_='_155sga30').text
            rating = post.find('span', class_='_10fy1f8').text
            review = post.find('span', class_='_a7a5sx').text
            deskripsi = post.find('div', class_='_kqh46o').text
            dataku_yogya = dataku_yogya.append({'Links':link_lengkap, 'Judul':judul, 
                                    'Deskripsi':deskripsi, 'Harga':harga, 'Rating':rating,
                                    'Review':review},ignore_index=True)
        except:
            pass
    
    try:
        hal_next = soup.find('a',{'aria-label':'Next'}).get('href')
        hal_next_lengkap = 'https://www.airbnb.com'+hal_next
        hal_next_lengkap
    except:
        print('Index sudah selesai')
        break
    
    url = hal_next_lengkap
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'lxml')
    
# convert dataku = pd.DataFrame kedalam csv
data_yogya = dataku_yogya.to_csv('yogya.csv')

# 7 Membuat object url BALI
url = 'https://www.airbnb.com/s/Bali--Indonesia/homes?refinement_paths%5B%5D=%2Fhomes&flexible_trip_dates%5B%5D=april&flexible_trip_dates%5B%5D=may&flexible_trip_lengths%5B%5D=weekend_trip&date_picker_type=calendar&source=structured_search_input_header&search_type=autocomplete_click&click_referer=t%3ASEE_ALL%7Csid%3A3a31a533-0c2a-4ad5-a847-3c07e80563cf%7Cst%3ASTAYS_LARGE_AREA_DESTINATION_CAROUSELS&tab_id=home_tab&query=Bali%2C%20Indonesia&place_id=ChIJoQ8Q6NNB0S0RkOYkS7EPkSQ&disable_auto_translation=false'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'lxml')

dataku_bali = pd.DataFrame({'Links':[''], 'Judul':[''], 'Deskripsi':[''], 'Harga':[''],
                                  'Rating':[''], 'Review':['']})

# Lakukan loop mencari panah sampai tidak ada (hal ke 15)
while True:   
    postings = soup.find_all('div', class_ = '_8ssblpx')
    for post in postings:
        try:
            link = post.find('a', class_='_mm360j').get('href')
            link_lengkap = 'https://www.airbnb.com'+link
            judul = post.find('meta', {'itemprop':'name'}).get('content')
            harga = post.find('span', class_='_155sga30').text
            rating = post.find('span', class_='_10fy1f8').text
            review = post.find('span', class_='_a7a5sx').text
            deskripsi = post.find('div', class_='_kqh46o').text
            dataku_bali = dataku_bali.append({'Links':link_lengkap, 'Judul':judul, 
                                    'Deskripsi':deskripsi, 'Harga':harga, 'Rating':rating,
                                    'Review':review},ignore_index=True)
        except:
            pass
    
    try:
        hal_next = soup.find('a',{'aria-label':'Next'}).get('href')
        hal_next_lengkap = 'https://www.airbnb.com'+hal_next
        hal_next_lengkap
    except:
        print('Index sudah selesai')
        break
    
    url = hal_next_lengkap
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'lxml')
    
# convert dataku = pd.DataFrame kedalam csv
data_bali = dataku_bali.to_csv('bali.csv')
    
#### tanpa rating dan review ###
url = 'https://www.airbnb.com/s/Jakarta--Indonesia/homes?refinement_paths%5B%5D=%2Fhomes&flexible_trip_dates%5B%5D=april&flexible_trip_dates%5B%5D=may&flexible_trip_lengths%5B%5D=weekend_trip&date_picker_type=calendar&source=structured_search_input_header&search_type=autocomplete_click&click_referer=t%3ASEE_ALL%7Csid%3A3a31a533-0c2a-4ad5-a847-3c07e80563cf%7Cst%3ASTAYS_LARGE_AREA_DESTINATION_CAROUSELS&tab_id=home_tab&query=Jakarta%2C%20Indonesia&place_id=ChIJnUvjRenzaS4RILjULejFAAE&disable_auto_translation=false'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'lxml')
dataku2 = pd.DataFrame({'Links':[''], 'Judul':[''], 'Deskripsi':[''], 'Harga':['']})
postings = soup.find_all('div', class_ = '_8ssblpx')

while True:
    postings = soup.find_all('div', class_ = '_8ssblpx')
    for post in postings:
        link = post.find('a', class_='_mm360j').get('href')
        link_lengkap = 'https://www.airbnb.com'+link
        judul = post.find('meta', {'itemprop':'name'}).get('content')
        harga = post.find('span', class_='_155sga30').text
        deskripsi = post.find('div', class_='_kqh46o').text
        dataku2 = dataku2.append({'Links':link_lengkap, 'Judul':judul, 
                                  'Deskripsi':deskripsi, 'Harga':harga}, 
                                 ignore_index=True)
    
    try:
        hal_next = soup.find('a',{'aria-label':'Next'}).get('href')
        hal_next_lengkap = 'https://www.airbnb.com'+hal_next
        hal_next_lengkap
    except:
        print('Index sudah selesai')
        break
    
    url = hal_next_lengkap
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'lxml')
# Menghilangkan baris pertama
dataku2 = dataku2.iloc[1:]

# Menghilangkan baris pertama
dataku = dataku.iloc[1:]

# Eksport ke csv
dataku.to_csv('web_scrap_multi.csv', index=False)

# Membuka file yang sudah disimpan
buka = pd.read_csv('web_scrap_multi.csv')
