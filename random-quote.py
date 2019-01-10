import json
import requests

r = requests.get('http://quotesondesign.com/wp-json/posts?filter[orderby]=rand&filter[posts_per_page]=1&callback=%22')

s = r.json()[0]['content']

s = s.replace('<p>','')
s = s.replace('</p>','')
s = s.rstrip("\n")
s = s.rstrip();
a = r.json()[0]['title']

txt = '"'+s+'"' + ' - ' + a


#fix unicode in !, '', etc.
from HTMLParser import HTMLParser
html = HTMLParser()
txt = html.unescape(txt)
print txt

import Tkinter as Tk
label = Tk.Label(None, text=txt, font=('Comic Sans MS', '12'),fg='black')
label.pack()
label.mainloop()