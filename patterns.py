#time To pattern
# n=5
# for i in range(5):
#     for j in range(i+1):
#         print("*",end=" ")
#     print()
# * 
# * *
# * * *
# * * * *
# * * * * *

#2nd pattern
# n=5
# for i in range(n):
#     for j in range(i,n):
#         print("*",end=" ")
#     print()
# * * * * * 
# * * * *
# * * *
# * *
# *

# n=5  #this is also reverse of 2nd pattern just only add1 loop i+1 all code as it is 1st print blank
# for i in range(n):
#     for j in range(i,n):
#         print(" ",end=" ")
#     for i in range(i+1):
#         print("*",end=" ")
#     print()
#           * 
#         * *
#       * * *
#     * * * *
#   * * * * *

# n=5
# for i in range(n):
#     for j in range(i+1):
#         print("",end=" ")
#     for i in range(i,n):
#         print("*",end=" ")
#     print()
#     * * * * * * * * 
#   * * * * * * *
#    * * * * * *
#     * * * * *
#      * * * *
#       * * *
#        * *
#         *