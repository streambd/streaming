from this playlist :
https://raw.githubusercontent.com/abusaeeidx/BDxTV/refs/heads/main/playlist_s.m3u

need to update playlist with reffere token like this : 
#EXTVLCOPT:http-referrer=http://www.fawanews.sc/
#EXTVLCOPT:http-origin=http://www.fawanews.sc
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36
#EXTINF:-1 group-title="Rugby World Cup" tvg-name="England vs Tonga" tvg-logo="https://pbs.twimg.com/profile_images/1597190896885309440/ZVwKqVO3.jpg",England vs Tonga
http://193.47.62.55/hls/5GGGAAA.m3u8

otherwise it will not play now currently its only updatine the playlist only like this 
#EXTINF:-1 group-title="Rugby World Cup" tvg-name="England vs Tonga" tvg-logo="https://pbs.twimg.com/profile_images/1597190896885309440/ZVwKqVO3.jpg",England vs Tonga
http://193.47.62.55/hls/5GGGAAA.m3u8

update update.py code to get referrer token part also
