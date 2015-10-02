import sys, os.path, time

if len(sys.argv)>1:
  bashhisto = sys.argv[1]
else:
  bashhisto = "/" + os.getlogin() + "/.bash_history"

histofile = "/" + os.getlogin() + "/.zsh_history"
outputfile = open(histofile, "a")

i = 0
y=0

timestamp=eval("%s\n" %time.time())

if os.path.isfile(bashhisto):
  fobj = open(bashhisto)
  for line in fobj:
      ts = eval("%s\n" %time.time())
#       timestampw=': '+ str(eval('%s\n' %ts)) +":0;"
#       print (ts, timestampw)
#       break
          
      if ts == timestamp:
        i=i+1
        timestampw = ": " + str(ts) + ":" + str(i) +";"
        timestamp = ts
#         print(timestampw, timestamp, ts)
#         break
      
      else:
        i=0
        timestampw = ": " + str(ts) + ":0;"
        timestamp=eval("%s\n" %time.time())
        
      print( timestampw + line.rstrip())
      outputfile.write(timestampw + line.rstrip() + "\n")
      
      if y ==20:
        break
      else:
        y + 1 
  fobj.close()
  outputfile.close()
