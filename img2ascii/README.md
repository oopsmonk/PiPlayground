# Convert image to ASCII 

For help:  `img2ascii.py -h`  

### Scale image to 40 pixles

```
./img2ascii.py -s 40 ./raspberry-pi-logo2.png 

########################################
#####=-#....+.############.2....#'"#####
####.............;#####.............####
###,....&8........$###........1>....+###
####.......'#......##......#".......####
####>.........##...##-../#0......../####
#####/.........4########$..........#####
#######.........########.........#######
#########/,...(###########...!7#########
#################******#################
########*****##**********#*****-########
######>*****###**********##$*****#######
######***+#######******######;***,######
#####4*+####****0######*****,##&**######
##########********####********6#########
####*+###**********##**********/##*+####
###***##***********##***********#+***###
##****##**********&##&**********#+****##
##****##**********####1*********#$****##
##****###*******;#######*******###****##
##=**###########3******/##########<**###
###############**********######***######
#####*****####'***********###******#####
#####*******##+***********##*******#####
#####*******)##**********##********#####
######*******###********##(*******######
#######******######%.$####*******#######
#########-**8##############****#########
###############**********'##############
###############**********###############
#################******#################
########################################
```

### Change character of block color  

```
./img2ascii.py -b 8 -s 40 ./raspberry-pi-logo2.png  

8888888888888888888888888888888888888888
88888=-8....+.888888888888.2....8'"88888
8888.............;88888.............8888
888,....&8........$888........1>....+888
8888.......'8......88......8".......8888
8888>.........8#...88-../80......../8888
88888/.........488888888$..........88888
8888888.........88888888.........8888888
888888888/,...(88888888888...!7888888888
88888888888888888******88888888888888888
88888888*****88**********8*****-88888888
888888>*****888**********88$*****8888888
888888***+8888888******888888;***,888888
888884*+8888****0888888*****,88&**888888
8888888888********8888********6888888888
8888*+888**********88**********/88*+8888
888***88***********88***********8+***888
88****88**********&88&**********8+****88
88****88**********88881*********8$****88
88****888*******;8888888*******888****88
88=**888888888883******/8888888888<**888
888888888888888**********888888***888888
88888*****8888'***********888******88888
88888*******88+***********88*******88888
88888*******)88**********88********88888
888888*******888********88(*******888888
8888888******888888%.$8888*******8888888
888888888-**888888888888888****888888888
888888888888888**********'88888888888888
888888888888888**********888888888888888
88888888888888888******88888888888888888
8888888888888888888888888888888888888888
```

### Invert imamge and change ascii mapping  

```
./img2ascii.py -i -a raspberrypi -s 40 ./raspberry-pi-logo2.png
                                        
     ys bbbbrb            bybbbb ye     
    bbbbbbbbbbbbbp     bbbbbbbbbbbbb    
   sbbbbaebbbbbbbbi   bbbbbbbbabbbbbb   
    bbbbbbbr bbbbbb  bbbbbb rbbbbbbb    
    rbbbbbbbbb bbbb  ebbp sbbbbbbbbp    
     pbbbbbbbbbp        pbbbbbbbbbb     
       bbbbbbbbb        bbbbbbbbb       
         spbbbr           bbbre         
                 iiiiii                 
        iiiii  iiiiiiiiii iiiiia        
      riiiii   iiiiiiiiii  iiiiii       
      iiip       iiiiii      aiiiy      
     eip    iiiip      iiiiiy  pii      
          iiiiiiii    iiiiiiiir         
    ip   iiiiiiiiii  iiiiiiiiiis  ip    
   iii  iiiiiiiiiii  iiiiiiiiiii piii   
  iiii  iiiiiiiiiip  yiiiiiiiiii piiii  
  iiii  iiiiiiiiii    piiiiiiiii iiiii  
  iiii   iiiiiiia       iiiiiii   iiii  
  iii           riiiiiie          yii   
               iiiiiiiiii      iii      
     iiiii    iiiiiiiiiiii   iiiiii     
     iiiiiii  piiiiiiiiiii  iiiiiii     
     iiiiiiir  iiiiiiiiii  iiiiiiii     
      iiiiiii   iiiiiiii  aiiiiiii      
       iiiiii      api    iiiiiii       
         riib              iiii         
               iiiiiiiiiir              
               iiiiiiiiii               
                 iiiiii                 
                                        
```

### Rotate image and change ascii mapping  

```
./img2ascii.py -r 30 -i -a raspberry -s 40 ./raspberry-pi-logo2.png  

                  ssssbssssa            
                 ssss sssss             
                ssssessssss             
               sssssasssss              
               ssss sssss               
          a    sss sssss   p            
       esssss      ssp  rrrrrrp         
     ssssssssa        errrrrrrr         
   esssssssss                   rrrr    
  ssssssr        rrrrr    rrr   rrrrr   
psssrbasssss   rrrrrrr yrrrrrrr errrr   
ssssssssssss  brrrrrr rrrrrrrrr  rrrr   
sssssssssss   rrrrry rrrrrrrrrr   ers   
 sssssssss   rrrrr   rrrrrrrrrr         
 bassssaa ra rrb     rrrrrrrrrb  rrry   
        err     p    rrrrrrrr   rrrrr   
       rrr   rrrrrr   rrrrrb   arrrrr   
      rrrr  rrrrrrre           rrrrrr   
      rrr  rrrrrrrrr   rrrrr  srrrrrr   
      rrb rrrrrrrrr  srrrrrrr rrrrrr    
      rr  rrrrrrrrr rrrrrrrrr rrrrr     
      e   rrrrrrrr rrrrrrrrrr errr      
          rrrrrrr  rrrrrrrrr   a        
      rr  rrrrrr  rrrrrrrrr             
     errr   ry    arrrrrrr   rr         
     rrrr          rrrrrp arrrr         
     rrrr      r         rrrrr          
     rrrr  errrrrrr     rrrrrr          
       rr rrrrrrrrrr  errrrr            
          rrrrrrrrra  rrrrr             
           rrrrrrr                      
            resr                        
```

