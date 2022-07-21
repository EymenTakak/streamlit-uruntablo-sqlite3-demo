import streamlit as st
import sqlite3
import pandas as pd

st.markdown("Ürün Panel")

def baglan():
  global conn
  conn=sqlite3.connect("test.db")
  global c
  c=conn.cursor()

def tablo():
  c.execute("CREATE TABLE IF NOT EXISTS urunler(isim TEXT, fiyat REAL, marka TEXT, tarih TEXT, resim TEXT)")
  conn.commit()

def urunekle(name,price,brand,date,image):
  c.execute("INSERT INTO urunler VALUES(?,?,?,?,?)", (name,price,brand,date,image))
  conn.commit()
  return "Başarıyla Eklendi"

def urunlistele():
  c.execute("SELECT * FROM urunler")
  urunler = c.fetchall()
  tablo = pd.DataFrame(urunler)
  st.dataframe(tablo)

  return tablo

def urunsil(isim):
  c.execute(f"DELETE FROM urunler WHERE isim=?",(isim,))

def fiyatguncelle(isim,yenifiyat):
  c.execute(f"UPDATE urunler SET fiyat=? WHERE isim=?", (yenifiyat,isim))
  conn.commit
  return "Başarıyla Güncellendi"

if st.button("Listele"):
  baglan()
  tablo()
  urunlistele()

tab1,tab2,tab3 = st.tabs(["Ürün Ekle","Ürün Sil","Fiyat Güncelle"])

with tab1:
  baglan()
  tablo()
  name = st.text_input("Ürün İsmi: ")
  price = st.number_input("Fiyat: ")
  brand = st.text_input("Marka: ")
  date = st.text_input("Tarih: ")
  image = st.text_input("Fotoğraf: ")

  if st.button("Ekle"):
    urunekle(name,price,brand,date,image)


with tab2:
  tablo()
  baglan()
  isim = st.text_input("Silmek İstediğiniz Ürün İsmi: ")

  if st.button("Sil"):
    urunsil(isim)

with tab3:
  tablo()
  baglan()
  isim2 = st.text_input("Düzenlemek İstediğiniz Ürün İsmi: ")
  fiyat = st.number_input("Yeni Fiyat: ")

  if st.button("Güncelle"):
    fiyatguncelle(isim2,fiyat)