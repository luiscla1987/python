def main():
    import matplotlib.pyplot as plt
    import numpy as np

    threads=[1,2,4,8]

    #Multiplicação de vetores com MPI
    tempo_t1=[2.271212,2.271212,2.161445,2.157448,2.157448,2.180102,2.190247,2.157761,2.163375,2.154493]
    tempo_t2=[1.881753,1.736321,1.724658,1.717946,1.714045,1.721976,1.845923,1.706485,1.720128,1.717000]
    tempo_t3=[1.891825,1.939822,1.858809,2.720530,2.805265,3.725934,2.043100,1.918950,1.902611,1.896425]
    tempo_t4=[3.646131,3.169339,4.542297,3.248911,3.597263,3.163422,3.762319,3.093562,3.228184,3.206059]
    
    media_t1=media(tempo_t1)
    
    

    Dynamicspeedups=[speedup(media_t1,media_t1), speedup(media_t1,media(tempo_t2)), speedup(media_t1,media(tempo_t3)),speedup(media_t1,media(tempo_t4))]
       
    plt.plot(threads, Dynamicspeedups,"bs")
    plt.plot(threads, Dynamicspeedups,"k:",color="blue",label="Parallel - Task")

    plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

    plt.title("Multiplicação de vetores com MPI")
    plt.ylabel('Speedup (s)')
    plt.xlabel('')
    plt.show()

def media(tempo):
    import numpy as np
    return(np.mean(tempo))

def speedup(media1,media):
    return(media1/media)

if __name__ == '__main__':
    main()

