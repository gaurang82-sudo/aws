import heart_bit
import time 
def vcdtocsv():
    print('vcd to csv...')
    time.sleep(2)

def model_gen():
    print('model is traing')
    time.sleep(2)


def main():
    vcdtocsv()
    heart_bit.send_heartbit()
    model_gen()
    heart_bit.send_heartbit()

if __name__== '__main__':
    if heart_bit.send_heartbit():
        main()
    else:
       if heart_bit.login():
           main()
       else:
           print('wrong password ......')
   
