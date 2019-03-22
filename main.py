import disk.df as df
import disk.find as find
import disk.rm as rm
import time
import subprocess

cond = True
while cond:
    x = df.get_data("ext4")
    for aux in x:
        aux.print_df()
        aux.is_inside_limit(90)
#    time.sleep(5)
    cond = False
rm.all_but("/")
#print(find.get_data("/var/lib/mysql", 5))
    


#for aux in l:
#    mopa = str(aux, 'utf-8')
#    mopa = " ".join(mopa.split())
#    print(mopa.split(" ")[0])
    
p1 = subprocess.Popen(["find", "/var", "-type", "f", "-printf", "'%s %p\n'"], stdout=subprocess.PIPE)
p2 = subprocess.Popen(["sort", "-nr"], stdin=p1.stdout, stdout=subprocess.PIPE)
p3 = subprocess.Popen(["head", "-5"], stdin=p2.stdout, stdout=subprocess.PIPE)
p1.stdout.close()
p2.stdout.close()
output,err = p3.communicate()

l = output.splitlines()
for aux in l:
    print(aux)
