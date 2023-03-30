guests =['Trump','Messi','ronaldo','alex']
print(f"Welcome to the Diner {guests[0]}")
print(f"Welcome to the Diner {guests[1]}")
print(f"Welcome to the Diner {guests[2]}")
print(f"Welcome to the Diner {guests[3]}")
guests_not_coming=[]
guests_not_coming.append(guests[0])
guests[0] = "M.Sharapova"
print(guests_not_coming)
print(f"{guests[3].title()}  sorry to hear, please come next time ")