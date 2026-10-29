import json
sv=lambda *a:[{'title':t,'desc':d} for t,d in a]
json.dump([dict(slug='sample-cafe',name='Sample Cafe',suburb='Dunedin',kind='cafe',preset='espresso-latte',font='fraunces',layout='b',
 headline='Coffee worth the walk.',sub='Small-batch espresso, fresh baking and a warm corner table.',cta_label='Say hello',cta_url='mailto:hello@example.com',
 words=['Espresso','Flat white','Baking','Brunch','Takeaway'],serv_title='On the menu',
 services=sv(('Espresso','Rich and balanced.'),('Brunch','Served all morning.'),('Baking','Fresh each day.')),
 address='Dunedin',phone='',email='hello@example.com',close='Pull up a chair',close_sub='Message us to book a table.',
 facts=[('Where','Dunedin'),('Open','Daily'),('Bring','A friend')],card=('Warm welcome','Come in<br>for a brew.'),band=('Takeaway','Order ahead and pick up.'))],open('cfg.json','w'))
