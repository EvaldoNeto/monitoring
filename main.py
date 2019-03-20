import disk.df as df
import time
    
while True:
    x = df.get_data()
    for aux in x:
        #aux.print_df()
        aux.is_inside_limit(90)
        print(type(aux))
    time.sleep(5)
    


#for aux in l:
#    mopa = str(aux, 'utf-8')
#    mopa = " ".join(mopa.split())
#    print(mopa.split(" ")[0])
    
#p1 = subprocess.Popen(["find", "/home/biga/work/DAO/company", "-type", "f", "-printf", "'%s %p\n'"], stdout=subprocess.PIPE)
#p2 = subprocess.Popen(["sort", "-nr"], stdin=p1.stdout, stdout=subprocess.PIPE)
#p3 = subprocess.Popen(["head", "-3"], stdin=p2.stdout, stdout=subprocess.PIPE)
#p1.stdout.close()
#p2.stdout.close()
#output,err = p3.communicate()

#l = output.splitlines()
#for aux in l:
#    print(aux)
