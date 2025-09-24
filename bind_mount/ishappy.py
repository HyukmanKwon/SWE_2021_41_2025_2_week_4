def isHappy(n):
  list = []
  while n!=1:
    num=0
    for i in list:
     if n in list:
      return False
    list.append(n)
    while n>=1:
      num+=(n%10)*(n%10)
      n//=10
    n=num
  return True

if __name__ == "__main__":
  sample0_output = isHappy(19)
  sample1_output = isHappy(2)

  with open("/app/bind_mount/output.txt", "w") as f:
    f.write(f"19: {sample0_output}\n")
    f.write(f"2: {sample1_output}\n")

  print("Results saved to /app/bind_mount/output.txt")
