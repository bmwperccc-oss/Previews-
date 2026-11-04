import json

base={'name':'Sample Day Spa','suburb':'Rotorua','headline':'Breathe out.','sub':'Massage, facials and calm in the heart of town.','cta_label':'Book now','cta_url':'mailto:hello@example.com','words':['Massage','Facials','Wraps','Calm','Gift cards'],'serv_title':'Treatments','services':[{'title':'Massage','desc':'Deep and slow.'},{'title':'Facials','desc':'Glow, gently.'},{'title':'Wraps','desc':'Warm and soft.'}],'address':'Rotorua','phone':'','email':'hello@example.com','close':'Book a visit','close_sub':'Message us to book.','facts':[['Where','Rotorua'],['Open','Tue-Sat'],['Walk-ins','Welcome']],'card':['Fresh start','Slow down.<br>Feel it.'],'band':['Gift cards','Treat someone.'],'kind':'lotus','font':'fraunces'}
out=[]
for slug,pre,lay in [('lotus-a','blush-pink','a'),('lotus-c','forest-lime','c')]:
    d=dict(base);d.update(slug=slug,preset=pre,layout=lay);out.append(d)
json.dump(out,open('cfg.json','w'))
