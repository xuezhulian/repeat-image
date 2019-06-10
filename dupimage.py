import hashlib
import glob
import os
import sys

def repeat_image(path):
  repeatSize = 0
  repeatImage = {}
  hashimage = {}
  for line in os.popen("find %s -name \"*.png\"" % path).xreadlines():
    f = open(line.strip(),"r")
    imagedata = f.read()
    hashcode = hashlib.md5(png2.read()).hexdigest()
    # imagename = line.split("/")[-1].strip()
    if hashcode in hashimage:
      repeatSize = repeatSize + len(imagedata)
      repeatImage[line] = hashimage[hashcode]
    else:
      hashimage[hashcode] = line
  
  return repeatImage,repeatSize / 1024

if __name__ == "__main__":
  if len(sys.argv) != 2:
    print "please input file path"
    sys.exit(1)
  path = sys.argv[1]
  repeatImage,repeatSize = repeat_image(path)

  f = open("results.text","w")
  f.write("repeat image count: %d\n" % len(repeatImage))
  f.write( "repeat image size: %dKB\n" % repeatSize)
  for key in repeatImage:
    f.write("%s\n%s\n\n" %(key,repeatImage[key]))
  f.close()

