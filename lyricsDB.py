import numpy as np

mundo = [
    """
    Sa'n darating ang mga salita
    Na nanggagaling sa aming dalawa?
    """,
    """
    Kung lumisan ka, 'wag naman sana
    Ika'y kumapit na, nang 'di makawala
    """,
    """
    Aking sinta, ikaw na ang tahanan at mundo
    Sa pagbalik, mananatili na sa piling mo
    Mundo'y magiging ikaw
    """,
    """
    'Wag mag-alala kung nahihirapan ka
    Halika na, sumama ka
    Pagmasdan ang mga tala
    """,
    """
    Aking sinta, ikaw na ang tahanan at mundo
    Sa pagbalik, mananatili na sa piling mo
    Mundo'y magiging ikaw
    """,
    """
    Limutin na ang mundo
    Nang magkasama tayo
    Sunod sa bawat galaw
    Hindi na maliligaw
    """
    
]


come_inside_of_my_heart = [
    """
    I love you
    But I don't really show you
    """,
    """
    I'd call you
    But only if you want me too
    """,
    """
    Oh, don't you let it stop
    Oh, I won't let it happen, baby
    I will never stop
    But only if you listen to me
    """,
    """
    Come inside of my heart
    If you're looking for answers
    Look at the stars
    Go a little bit faster
    Ooh, ooh
    """,
    """
    Oh, baby
    Forgive me if I hurt you
    """,
    """
    Come save me
    'Cause you're the only one for me
    """,
    """
    Whatever happens to me, baby
    I'm sorry
    No one could ever go my way
    """
]

hey_barbara = [
    """
    Hey, Barbara!
    Maybe I can get you some wine
    """,
    """
    My Sylvia!
    How can I say that you are mine?
    """,
    """
    Hey, Beverly!
    Eyes are blue from what I can see
    """,
    """
    Hey, Stephanie!
    So you wanna dance with me?
    """,
    """
    I don't care
    What they say
    I'm just trying to be one of the boys
    """,
    """
    So you can't
    Change your mind
    You can never stand alone in the dark oh, baby, so
    Dance now!
    Dance now, baby!
    Give it all and I'm gonna start
    """,
    """
    Olivia!
    Tell me if you are satisfied
    """,
    """
    My dear Sandra!
    Someday, you'll be a superstar
    """,
    """
    Hey, my Ramona!
    Eyes are blue from what I can see
    """,
    """
    Hey, Margarita!
    So, you wanna dance with me?
    """
]

dulo_ng_hangganan = [
    """
    Dumating ka na sa dulo ng hangganan
    Sumisigaw, nag-iisa
    """,
    """
    Sumabay ang luha sa indak ng alon
    Umiiyak, nag-iisa
    """,
    """
    Binibigkas habang tumatakbo
    Pumipiglas sa mga yakap ko
    """,
    """
    Pag-ibig ko, bakit lumalayo?
    Pag-ibig mo, tila naglalaho?
    """,
    """
    Kapag makapiling ka
    Hindi alam ang gagawin, iiwas ba o titingin
    """,
    """
    Sa 'yong kagandahan?
    Ang kislap ng iyong mata ay 'di ko na nakikita
    """,
    """
    Umuwi sa ating sinimulang tahanan
    Ngunit ngayon, wala ka na
    """,
    """
    Hindi ko sukat akalain, pag-ibig mo'y nagbago
    Ang nais ko, pag-ibig mo
    """
]

ilaw_sa_daan = [
    """
    Mga ilaw sa daan, nakikisabay sa liwanag ng buwan
    """,
    """
    Habang ako'y nakatingin sa kawalan nang hindi mo pansin
    """,
    """
    Mga taong nalampasan ng apat na gulong na akin ngang sinasakyan
    Sa inipong usok ay bitin na nakaipit sa gitna at pang-bituin
    """,
    """
    Tuloy-tuloy sa pagtakbo
    Biglaang hihinto sa dulo
    """,
    """
    Kung makikita mo naman, lahat sila ay nagkakaisa
    """,
    """
    Tumatalon, sumisigaw, humihiyaw ang iba sa kanila
    """,
    """
    Hindi mo na mapipigilan ang saya, damdamin mo ay umaapaw
    """,
    """
    Sulitin mo ang buong gabi bago pa sumapit ang araw
    """,
    """
    Mga tao sa daan, sila'y sabay-sabay sa paggawa ng paraan
    Upang lapitan ang lasing na unti-unting umiikot ang paningin
    """
]

bata_dahan_dahan = [
    """
    Bata, dahan-dahan sa mundong kinagagalawan
    """,
    """
    Pagmasdan ang larawan ng hitsurang nagmamalakas
    """,
    """
    'Di pwedeng mabulag, makinig sa tamang tinig
    """,
    """
    Wala kang mapapala sa taong walang kahulugan
    """,
    """
    'Wag hahayaang magaya sa iba, Kawalang-sala
    """,
    """
    Halika na't tuklasin ang mundong puno ng isip-hangin
    """,
    """
    Bata, napa'no ka? Duguan, luhaan, nasaktan
    Sugatan ang kamay, 'di alam ang gagawin
    """,
    """
    Pwede bang magpalaya ka ng mga takot sa iyong isip
    Na pilit dinidikit ng kamatayan? Oh, 'di ka nag-iisa
    """,
    """
    Sa munting palaruan, ang bata ay tumatanda
    Nadadapa, nangangapa, nananatiling mag-isa
    """,
    """
    Ang iyong tanging panalangin, 'di mawawala
    """
]

bawat_kaluluwa = [
    """
    'Wag tahaking mag-isa
    """,
    """
    Bulong mula ulo hanggang paa
    """,
    """
    Ang araw ay mag-aantay sa sinag ng buwan
    """,
    """
    'Wag hayaan ang paa
    """,
    """
    Pinosas ang kamay ng bata
    Upang ito'y maging isang sunod-sunuran
    """,
    """
    Akin ngang inaasahang
    Hindi mawawala ang kawalan sa iyong kaluluwa
    """,
    """
    Wala ka nang magagawa
    Patuloy mong sisirain
    """,
    """
    Basahin bawat kaluluwa
    Bangungot ng panaginip ang magpapagising
    """,
    """
    Ang pag-asang nawala
    Pilit kong balikan ang nakaraan
    """,
    """
    Subukan mo lang, subukan mo lang at makakaya mo
    At baka sakaling matanaw ang nawala
    """,
    """
    Isara ang kamay sa mga gabay ng mga anino
    Langit at luha, aking pinapasan
    """,
    """
    Subukan mo lang, subukan mo lang at makikita mo
    Subukan mo lang, subukan mo kung makakalaya ang...
    """
]

in_my_prison = [
    """
    Help me
    Something is a misery
    """,
    """
    Save me
    Somebody wants to take me
    """,
    """
    Kill me
    So I have a reason to live
    """,
    """
    Take me
    So I have a reason to give
    """,
    """
    I'm in my prison
    And I am the only prey
    """,
    """
    You are the reason
    Why my heart and soul would stay
    """,
    """
    La, la, la, la, la
    La, la, la, la
    """,
    """
    I'm in the middle of the night
    I won't forget it on my mind
    I can't remember
    """,
    """
    I'm in the middle of the night
    I won't be coming home tonight, oh!
    """,
    """
    Faster
    Cars are slowly moving
    """,
    """
    Shining
    Like a dream that we are facing
    """
]

where_have_you_been_my_disco = [
    """
    Your momma said that you should be home
    Seven in the evening with a sober soul
    """,
    """
    Don't you worry, brother, I am on my way
    Just keep on trucking tonight
    """,
    """
    Children of the future, let me tell you something
    Boogie is my life that I've never shown it
    """,
    """
    Why have you forsaken all the things we know?
    """,
    """
    I wanna show it tonight
    """,
    """
    They don't need no disco, no disco
    Where have you been, my disco, my disco?
    """,
    """
    Take me back to disco, to disco
    Groove it up, groove it up
    """,
    """
    Darling, it's coming back, loving you
    Revive the old, make it new
    """,
    """
    Come on, it's going down, make it true
    Celebrate, celebrate
    """,
    """
    Your momma said that you should be gone
    Don't you dare to come back with a pretty bad face
    """,
    """
    Take it easy, brother, I am here to stay
    """,
    """
    Just keep on dancing 'til the girls are gone
    """,
    """
    Children of the future, let me tell you something
    Boogie is my life since when I was young
    """,
    """
    I've been livin' heaven, leaving all the pain
    """
]

i_aint_perfect = [
    """
    There you are beautiful, quietly
    Sleepin' on the bed we made right next to me
    """,
    """
    Feels like a dream
    Only a dream
    """,
    """
    Here we are holding on, dangerously
    Dancin' on the edge of the infinity
    """,
    """
    Writing all these memories
    """,
    """
    Singing all these melodies
    """,
    """
    Waiting here for centuries
    """,
    """
    I ain't perfect
    Perfect for you
    """,
    """
    Here I am beautiful, as you see
    Standing on the pedestal you made for me
    """,
    """
    Waltzin' through our symphonies
    """,
    """
    In our little galaxy
    """,
    """
    Waiting for our destiny
    """
]

take_that_man = [
    """
    Living in a world
    With nobody else
    """,
    """
    Every time we talk
    They'll give us a stare
    """,
    """
    Conspiracy, no privacy?
    Blame on me, instead of pointing out somebody
    """,
    """
    Take that man, I can let you go and do it
    Oh, take that man, I can let you go and do it
    """,
    """
    Free me from my mind
    From words I cannot find
    """,
    """
    Imagine you and me
    Escape reality
    """,
    """
    Unnatural, so fictional
    Blame on me, instead of pointing out somebody
    """
]

sariling_multo = [
    """
    Sa panaginip ko, ikaw ang nakakasama
    """,
    """
    Sa bawat agos ng salita
    Dala ang damdamin kong sawa
    """,
    """
    Pikit-matang titingin sa patay na bituin
    """,
    """
    Sana pigilan sandali ang sandali
    Upang takasan lahat ng takot ko
    """,
    """
    Sa araw-araw ko, ikaw ang nakakausap
    """,
    """
    Ang luha kong nag-aabang
    Laman ang tinagong kalungkutan
    """,
    """
    Pikit-matang dadal'hin, kapayapaan hihingin
    """,
    """
    Paano ba pigilan ang ikot ng mundo?
    """,
    """
    Sa awiting 'to, may magtataka
    Kung magbago man ako, huwag sanang umalis
    """,
    """
    Panalangin ko, iwanan ninyo ako
    """,
    """
    Dapat bang matakot sa sariling multo?
    """,
    """
    Sa araw-araw ko, ikaw ang nakakalaban
    """,
    """
    Ano man dakong puntahan
    Sabay tayong mahihirapan
    """,
    """
    Huwag ka sanang bumitaw
    Bantayan bawat galaw
    """,
    """
    Nang hindi magtampisaw sa lungkot at luha ng ulan
    """
]

captivated = [
    """
    You're the one that I want to be with
    Never wanna be separated
    """,
    """
    I'm captivated
    """,
    """
    Everyone says you're complicated
    """,
    """
    Every day, you're my most awaited, oh
    """,
    """
    Oh, they don't see you as I do
    You are so beautiful
    """,
    """
    Come breathe within my soul
    """,
    """
    Oh, my love
    You don't have to listen to a word they say
    """,
    """
    'Cause all that really matters is that I love you
    I really do
    """,
    """
    Oh, I need you and I really hate it
    """,
    """
    But I'll never get tired of waiting
    """
] 

ang_pinagmulan = [
    """
    Sa 'yong pagtingin, ang tanging hiling
    """,
    """
    'Di ko man alam ang rason at dahilan
    Ako'y kasama mo, kasama mo hanggang sa dulo
    """,
    """
    Itago man lahat, hindi maiiwasan
    Ang pagsabog ng pangkat, gigising ang katotohanan
    """,
    """
    'Di mo ba alam ang pinagmulan?
    Kamatayan man ang makalaban?
    """,
    """
    Sa 'yong pagtingin, ang tanging hiling
    Sagipin mo 'ko, nalulunod na ako
    """,
    """
    'Di mo ba alam, dagat man ng kamatayan
    Tumangay sa 'yo, mabibigla ka sa paglunod
    """,
    """
    Itago man lahat, kasama mo 'ko sa pag-ahon
    Ako'y naririto, ngayong nalilito
    """,
    """
    'Di ko rin alam kung sa'n patungo ang dahilan ng alon
    Hahayaan na lang sa kamay ng panahon
    """
]

my_juliana = [
    """
    My Juliana, I promise that I'll never come back
    """,
    """
    When the sky hides the sun
    You'll never see my heart on a string
    With your broken ring
    """,
    """
    I'm sitting on the corner
    Waiting to discover
    """,
    """
    If your eyes would see my broken heart
    """,
    """
    My self-esteem is fading
    """,
    """
    Mind and soul forsaking
    """,
    """
    All the darkness that invades within
    """,
    """
    I, I don't believe
    What everybody tells me what I'm supposed to be
    """,
    """
    I, I just can't see
    The reason why you should be lying next to me
    """,
    """
    Call me when it's over
    Deal with this together
    """,
    """
    Teach me how to mend a broken heart
    """,
    """
    Be with me forever
    In this stormy weather
    """,
    """
    Tell me and I'll wish upon a star
    """
]

im_a_butterfly = [
    """
    Daylight has come to an end
    The sun sleeps for the moon
    """,
    """
    Night sky has remained unchanged
    The rain speaks for the clouds
    """,
    """
    Extemporizing, imperatively
    The mourning would weep for herself
    """,
    """
    Melody has become unsung
    Swaying towards your fervent lips
    """,
    """
    I am a butterfly
    Who doesn't even know where else to fly
    """,
    """
    Lost and broken
    I don't know why
    """,
    """
    I've never looked at me this way before
    """,
    """
    Don't believe in everything you see
    """,
    """
    Listen to the butterfly
    As he escape his homemade cage
    """,
    """
    Don't hide in the dark shadows
    For you can't run from your other face
    """,
    """
    Don't be discouraged if the
    Darkness tries to fool you
    """,
    """
    Save your own protection
    To preserve your imperfection, darling
    """,
    """
    I know something
    That you don't know
    """,
    """
    You know something
    That everybody knows
    """
]

kung_ayaw_mo_huwag_mo = [
    """
    Hari ng dedmahan ang teleponong
    Apat na magdamag nang 'di umiimik
    """,
    """
    Kung 'di ka tatawagan, may pag-asa kayang
    Maisip mo ako't biglang ma-miss?
    """,
    """
    Hindi kita mapipilit kung ayaw mo
    """,
    """
    'Wag mo akong isipin, bahala na
    """,
    """
    Hindi kita mapipigil kung balak mong
    Ako'y iwanang nag-iisa
    """,
    """
    P'wes walkathon ako patungo riyan
    Isosoli ko lang lahat ng mga sulat mo
    """,
    """
    At me-katok pa yata'ng doorbell n'yo
    Magtatatlong oras na 'ko dito
    """
]

sweet_shadow = [
    """
    I want you to set me free
    From this place, I don't belong
    """,
    """
    Now that you're older
    The world tells you to be stronger
    """,
    """
    If you want to get better
    You have to get that friend beside ya
    """,
    """
    Now that you're older
    The world tells you to grow faster
    """,
    """
    If you want to get better
    The shadows will still run after ya
    """,
    """
    Ooh, sweet shadow
    My mind is giving up again
    """,
    """
    Ooh, sweet shadow
    'Cause I don't want you to become like that
    Oh, I don't want to become like that
    """,
    """
    I want you to set me free
    From this place, I don't belong
    """,
    """
    I don't want here to stay any longer
    Everything feels so wrong
    """
]

i_would_rather_live_alone = [
    """
    I would rather live alone without you
    """,
    """
    You saved all my raging thoughts
    But you torn my heart, I didn't ask for this
    """,
    """
    You're my favorite pain that could make me feel again
    """,
    """
    I can feel over my skin the whisper
    Of your loving scars within
    """,
    """
    But you ripped my heart, I always wanted this
    """,
    """
    But you always had my heart
    And I just don't want to be part of your life
    """,
    """
    I'll never be the same
    I'm not who I'm today
    """,
    """
    So, please just break my heart, don't break my heart
    """,
    """
    I have no chance to, Be someone you'll hold on to
    """,
    """
    My veins are failing
    My mind is degrading
    """,
    """
    'Cause my soul is fading to the sea
    """,
    """
    'Cause maybe I'm not who I'm today
    """,
    """
    I would rather live alone
    I would rather live alone
    I can't do this all alone
    """
]

not_my_energy = [
    """
    I've ran out of reasons
    Reasons to comfort my mind
    """,
    """
    Illusions, delusions
    Confusions are running inside
    """,
    """
    Pale lips and dark lies has conquered the dreamer's eyes
    """,
    """
    'Cause there is something in those eyes I can never find, boy
    """,
    """
    I'm sick and tired of the noises, the voices
    """,
    """
    Everything seems magical
    """,
    """
    And yes, my mind is awakened, dead conscience
    Everyday's a torture for me
    """,
    """
    No, I am not holding on to the darkness
    """,
    """
    'Cause you're already in my mind
    """,
    """
    And if you would walk alone, then just do it
    """,
    """
    The clock is ticking backwards
    """,
    """
    I ain't got it all, I don't care
    You're not my energy
    """,
    """
    Your tears are in laughter
    While your smile is in despair
    """,
    """
    The poison of your tongue
    Has killed all your truthful words
    """,
    """
    My eyes are hiding the pavements of my vacancy
    You can't take the power from me
    """
]

nagbabalik = [
    """
    Hindi ko malimutan
    Hindi ko maintindihan
    """,
    """
    Ano ang naisipan?
    Tinapon na nakaraan
    """,
    """
    Nagbabalik, nagbabalik
    Ang puso ko, muling iyo
    """,
    """
    Oh, bakit ang kulit ko?
    Akala ko ba'y ayaw na?
    """,
    """
    Ngunit 'sang kalabit mo
    Ako'y nagkakandarapa
    """,
    """
    Pinilit ko na isara
    Pintong ito't limutin ka
    """,
    """
    Akala ko, hindi ko na
    Mahahanap ang nawala
    """ 
]

sentimental = [
    """
    We won't segregate our thoughts
    This will not be settled
    Ears closed to the lips of yours
    """,
    """
    Never giving it up on you
    Never changing it up for you
    """,
    """
    Never ever gonna lose ourselves
    To the man who's sitting on a chair
    """,
    """
    Maybe we should try someone new
    So we could play our own game fair
    """,
    """
    Ohh, ohh, so sentimental
    They hate this awful face
    Gonna cause shit in this place, oh baby
    """
    """
    They won't comprehend our mind
    Though it's not a battle
    """
]

songs = [mundo, come_inside_of_my_heart, hey_barbara, dulo_ng_hangganan, ilaw_sa_daan, bata_dahan_dahan, bawat_kaluluwa, in_my_prison, where_have_you_been_my_disco, i_aint_perfect, take_that_man, sariling_multo, captivated, my_juliana, im_a_butterfly, kung_ayaw_mo_huwag_mo, sweet_shadow, i_would_rather_live_alone, not_my_energy, nagbabalik, sentimental]
allsongs = np.concatenate((songs))
