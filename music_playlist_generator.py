import random
import pytz
from datetime import datetime
import pandas as pd
import pyfiglet
import requests
path = "pypro.xlsx"
df = pd.read_excel(path)
df = df.fillna('') 

#spotipy
import spotipy 
from spotipy.oauth2 import SpotifyClientCredentials

def get_top_tracks(artist_name):
    # Spotify API credentials
    client_id = 'b23a2888fbd3462eafb9d42b938f0b68'
    client_secret = '032fc421d1f74a398f9c665427cd319a'
    client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


    results = sp.search(q='artist:' + artist_name, type='artist')
    items = results['artists']['items']

    if len(items) > 0:
        artist = items[0]
        artist_id = artist['id']


        top_tracks = sp.artist_top_tracks(artist_id)

        print(f"\nTop tracks of {artist_name}:\n")
        for track in top_tracks['tracks']:
            print(f"{track['name']} - {', '.join([artist['name'] for artist in track['artists']])}")
    else:
        print(f"Artist '{artist_name}' not found on Spotify.")




#video playing funtion
from googlesearch import search
import webbrowser

def play_1st_video(song_name):
    query = song_name + " official audio site:youtube.com"
    search_results = search(query, num=5, stop=5, pause=2.0)

    for url in search_results:
        if "watch" in url and "&list=" not in url:
            video_url = url
            break
    else:
        print("No video found on YouTube.")
        return
    webbrowser.open(video_url)


time = datetime.now(pytz.timezone("Asia/Kolkata"))

def tme(time):
  if 0 <= time.hour < 4:
    tm = [
        "Late-night vibes", "Midnight melodies",
        "Soothing lofi's for the night", "Chill tunes for the midnight hour",
        "Music for moonlit moments"
    ]
  elif 4 <= time.hour < 7:
    tm = [
        "Sunrise serenade", "Morning motivation mix",
        "Refreshing tunes for dawn", "Start your day with music",
        "Upbeat melodies for early risers"
    ]
  elif 7 <= time.hour < 12:
    tm = [
        "Dawn Serenade: Gently waking up with soft melodies",
        "Morning Bliss: Refreshing tunes for a new day",
        "Daybreak Delight: Music to welcome the sunrise",
        "Sunrise Symphony: A playlist for the first light of day",
        "Morning Magic: Energize your day with uplifting melodies"
    ]
  elif 12 <= time.hour < 18:
    tm = [
        "Afternoon chill-out session",
        "Laid-back tunes for the afternoon",
        "Relax and unwind with afternoon melodies",
        "Smooth sounds for a lazy afternoon",
        "Easy-listening playlist for the midday break"
    ]
  elif 18 <= time.hour < 21:
    tm = [
        "Evening unwind playlist", "Golden hour tunes",
        "Soothing melodies for sunset", "Relax and recharge in the evening",
        "Wind down with evening ambiance"
    ]
  else:
    tm = [
        "starry night symphony", "nightly rhythms", "twilight tunes",
        "moonslight's whispers"
    ]
  return tm
print("\033[H\033[J")
print(pyfiglet.figlet_format("Music Playlist Generator ", font="slant"))
print('\t*****♬ ', random.choice(tme(time)), '♬ *****\t')
while True:
  print('Press 1 : Create Playlist By Genre')
  print('Press 2 : Create Playlist By Artist')
  print('Press 3 : Create Random Playlist')
  print('Press 4 : Play The Song')
  print('Press 5 : Spotify Top-Track Playlist')
  print('Press 6 : Exit')

  play = int(input('Enter Your Choice: '))
  print("\033[H\033[J")

  if play == 1:
    print(
        "Available genres are :\n ghazal \t romantic \n qawwali \t instrumental\n festive \t patriotic \n classical \t devotional \n folk"
    )
    genre = input("Enter your favorite genre: ")
    print("\033[H\033[J")
    genre = genre .lower()

    #just checking
    import time
    import sys
    print("generating:")

    animation = [
        "[■□□□□□□□□□]", "[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]",
        "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]",
        "[■■■■■■■■■□]", "[■■■■■■■■■■]"
    ]

    for i in range(len(animation)):
      time.sleep(0.2)
      sys.stdout.write("\r" + animation[i % len(animation)])
      sys.stdout.flush()
    print("\n")

    if genre == 'ghazal':
      print(df['ghazal'])
    elif genre == 'romantic':
      print(df['romantic'])
    elif genre == 'qawwali':
      print(df['qawwali'])
    elif genre == 'folk':
      print(df['folk'])
    elif genre == 'devotional':
      print(df['devotional'])
    elif genre == 'patriotic':
      print(df['patriotic'])
    elif genre == 'classical':
      print(df['classical'])
    elif genre == 'festive':
      print(df['festive'])
    elif genre == 'instrumental':
      print(df['Instrumental'])
    else:
      print('Enter a valid genre')

  elif play == 2:

    print(
        "Available artists are:\n"
      "Mohammed Rafi   : rafi\t\t\tLata Mangeshkar : lata\n"
      "A.R Rahman      : arrahman\t\tShreya Goshal   : shreya\n"
      "Kishore Kumar   : kishore\t\tMukesh          : mukesh\n"
      "Sonu Nigam      : sonu\t\t\tUdit Narayan    : udit\n"
      "Kumar Sanu      : sanu\t\t\tArijit Singh    : arijit\n"
      "Hariharan       : hariharan\t\tVishal Dadlani  : vishal\n"
      "Rahat Fateh Ali Khan : rahat\t\tAtif Aslam      : aslam\n"
      "Sukhwinder Singh: sukhwinder" )


    artist = input("Enter your favorite Indian artist: ")
    print("\033[H\033[J")
    artist = artist.lower()
    #just checking
    import time
    import sys
    print("generating:")
    animation = [
        "[■□□□□□□□□□]", "[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]",
        "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]",
        "[■■■■■■■■■□]", "[■■■■■■■■■■]"
    ]

    for i in range(len(animation)):
      time.sleep(0.2)
      sys.stdout.write("\r" + animation[i % len(animation)])
      sys.stdout.flush()
    print("\n")

    if artist == 'rafi':
      print(df['m_rafi'])
    elif artist == 'lata':
      print(df['lata_mangeshkar'])
    elif artist == 'arrahman':
      print(df['ar_rahman'])
    elif artist == 'shreya':
      print(df['shreya_goshal'])
    elif artist == 'kishore':
      print(df['kishore_kumar'])
    elif artist == 'mukesh':
      print(df['mukesh'])
    elif artist == 'sonu':
      print(df['sonu_nigam'])
    elif artist == 'udit':
      print(df['udit_narayan'])
    elif artist == 'sanu':
      print(df['kumar_sanu'])
    elif artist == 'arijit':
      print(df['arijit_singh'])
    elif artist == 'hariharan':
      print(df['hariharan'])
    elif artist == 'vishal':
      print(df['vishal_dadlani'])
    elif artist == 'rahat':
      print(df['Rahat_fak'])
    elif artist == 'aslam':
      print(df['atif_aslam'])
    elif artist == 'sukhwinder':
      print(df['sukhwinder_singh'])
    else:
      print('Enter a valid Indian artist')

  elif play == 3:
    rgenre =[
        "Tum Hi Ho", "Hungama Hai Kyon Barpa", "Bhar Do Jholi Meri", "Yaman", "Moonlight Sonata", "Aayi Diwali Aayi", "Kaun Hai Voh", "Ae Watan", "Bihu",
        "Channa Mereya", "Dil Mein Ek Lehar Si Uthi Hai Abhi", "Kun Faya Kun", "Bhairavi", "Canon in D", "Rang Barse", "Namo Namo", "I Love My India", "Heege Doora",
        "Raabta", "Ranjish Hi Sahi", "Tajdar-e-Haram", "Malkauns", "Air on the G String", "Holi Khele Raghuveera", "Hey Ganaraya", "Rang De Basanti", "Kaavaan Kaavaan",
        "Phir Le Aaya Dil", "Hoshwalon Ko Khabar Kya", "Ali Maula Ali Maula Ali Dam Dam", "Darbari Kanada", "Eine kleine Nachtmusik", "Balam Pichkari", "Radhe Radhe", "Jai Hind Jai Hind", "Mangal Mangal",
        "Janam Janam", "Chupke Chupke Raat Din", "Mast Qalandar", "Bageshri", "The Four Seasons", "Dholida", "Deva Deva", "Desh Mere", "Amba Bagicha",
        "Soch Na Sake", "Tum Ko Dekha To Yeh Khayal Aaya", "Dama Dam Mast Qalandar", "Todi", "My Favorite Things", "Nagada Sang Dhol", "Phir Bhi Dil Hai Hindustani", "Dum Dum Diga Diga",
        "Tum Se Hi", "Ghazab Kiya Tere Vaade Pe", "Khwaja Mere Khwaja", "Kafi", "So What", "Chogada", "Bharat Hamko Jaan Se Pyaara Hai", "Gali Gali Chor Hai",
        "Pehli Nazar Mein", "Woh Kagaz Ki Kashti", "Allah Hoo", "Bhimpalasi", "Take Five", "Deva Shree Ganesha", "Aye Watan Tere Liye", "Chura Liya Hai Tumne Jo Dil Ko",
        "Enna Sona", "Shaam Se Aankh Mein Nami Si Hai", "Sanu Ik Pal Chain Na Aave", "Desh", "Yardbird Suite", "Pongalo Pongal", "Mere Desh Ki Dharti", "Nimboda Nimboda",
        "Teri Ore", "Koi Fariyaad", "Mera Piya Ghar Aaya", "Durga", "Round Midnight", "Jingle Bells", "Ye Desh Hai Veer Jawano Ka", "Kangna",
        "Kuch Kuch Hota Hai", "Kalyani", "The Thrill Is Gone", "Hum Hindustani",
        "Paniyon Sa", "Bhairavi", "Little Wing", "Ae Mere Pyare Watan",
        "Gazab Ka Hai Din", "Todi", "Boogie Chillen", "Salaam India",
        "Tum Mile", "Kambhoji", "Born Under a Bad Sign", "Aisa Desh Hai Mera",
        "Hasi", "Mohanam", "Hide Away", "Jahaan Daal Daal Par",
        "Kabhi Kabhi Aditi", "Shankarabharanam", "Jessica", "Maa Tujhe Salaam",
        "Hawayein", "Kedaragaula", "Interstellar Overdrive", "Mera Rang De Basanti Chola",
        "Pehla Nasha", "Natabhairavi", "Samba Pa Ti", "Kar Chale Hum Fida",
        "Ishq Wala Love", "Bilahari", "Cause We've Ended As Lovers", "Chak De India",
        "Dil Diyan Gallan", "Anandabhairavi", "Satch Boogie", "Teri Mitti",
        "Marwa", "Rise", "Jai Ho",
        "Jaunpuri", "Oxygène IV", "Sandese Aate Hai",
        "Shuddh Sarang", "Chariots of Fire",
        "Madhuvanti", "Songbird",
        "Jog", "Nostalgia",
        "Oxygène",
        "Music for Airports",
        "Love on a Real Train",
        "Autobahn",
        "Alberto Balsalm"
    ]
    rartist = [
        "Aaj Mausam Bada Beiman Hai", "Meri Awaaz Hi Pehchan Hai", "Dil Se Re", "Dil Dooba", "O Mere Dil Ke Chain",
        "Kahi Door Jab Din Dhal Jaye", "Mein Agar Kahoon", "Jadu Teri Nazar", "Tujhe Dekha To", "Tum Hi Ho", "Tu Hi Re",
        "Beliya", "Sajdaa", "Dil Meri Na Sune", "Aaja Sanam", "Aane Se Uske Aaye Bahar", "Do Pal Ruka", "Tu Hi Re",
        "Jadu Hai Nasha Hai", "Tere Bina Zindagi Se", "Kabhi Kabhi Mere Dil Mein", "Kal Ho Na Ho", "Jo Bhi Kasmein",
        "Dheere Dheere Se", "Channa Mereya", "Roja Janeman", "Jee Le Zara", "Main Jahaan Rahoon", "Jeena Jeena", "Dil Hara Re",
        "Chhup Gaye Sare Nazare", "Tere Bina Zindagi Se Koi", "Jiya Jale", "Bahara", "Yeh Shaam Mastani", "Jeena Yaha Marna Yaha",
        "Suraj Hua Maddham", "Nazar Nazar", "Mera Dil Bhi Kitna Pagal Hai", "Kabira", "Chanda Re Chanda Re", "Bachchan",
        "Aaj Din Chadheyan", "Mein Rang Sharbato ka", "Fashion Ka Jalwa", "Dard-E-Dil", "Ajeeb Dastan Hai Ye", "Taal Se Taal",
        "Saibo", "Pyar Diwana Hota Hai", "Awara Hoon", "Mere Haath Mein", "Chand Chupa Badal Mein", "Tumhein Apna Banane Ki Kasam",
        "Ae Dil Hai Mushkil", "Jhoka Hawa Ka", "Badtameez Dil", "Bol Na Halke Halke", "Piya O Re Piya", "Wo Kisna Hai",
        "Gulabi Ankhein", "Ruk Ja Raat Thehar Ja Re Chanda", "Ishq Bina", "Samjhawan", "Kora Kagaz Tha Ye Man Mera",
        "Sawan Ka Mahina", "Sapna Jahan", "Pehla Nasha", "Ek Ladki Ko Dekha", "Phir Le Aaya Dil", "Bahon Ke Darmiyan",
        "Tumhi Ho Bandhu", "Jiya Dhadak Dhadak", "Jab Koi Baat", "Saaki Saaki", "Kya Hua Tera Wada", "Lag Ja Gale",
        "Yeh Haseen Waadiya", "Dola Re Dola Re", "Mere Sapno Ki Rani", "Chandan Sa Badan", "Sun Zara", "Tip Tip Barsa Pani",
        "Yeh Kaali Kaali Aankhein", "Janam Janam", "Tum Bin Jiya Jaye Kaise", "Kurbaan Hua", "Aas Paas Khuda", "Dil Diyaan Gallan",
        "Dard E Disco", "Likhe Jo Khat Tujhe", "Ek Pyaar Ka Nagma Hai", "Guzarish", "Suna Hai", "Dekha Ek Khwab", "Dum Dum Diga Diga",
        "Do Pal", "Jadu Teri Nazar", "Main Duniya Bhula Doonga", "Soch Na Sake", "Piya Basanti", "Gandi Baat", "Afreen Afreen",
        "O Saathi", "Ramta Jogi", "Maine Pucha Chand Se", "Masakkali", "Jaagi Jaagi Soyi Na Main Saari Raat", "Neele Neele Ambar Par",
        "Kya Khoob Lagti Ho", "Sau Dard Hai", "Dil To Pagal Hai", "Sochenge Tumhe Pyar", "Tera Yaar Hoon Main", "Tu Mile Dil Khile",
        "Manchala", "Mann Ki Lagan", "Tera Hone Laga Hu", "Jai Ho", "Tarif Karoon Kya Uski", "Jai Ho", "Piya O Re Piya",
        "Chala Jaata Hoon", "Dheere Dheere Bol Koi", "Yeh Dil Deewana", "Janam Dekhlo", "Jeeta Tha Jiske Liye", "Samjhawan",
        "Phir Teri Kahani Yaad Aayi", "Chammak Challo", "O Re Piya", "Pehli Nazar Mein", "Chak De India", "Teri Galiyon Mein",
        "Naaadan Parinde", "Dil Kya Kare Jab Kisi Se", "Tauba Ye Matwali Chaal", "Mein Hoon Na", "Ho Gaya Hai Tujhko",
        "Ab Tere Bin Jee Lenge Hum", "Hamari Adhuri Kahani", "Thodi Thodi Piya Karo", "Ude Dil Befikre", "Ehsaas", "Chaiyya Chaiyya",
        "Yeh Duniya Yeh Mehfil", "Kaise Mujhe", "Pal Pal Dil Ke Paas", "Chand Si Mehbooba Ho Meri", "Sathiya", "Tu Jaane Na",
        "Yeh Reshmi Zulfein", "Tere Bina", "Sandese Aate Hai", "Doorie", "Abhi Mujh Mein Kahin", "Tere Bin", "Wo Lamhe Woh Baatein",
        "Aadat"
    ]
    rch = int(
        input(
            "press 1 : random genre playlist \npress 2 : random artist playlist \nenter your choice :"
        ))
    randnum = int(
        input("enter the number of songs you want in your playlist : "))
    if rch == 1 and randnum <= len(rgenre):
        r_list = random.sample(rgenre, randnum)
        for item in r_list:
            print(item)
    elif rch == 2 and randnum <= len(rartist):
        r_list = random.sample(rartist, randnum)
        for item in r_list:
            print(item)
    else:
      print("enter a valid choice or number")
  elif play == 4:
   song_name = input("Enter the song name: ")
   play_1st_video(song_name)
  elif play == 5:
    artist_name = input("Enter the artist name: ")
    get_top_tracks(artist_name)
  elif play == 6:
    
    print("Exiting the program. Thanks for using!")
    break
  else:
    print('Invalid choice. Please enter 1, 2, 3, 4, or 5.')
