import streamlit as st
import os
<<<<<<< HEAD
import webbrowser
=======
import imgkit
>>>>>>> origin/main
from decimal import *



# This software is exclusively for use by VILLAVICIOSA ENERGIA, CIF:B74215435
# Unauthorized use of this software is strictly prohibited.

LEGAL_TEXT = "Este software es de uso exclusivo de VILLAVICIOSA ENERGIA con CIF: B74215435. El uso no autorizado de este software queda terminantemente prohibido."
BUTTON_TEXT = "General Cartel"

DISCOUNT_STAR_GOW = Decimal('0.05')
DISCOUNT_OPTIMA_GOW = Decimal('0.05')

DISCOUNT_STAR_WIZINK = Decimal('0.07')
DISCOUNT_OPTIMA_WIZINK = Decimal('0.08')

DISCOUNT_STAR_GOW_WIZINK = Decimal('0.05')
DISCOUNT_OPTIMA_GOW_WIZINK = Decimal('0.05')

png_path = "./Cepsa_Logo.png"
pdf_path = "./precios_carburantes.pdf"

# Fellow mantainer of this code this is the name encoding in case you want to add some new gas type or whatever:
#        
#        Ex. (sdi_init)
#
#        s --> Star product (Star, Optima)
#        di --> Diesel gas (Diesel, gas95, gas98) (First two letters of the name of the product in lowercase)
#        _ --> spacing
#        init --> No discount ("init" (initial price), "gow" gow discount, "wiz" wizink discount, "gowcarr" gow + wizink discount)  

def check_values(df):
    for i in range(len(df["Precio"])):
        
        gas_p = str(df["Precio"][i])

        gas_p = gas_p.replace(',', '.')

        if gas_p == '1.0':
            gas_p = '1.000'

        gas_p_splited = gas_p.split('.')

        if len(gas_p) != 5 or len(gas_p_splited[1]) != 3:
            st.warning(f"Revisa el formato del precio del combustible {df['Carburante'][i]}", icon="🚨")
            return False
    
    return True

def generate_prices(df):

    for i in range(len(df["Precio"])):
        df["Precio"][i] = df["Precio"][i].replace(',', '.') # Replace comma with dot

    sdi = Decimal(str(df["Precio"][0])) # diesel star
    s95 = Decimal(str(df["Precio"][1])) # 95 star
    odi = Decimal(str(df["Precio"][2])) # diesel optima
    o95 = Decimal(str(df["Precio"][3])) # 95 optima
    o98 = Decimal(str(df["Precio"][4])) # 98 optima
    
    # Discounts for star and optima gas depending on the membership

    getcontext().prec = 4
    
    sgow = DISCOUNT_STAR_GOW
    ogow = DISCOUNT_OPTIMA_GOW

    swiz = DISCOUNT_STAR_WIZINK
    owiz = DISCOUNT_OPTIMA_WIZINK

    sgowcarr = DISCOUNT_STAR_GOW_WIZINK
    ogowcarr = DISCOUNT_OPTIMA_GOW_WIZINK

    prices_dict = {
        "sdi_init": sdi,
        "sdi_gow": sdi - sgow,
        "sdi_wiz": sdi - swiz,
        "sdi_gowcarr": sdi - sgowcarr,

        "s95_init": s95,
        "s95_gow": s95 - sgow,
        "s95_wiz": s95 - swiz,
        "s95_gowcarr": s95 - sgowcarr,

        "odi_init": odi,
        "odi_gow": odi - ogow,
        "odi_wiz": odi - owiz,
        "odi_gowcarr": odi - ogowcarr,

        "o95_init": o95,
        "o95_gow": o95 - ogow,
        "o95_wiz": o95 - owiz,
        "o95_gowcarr": o95 - ogowcarr,

        "o98_init": o98,
        "o98_gow": o98 - ogow,
        "o98_wiz": o98 - owiz,
        "o98_gowcarr": o98 - ogowcarr
    }

    sign_template = open("./html/template.html", "r", encoding="utf-8")
    sign = open("./html/sign.html", "w", encoding="utf-8")

    html = sign_template.read()
    sign_template.close()

    for(key, value) in prices_dict.items():
        html = html.replace(f"<span>{key} €</span>", f"<span>{str(value)} €</span>")

    sign.write(html)
    sign.close()

<<<<<<< HEAD
def show_sign(df):
    
    generate_prices(df)

    filename = 'file:///'+os.getcwd()+'/html/' + 'sign.html'
    webbrowser.open_new_tab(filename)
=======
def download_sign(df):
    
    generate_prices(df)

    options = {
    'quiet': '',
    '--enable-local-file-access':''
    }
    
    imgkit.from_file(os.getcwd() + '/html/sign.html', 'out.jpg', options=options)

    with open("./out.jpg", "rb") as image:
        document = image.read()
    
    return document
    
>>>>>>> origin/main

st.image(png_path, width = 250)

df = {
        "Carburante": ["Diesel Star", "95 Star", "Diesel Optima", "95 Optima", "98 Optima"] ,
        "Precio": ["1.333", "1.333", "1.333", "1.333", "1.333"],
}

edited_df = st.data_editor(df, use_container_width=True, hide_index=True, disabled=["Carburante"])

<<<<<<< HEAD
if st.button("Generar Cartel", "Precios_Carburantes.pdf", disabled= not check_values(edited_df)):
    show_sign(edited_df)
=======
st.download_button("Generar Cartel", download_sign(df), "Precios_Carburantes.jpg", disabled= not check_values(edited_df))
>>>>>>> origin/main

st.caption(LEGAL_TEXT)