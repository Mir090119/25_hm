# def daraja(a):
#     if a==0:
#         return 1
#     return 2*daraja(a-1)
# print(daraja(0))

# def daraja(a):
#     if a==1:
#         return 1
#     return a**2+daraja(a-1)
# print(daraja(8))


# def fakh(n, k):
#     if k==0 or k==n:
#         return 1
#     return fakh(n-1,k-1)
# print(fakh(2,1))


# def fakh(a,n):
#     if n==0:
#         return 1
#     return a**n+fakh(a,n-1)
# print(fakh(2,2))


# def sum(n):
#     if n==0:
#         return 1
#     return 2**n+sum(n-1)
# print(sum(4))


# def r(a,n):
#     if n==0:
#         return 1
#     return a*r(a,n-1)
# print(r(3,2))