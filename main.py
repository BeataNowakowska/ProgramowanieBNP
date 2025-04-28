def figury():
  figura = input(
      "Jakiej figury pole chcesz policzyć? (koło, kwadrat, prostokąt, trójkąt): "
  ).strip().lower()

  if figura == "koło":
    r = float(input("Podaj promień: "))
    pole = 3.14159 * r * r
  elif figura == "kwadrat":
    a = float(input("Podaj długość boku: "))
    pole = a * a
  elif figura == "prostokąt":
    a = float(input("Podaj długość pierwszego boku: "))
    b = float(input("Podaj długość drugiego boku: "))
    pole = a * b
  elif figura == "trójkąt":
    a = float(input("Podaj długość podstawy: "))
    h = float(input("Podaj wysokość: "))
    pole = (a * h) / 2
  else:
    print("Nieznana figura.")
    return

  print(f"Pole {figura} wynosi {pole:.2f}")


if __name__ == "__main__":
  figury()
