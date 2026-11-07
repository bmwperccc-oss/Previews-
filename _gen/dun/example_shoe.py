import json
base={'slug':'sample-shoe','name':'Sample Ballet','suburb':'Dunedin','kind':'shoe','preset':'blush-pink','font':'bsd','layout':'a','headline':'Dance on your toes.','sub':'Ballet for every age.','cta_label':'Book a trial','cta_url':'mailto:hello@example.com','words':['Ballet','Jazz','Contemporary','Hip hop','Acro'],'serv_title':'Classes','services':[{'title':'Ballet','desc':'Technique.'},{'title':'Jazz','desc':'Energy.'},{'title':'Acro','desc':'Strength.'}],'address':'Dunedin','phone':'','email':'hello@example.com','close':'Join us','close_sub':'Message to book.','steps':[['Hello','Message us.'],['Trial','Try a class.'],['Dance','Join in.']],'facts':[['Where','Dunedin'],['Open','Mon-Sat'],['Ages','3+']],'card':['Trial class','Come and dance.'],'band':['New students welcome','Say hello.'],'scene':{'kind':'shoe'}}
out=[]
for l,p in (('a','black-gold'),('c','blush-pink')):
    d=dict(base);d['slug']='sample-shoe-'+l;d['layout']=l;d['preset']=p;out.append(d)
json.dump(out,open('cfg.json','w'))
