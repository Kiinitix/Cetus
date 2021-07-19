# Cetus
> Inspired by: https://www.ijser.org/researchpaper/Secured-Communication-through-Fibonacci-Numbers-and-Unicode-Symbols.pdf

In the proposed method, the original message called plain text 
is  converted  into  cipher  text  with  the  help  of  Fibonacci num-
bers  generated.  Here,  each  character  is  extracted  from  the 
original  message  and  is  replaced  with  another  character,  the 
way  the  character  is  chosen  to  replace  the  original  character 
makes  this  method  unique  and  different  when  compared  to 
the traditional methods. The obtained cipher text is converted 
into  Unicode  symbols,  and  these  symbols  in  a  text  file  are 
transmitted  to  the  recipient  through  an  unsecured  communi-
cation channel. Since the message is encrypted in two levels, it 
is hidden from others and makes the decryption process more 
difficult for any intruders.  The conversion of plain text to Un-
icode symbols undergoes two phases namely; converting plain 
text to cipher text and converting cipher text  to Unicode sym-
bols. 


The  character  set  follows  a  round-robin  method  and  the  cha-
racter which falls below the Fibonacci number will be taken as 
the  character  in  the cipher  text.  If  there  are  a  number  of  cha-
racters  in  the  plain  text,  the  process  of  finding  the  replacing 
character  with  the  Fibonacci  number  might  be  difficult  be-
cause  each  time  the  size  of  the  Fibonacci  number  is  increased 
by  adding  the  previous  two  numbers.  If  the  application  does 
not  support  the  size  of  the  Fibonacci  number,  after  a  fixed 
range,  Fibonacci  number  can  be  restarted  from  the  begin-
ning.  Since the selection of the character depends on the Fibo-
nacci  number,  it  provides  more  security  for  the  system,  and 
any unknown person cannot decode the message easily.
In the second level of security, the ASCII code of each charac-
ter  obtained  from  the  cipher  text  plus  the  ASCII  code  of  its 
previous  character,  and  next  character  is  added  to  the  ASCII 
code of the equivalent character in the original message.  Here, 
ASCII  codes  of  four  characters  are  used  as  a  security  key  to 
further  encode  the  characters  available  in  the  cipher  text  to 
Unicode symbols.

## Steps involved in Encryption  
    1. A sender wants to send a Hello message to a recipient.
    2. The  original  message,  also  called  plaintext,  is  converted  to cipher  text  by  using  a  key  and  Fibonacci  numbers.  The  algorithm  being  used  can  produce  a  different  output  each time it is used, based on the key selected. 
    3. Cipher Text is converted into Unicode symbols using another key and saved in a text file.
    4. The text file is transmitted over the transmission medium.

## Steps involved in decryption
    1. At  the  recipient  end,  Unicode  symbols  are  converted  to hexadecimal values and then to equivalent decimal values using  the  same  algorithm  and  key  that  were  used  to  encrypt the message.
    2.  Perform subtraction with the decimal values and the ASCII code of characters from cipher text.
    3. The remainder after subtraction gives the ASCII code of the character in need.
    4. The process is repeated for the number of characters in the cipher  text  and  accumulated  characters  forms  the  original plain text.
