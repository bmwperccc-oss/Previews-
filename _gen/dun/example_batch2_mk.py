import json
def sv(*a): return [{'title':t,'desc':d} for t,d in a]
GS=[('Say hello','Send the team a message and say what you would like to try.'),('Come along','Book a first class or visit and meet the teachers.'),('Keep going','Settle into a weekly routine you enjoy.')]
L=[]
def A(**k): L.append(k)
A(slug='etk',name='Elite Thai Kickboxing',suburb='Penrose, Auckland',kind='bag',preset='violet-hot',font='anton',layout='c',
 headline='Train Thai boxing properly.',sub='Group classes for every level, kids from age 5, a women\'s self-defence class and King in the Ring fight nights in Penrose.',
 cta_label='Book a class',cta_url='mailto:info@etk.co.nz',words=['Thai boxing','Boxing','Kids classes','Women\'s class','Fight nights'],serv_title='On the mats',
 services=sv(('Group classes','Thai boxing sessions for all skill and fitness levels.'),('Boxing classes','Boxing-focused sessions to sharpen your hands.'),('Kids classes','Classes for children aged 5 and up.'),('Women\'s class','Self-defence, fitness and fun in a women-only room.'),('Wim Hof workshops','Ice baths and breathing techniques.'),('King in the Ring','Fight night events to watch or compete in.')),
 address='Penrose, Auckland',phone='09 589 4120',email='info@etk.co.nz',close='Step in',close_sub='Message the team to book your first class.',
 facts=[('Where','Penrose, Auckland'),('Kids','From age 5'),('Events','King in the Ring')],card=('Open to all','Beginners<br>welcome.'),band=('Fight night','King in the Ring brings the club together under the lights.'),
 scene=dict(bagTop='ETK',bagSub='THAI'))
A(slug='dunedinkickboxing',name='Dunedin Kickboxing',suburb='Dunedin',kind='core',preset='forest-lime',font='bsd',layout='b',
 headline='Kickboxing in Dunedin.',sub='Kickboxing and Muay Thai classes for every level, with a free first class and no joining fee.',
 cta_label='Book a free trial',cta_url='mailto:info@dunedinkickboxing.com',words=['Kickboxing','Muay Thai','Women\'s class','Sparring','Free trial'],serv_title='Class types',
 services=sv(('Fundamentals','Start from the beginning and build solid technique.'),('Skills','Sharpen combinations, defence and timing.'),('Women\'s only','A women-only kickboxing class.'),('Sparring','Controlled sparring for those ready for it.'),('Conditioning','Fitness work that carries into the ring.')),
 address='Dunedin',phone='027 359 1840',email='info@dunedinkickboxing.com',close='Throw the first one',close_sub='Your first class is free. Message the gym to book it.',
 facts=[('Free','First class'),('Adult membership','$28 per week'),('Casual class','$15')],card=('Simple pricing','No joining fee.<br>Ever.'),band=('Student rates','Students pay $25 a week for membership or $13 casual.'),
 scene=dict())
A(slug='qtgymnastics',name='Queenstown Gymnastics Club',suburb='Frankton, Queenstown',kind='rings',preset='navy-sky',font='bsd',layout='a',
 headline='Learn to fly in Queenstown.',sub='Recreational and competitive gymnastics for men and women, from age 3 through to adults, at Frankton.',
 cta_label='Ask about classes',cta_url='mailto:qtgymnastics@hotmail.co.nz',words=['Gymnastics','Ages 3 and up','Adults','Competitive','Recreational'],serv_title='What we teach',
 services=sv(('Recreational classes','Gymnastics for kids from age 3 and adults of every level.'),('Women\'s artistic','Vault, uneven bars, beam and floor.'),('Men\'s artistic','Strength, swing and control on the apparatus.'),('Adult classes','Start at any age, at any level.'),('Competitive squads','Training for gymnasts who want to compete.')),
 address='13 Red Oaks Drive, Frankton, Queenstown',phone='',email='qtgymnastics@hotmail.co.nz',close='Come and tumble',close_sub='Message the club to ask about the next class.',
 facts=[('Where','Frankton'),('Ages','3 to adult'),('Levels','Rec to competitive')],card=('All ages','Flip, swing,<br>balance.'),band=('For adults too','Adult classes run for all skill levels.'),steps=GS)
A(slug='gymkids',name='Gym Kids',suburb='Hobsonville, Auckland',kind='tramp',preset='cream-red',font='anton',layout='b',
 headline='Gymnastics for all.',sub='Preschool, freestyle and tumbling and trampoline programmes in Hobsonville, plus free-play sessions and holiday programmes.',
 cta_label='Join a session',cta_url='mailto:admin@gymkids.co.nz',words=['Preschool','Freestyle','Tumbling','Trampoline','Free-play'],serv_title='Programmes',
 services=sv(('Preschool gymnastics','A first step into movement for little ones.'),('Freestyle gymnastics','Build skills across the apparatus.'),('Tumbling and trampoline','Flips, rotations and big air, safely.'),('Free-play sessions','Mon, Wed and Fri 10:30am, Saturday afternoons and Sundays.'),('Holiday programmes','Active fun during the school breaks.'),('Birthday parties','Free-play sessions can be booked for parties.')),
 address='Unit 1, 4 Workspace Drive, Hobsonville, Auckland',phone='09 416 0003',email='admin@gymkids.co.nz',close='Come and play',close_sub='Message the team to book a free-play session.',
 facts=[('Where','Hobsonville'),('Free-play','Mon, Wed, Fri, Sat, Sun'),('Holidays','Programmes run')],card=('First visit?','Try a<br>free-play.'),band=('Uniform shop','Leotards, hoodies and drink bottles in the online store.'),steps=GS)
A(slug='dancemasters',name='Dance Masters International',suburb='Christchurch',kind='shoe',preset='black-gold',font='fraunces',layout='c',
 headline='Train with the masters.',sub='Workshops and coaching for Royal Academy of Dance students, with guest artists and scholarships.',
 cta_label='Enquire',cta_url='mailto:dancemasters.international@gmail.com',words=['Ballet','Contemporary','Jazz','Pointe','Character'],serv_title='The studio',
 services=sv(('Classical ballet','Technique built on the Royal Academy of Dance syllabus.'),('Contemporary','Floor work, release and flow.'),('Jazz','Sharp, rhythmic and expressive.'),('Pointe','Strength and artistry on pointe.'),('Character dance','Folk-inspired performance dance.'),('Guest artists','International tutors and scholarships.')),
 address='Christchurch (also Auckland)',phone='+64 22 670 2971',email='dancemasters.international@gmail.com',close='Take the floor',close_sub='Message the team about the next workshop.',
 facts=[('Syllabus','Royal Academy of Dance'),('Where','Christchurch'),('Awards','Scholarships')],card=('Workshops','Learn from<br>guest artists.'),band=('Scholarships','Workshop participants can win scholarships.'),steps=GS)
A(slug='convergencedance',name='Convergence Dance Studios',suburb='Christchurch and Rolleston',kind='ribbon',preset='violet-hot',font='bsd',layout='b',
 headline='Where styles converge.',sub='Ballet, contemporary, modern, jazz, musical theatre, tap and lyrical in Christchurch and Rolleston.',
 cta_label='Join a class',cta_url='mailto:cdancestudios@gmail.com',words=['Ballet','Contemporary','Jazz','Tap','Lyrical','Musical theatre'],serv_title='Styles',
 services=sv(('Ballet','Classical technique and grace.'),('Contemporary and modern','Movement with feeling.'),('Jazz','Energy, turns and attack.'),('Musical theatre','Sing, act and dance.'),('Tap','Rhythm you can hear.'),('Lyrical','Expressive, flowing movement.')),
 address='190 Montreal City Centre, Christchurch 8011',phone='+64 27 563 7471',email='cdancestudios@gmail.com',close='Find your style',close_sub='Message the studio to book a class.',
 facts=[('Styles','Seven'),('Where','Christchurch'),('Also','Rolleston')],card=('One studio','Seven ways<br>to dance.'),band=('Two locations','Classes run in Christchurch and Rolleston.'),steps=GS)
A(slug='jadondance',name='JaDon Dance',suburb='Christchurch',kind='mirrorball',preset='blush-pink',font='fraunces',layout='a',
 headline='Dance for everyone.',sub='Ballet, jazz, contemporary and hip hop for ages 4 and up, including adults, with performance opportunities.',
 cta_label='Ask about classes',cta_url='mailto:jacs2u@scorch.co.nz',words=['Ballet','Jazz','Contemporary','Hip hop','Adults welcome'],serv_title='Classes',
 services=sv(('Ballet','Gentle technique and grace.'),('Jazz','Big movement and energy.'),('Contemporary','Expressive and modern.'),('Hip hop','Groove, rhythm and confidence.'),('Performances','Show what you have learnt throughout the year.')),
 address='Harewood Playcentre, 719 Harewood Road, and St Aidans Church, Bryndwr',phone='+64 210 423 621',email='jacs2u@scorch.co.nz',close='Come and dance',close_sub='Message the studio to find a class for you.',
 facts=[('Ages','4 and up'),('Venues','Harewood, Bryndwr'),('Adults','Welcome')],card=('Every age','Step in<br>and move.'),band=('On stage','Performance opportunities run through the year.'),steps=GS)
A(slug='saraandersondance',name='Sara Anderson School of Dance',suburb='Christchurch',kind='ballerina',preset='sand-teal',font='fraunces',layout='b',
 headline='Ballet from the start.',sub='Preschool dance, graded ballet from age 5, adult ballet, contemporary and jazz, with an annual showcase.',
 cta_label='Ask about classes',cta_url='mailto:sadanceschool@gmail.com',words=['Preschool','Ballet','Adult ballet','Contemporary','Jazz'],serv_title='Classes',
 services=sv(('Preschool dance','A playful first taste of dance.'),('Ballet','Grade and vocational examinations from age 5.'),('Adult ballet','It is never too late to start.'),('Contemporary','Classes from age 9.'),('Jazz','Fun, sharp and rhythmic.'),('Annual showcase','Perform what you have learnt.')),
 address='Christchurch',phone='021 891 162',email='sadanceschool@gmail.com',close='Join the school',close_sub='Message Sara to ask about classes.',
 facts=[('Ballet from','Age 5'),('Exams','Graded and vocational'),('Show','Annual showcase')],card=('For all','Preschool<br>to adult.'),band=('Annual showcase','Every year the school performs on stage.'),steps=GS)
A(slug='yogaclubnz',name='Yoga Club',suburb='New Plymouth',kind='stones',preset='forest-lime',font='fraunces',layout='c',
 headline='Breathe in New Plymouth.',sub='Vinyasa, Hatha, Kundalini and Yin yoga for all levels, with private sessions, workshops and retreats.',
 cta_label='Book a class',cta_url='mailto:Yogaclubnz@gmail.com',words=['Vinyasa','Hatha','Kundalini','Yin','Meditation'],serv_title='Practices',
 services=sv(('Vinyasa','Flowing movement linked to breath.'),('Hatha','Slow, steady and grounded.'),('Kundalini','Breath, movement and sound.'),('Yin','Long, quiet holds to release.'),('Private sessions','One-on-one practice built around you.'),('Workshops and retreats','Go deeper with the community.')),
 address='35 Octavius Place, New Plymouth',phone='+64 27 759 2791',email='Yogaclubnz@gmail.com',close='Unroll a mat',close_sub='Message the studio. Mats, blocks and straps are supplied.',
 facts=[('Where','New Plymouth'),('Gear','Mats supplied'),('Levels','All welcome')],card=('Come as you are','Just bring<br>yourself.'),band=('Mindfulness','Meditation and mindfulness sit alongside the yoga.'),
 steps=[('Say hello','Message the studio and say what you are looking for.'),('Come to class','Everything you need is supplied.'),('Make it a habit','Find the practice that suits you.')])
A(slug='yogacentral',name='Yogacentral',suburb='Whangārei',kind='lotus',preset='ice-orange',font='fraunces',layout='b',
 headline='Yoga in the middle of Whangārei.',sub='Dynamic flow, gentle and restorative classes, meditation and mindfulness, with adapted teaching for injuries.',
 cta_label='Ask about classes',cta_url='mailto:info@yogacentral.co.nz',words=['Dynamic flow','Gentle','Restorative','Meditation','Workshops'],serv_title='Classes',
 services=sv(('Dynamic flow','Build heat and strength with breath.'),('Gentle and restorative','Slow down and recover.'),('Meditation and mindfulness','Quiet the noise.'),('Adapted teaching','Support for injuries and limitations.'),('Workshops','Philosophy, anatomy and advanced asana.')),
 address='69 Bank Street, Whangārei',phone='09 438 6887',email='info@yogacentral.co.nz',close='Find your centre',close_sub='Message the studio to book a class.',
 facts=[('Where','Bank Street'),('Props','Provided'),('Teaching','Adapted for injury')],card=('Gentle or strong','Pick the<br>pace.'),band=('Workshops','Go deeper into philosophy, anatomy and asana.'),
 steps=[('Say hello','Message the studio and mention any injuries.'),('Come along','Props are provided in the studio.'),('Keep practising','Build a practice that lasts.')])
json.dump(L,open('b2/cfg.json','w'))
