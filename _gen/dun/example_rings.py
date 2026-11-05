import json
base={'name':'Sample Gymnastics Club','suburb':'Hamilton','headline':'Learn to fly.','sub':'Recreational and competitive gymnastics for all ages.','cta_label':'Ask about classes','cta_url':'mailto:hello@example.com','words':['Gymnastics','Ages 3+','Adults','Rings','Competitive'],'serv_title':'What we teach','services':[{'title':'Recreational','desc':'Fun first.'},{'title':'Competitive','desc':'Train to compete.'},{'title':'Adults','desc':'Start at any age.'}],'address':'Hamilton','phone':'','email':'hello@example.com','close':'Come and tumble','close_sub':'Message the club.','facts':[['Where','Hamilton'],['Ages','3 to adult'],['Levels','All']],'card':['All ages','Flip, swing,<br>balance.'],'band':['For adults too','All levels.'],'kind':'rings','font':'bsd'}
out=[]
for slug,pre,lay in [('rings-a','navy-sky','a'),('rings-c','cream-red','c')]:
    d=dict(base);d.update(slug=slug,preset=pre,layout=lay);out.append(d)
json.dump(out,open('cfg.json','w'))
