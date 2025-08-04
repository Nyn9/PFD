import time

t = time.time()
print(f"Seconds since January 1, 1970: {t} or {t:.2e} in scientific notation")
print(time.strftime("%b %d %Y", time.localtime(t)))
