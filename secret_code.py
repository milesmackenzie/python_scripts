def maskify(cc):
  if len(cc) < 4:
    return cc
  return "#" * (len(cc)-4) + cc[-4:]




n = "453678430293834764647564848rhdhfbfhrw7474768wyr"
print maskify(n)
