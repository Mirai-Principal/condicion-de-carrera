from concurrent.futures import ThreadPoolExecutor

saldo = 100

def retirar(cantidad):
    global saldo
    if saldo >= cantidad:
        saldo -= cantidad
        print("Retiro aprobado:", saldo)
    else:
        print("Saldo insuficiente")

with ThreadPoolExecutor(max_workers=2) as executor:
    executor.submit(retirar, 80)
    executor.submit(retirar, 80)

print("Saldo final:", saldo)


#forma 2 bloqua el hilo hasta q termine
print("forma 2")
import threading

saldo = 100
lock = threading.Lock()

def retirar(cantidad):
    global saldo

    with lock:
        if saldo >= cantidad:
            saldo -= cantidad
            print("Retiro aprobado:", saldo)
        else:
            print("Saldo insuficiente")

hilo1 = threading.Thread(target=retirar, args=(80,))
hilo2 = threading.Thread(target=retirar, args=(80,))

hilo1.start()
hilo2.start()

hilo1.join()
hilo2.join()

print("Saldo final:", saldo)



# con for update bloquea el registro
# BEGIN;

# SELECT saldo
# FROM cuentas
# WHERE id = 1
# FOR UPDATE;

# -- Validar el saldo y actualizarlo
# UPDATE cuentas
# SET saldo = saldo - 80
# WHERE id = 1 AND saldo >= 80;

# COMMIT;

# operacion atomica - update con where del saldo
# UPDATE cuentas
# SET saldo = saldo - 80
# WHERE id = 1
#   AND saldo >= 80;