#         try
#           │
#      ┌────┴─────┐
#      │          │
#  No Error     Error
#      │          │
#      ▼          ▼
#    else      except
#       \        /
#        \      /
#         ▼    ▼
#       finally


try:
    num=int(input("Enter Number:"))

except ValueError:
    print("Invalid Input")

else: 
    print("Square= ",num*num)
finally:
    print("Execution Completed")