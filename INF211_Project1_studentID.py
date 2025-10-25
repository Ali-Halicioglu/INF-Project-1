# ================================================================
# INF211 Project 1: 4-Band Resistor Decoder
# Student Name: Ahmed Ali Halıcıoğlu
# Student ID  : 250102002330
# ================================================================

tolerance_colors = ["BROWN", "RED", "GREEN", "BLUE", "VIOLET", "GREY", "GOLD", "SILVER"]
digit_colors = ["BLACK", "BROWN", "RED", "ORANGE", "YELLOW", "GREEN", "BLUE", "VIOLET", "GREY", "WHITE"]
valid_colors = ["BLACK", "BROWN", "RED", "ORANGE", "YELLOW","GREEN", "BLUE", "VIOLET", "GREY", "GRAY","WHITE", "GOLD", "SILVER"]
def is_upper_letter(ch):
   return 'A' <= ch <= 'Z' #ASCII tablosuna göre  A-Z arası büyük harf
def parse_four_bands(line):
    bands = ["","","",""]
    bandIndex = 0
    for i in range(0,len(line)):
        if(line[i] == "-"):
          bandIndex +=1 # - karakteri gelince bir sonraki indexi eklemek için bir arttırır
        else:
            bands[bandIndex] = bands[bandIndex] + line[i] # Bands arrayine eleman ekler
    return bands        

def color_to_value(color):
    
    for i in range(0,len(valid_colors)):
        if color == valid_colors[i] and i<=9:
            return i
        
      
def color_to_multiplier_and_tolerance(mult_color, tol_color):
    mult_coefficient = 0
    tolerance_rate= 0
    for i in range(0,len(valid_colors)): 
        if mult_color == valid_colors[i] and i<=9: #9. indexe kadar bir örüntü olduğu için kısaca döngüyle yaptım
            mult_coefficient = i
            break
    if mult_color == "SILVER":
        mult_coefficient = -2
        
    elif mult_color == "GOLD":
        mult_coefficient = -1   
    
    tol_values = [1.0, 2.0, 0.5, 0.25, 0.1, 0.05, 5.0, 10.0]  
    for i in range(0,len(tolerance_colors)):
        if tol_color == tolerance_colors[i]:
            tolerance_rate = tol_values[i]
    return mult_coefficient,tolerance_rate


def compute_resistor_value(d1, d2, exp, tol):
    value = (10 * d1 + d2) * (10 ** exp)

    ratio = tol / 100.0

    min_val = value * (1 - ratio)
    max_val = value * (1 + ratio)

    print("Value:", format(value, ".2f"), "Ω")
    print("Tolerance: ±" + format(tol, ".2f") + "%")
    print("Min:", format(min_val, ".2f"), "Ω")
    print("Max:", format(max_val, ".2f"), "Ω")

    
def main():
    # TODO: parse and map colors, compute values, then print exactly:
    # Value: <R> Ω
    # Tolerance: ±<tol>%
    # Min: <Rmin> Ω
    # Max: <Rmax> Ω
   line = input("Enter 4-band resistor code (e.g. YELLOW-VIOLET-RED-GOLD): ")
   bands = parse_four_bands(line)
   for ch in line:
      if ch != '-' and not is_upper_letter(ch):
         print("Invalid input! Please use uppercase letters (A–Z).")
         return
   bands = parse_four_bands(line)
   for i in bands:
       if i not in valid_colors:
           print("Invalid Color")
           return
   if bands[0] in ["BLACK","GOLD","SILVER"]:
       print("INVALID DIGIT1")
       return
   elif bands[1] in ["GOLD","SILVER"]:
       print("INVALID DIGIT")
       return
   elif bands[3] not in tolerance_colors:
       print("Invalid Tolerance")
       return
   elif bands[0] in ["GOLD","SILVER"]:
       print("WRONG ORDER, TURN THE RESISTOR AROUND")
       return
   elif len(bands) != 4:
       print("Empty or out of range index")
       return
   compute_resistor_value(color_to_value(bands[0]), color_to_value(bands[1]), color_to_multiplier_and_tolerance(bands[2],bands[3])[0], color_to_multiplier_and_tolerance(bands[2],bands[3])[1])

main()
